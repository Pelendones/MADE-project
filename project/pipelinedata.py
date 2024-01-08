import pandas as pd
from io import BytesIO
import requests
import zipfile
import matplotlib.pyplot as plt
import numpy as np
import os

# Spezifizieren des Landes und den Regierungsbezirks
land=9
regbez=7

# Spezifizieren des Ortes der Wetterdaten
weatherstation='Muenchen-Stadt'

def load_weather_data(db_name):
    # Erster Datenquelle für die Wetterdaten
    zip_url = 'https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/precipitation/historical/stundenwerte_RR_03379_19970707_20221231_hist.zip'
    response = requests.get(zip_url)
    
    if response.status_code == 200:
        # Zip öffnen und extrahieren
         with zipfile.ZipFile(BytesIO(response.content), 'r') as zip_ref: 
            file_to_read='produkt_rr_stunde_19970707_20221231_03379.txt'
            with zip_ref.open(file_to_read) as file:
                df = pd.read_table(file, sep=';') 

                
    # Nur auf relevante Spalten reduzieren
    df = df[['STATIONS_ID', 'MESS_DATUM', '  R1']]

    # Festlegen der Datentypen
    dtypes = {'STATIONS_ID': "int64", 'MESS_DATUM': "int64", '  R1': float}
    df = df.astype(dtypes)

    # Das aufgespaltene MESS_DATUM transformieren und abspeichern
    df['YEAR'] = df['MESS_DATUM'] // 1000000
    df['MONTH'] = (df['MESS_DATUM'] // 10000) % 100
    df['DAY'] = (df['MESS_DATUM'] // 100) % 100
    df['HOUR'] = df['MESS_DATUM'] % 100

    # Bessere Metanamen für die Tabellen
    column_mapping = {'  R1': 'RAINFALL'}
    df = df.rename(columns=column_mapping) 

    # weatherstation als Ort eintragen
    df['LOCATION'] = weatherstation

    # MESS_DATUM ist nichtmehr benötigt
    df = df.drop('MESS_DATUM', axis=1)

    # Entferne Zeilen mit negativen Niederschlagswerten
    df = df[df['RAINFALL'] >= 0]

    # Schreiben in eine sqlite Datei rainweather.sqlite
    df.to_sql('rainweather', f'sqlite:///data/{db_name}.sqlite', if_exists='replace', index=False)
    print('Done loading the weather database') 

    return df

def load_accident_data(db_name,year):
    # Zweite Datenquelle für die Unfalldaten
    zip_url = f'https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte{year}_EPSG25832_CSV.zip'
    response = requests.get(zip_url)

    # Festlegen der Datentypen 
    dtypes_accidents = {
         'OBJECTID': "int64",
         'ULAND': "int64",
         'UREGBEZ': "int64",
         'UKREIS': "int64",
         'UGEMEINDE': "int64",
         'UJAHR': "int64",
         'UMONAT': "int64", 
         'USTUNDE': "int64",
         'UWOCHENTAG': "int64",
         'UKATEGORIE': "int64",
         'UART': "int64",
         'UTYP1': "int64", 
         'IstRad': "int64", 
     }

    # Wenn Anfrage erfolgreich
    if response.status_code == 200:
        # Zip öffnen und extrahieren 
         with zipfile.ZipFile(BytesIO(response.content), 'r') as zip_ref:
            # Kleine Abweichungen bei den zips ausgleichen
            file_to_read = f'csv/Unfallorte{year}_LinRef.txt'

            if year == '2016':
                file_to_read = f'csv/Unfallorte_{year}_LinRef.txt' 

            if year == '2020':
                file_to_read = f'csv/Unfallorte{year}_LinRef.csv'
            
            if year == '2021':
                file_to_read = f'Unfallorte{year}_EPSG25832_CSV.csv'

            if year == '2022':
                file_to_read = f'Unfallorte{year}_LinRef.csv' 

            with zip_ref.open(file_to_read) as file:
                df_zip = pd.read_table(file, sep=';', dtype=dtypes_accidents)

            # Weitere Abweichugen vereinheitlichen
            if year == '2018':
                column_mapping = {'OBJECTID_1': 'OBJECTID'}
                df_zip = df_zip.rename(columns=column_mapping)     

            # Nur auf relevante Spalten reduzieren
            df_zip = df_zip[['OBJECTID', 'ULAND', 'UREGBEZ', 'UKREIS', 'UGEMEINDE', 'UJAHR', 'UMONAT', 'USTUNDE', 'UWOCHENTAG', 'UKATEGORIE', 'UART', 'UTYP1', 'IstRad']] 

            # Schreiben in eine sqlite Datei mit dem Namen crashes.sqlite
            df_zip.to_sql('crashes', f'sqlite:///data/{db_name}{year}.sqlite', if_exists='replace', index=False)
            print(f'Done loading the {year} crash database')
            return df_zip 


def main():
    db_name_accident = 'crashes' 
    load_weather_data('rainweather') 
    load_accident_data(db_name_accident,year='2016')
    load_accident_data(db_name_accident,year='2017')
    load_accident_data(db_name_accident,year='2018')
    load_accident_data(db_name_accident,year='2019')
    load_accident_data(db_name_accident,year='2020')
    load_accident_data(db_name_accident,year='2021')
    load_accident_data(db_name_accident,year='2022') 


if __name__ == "__main__":
    main()