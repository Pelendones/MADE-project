import pandas as pd
from io import BytesIO
import requests
import zipfile 

def load_weather_data():
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
    df = df[['STATIONS_ID', 'MESS_DATUM', 'QN_8', '  R1']]

    # Festlegen der Datentypen
    dtypes = {'STATIONS_ID': int, 'MESS_DATUM': int, 'QN_8': int, '  R1': float}
    df = df.astype(dtypes)

    # Bessere Metanamen für die Tabellen
    column_mapping = {'QN_8': 'QUALITY', '  R1': 'RAINFALL'}
    df = df.rename(columns=column_mapping)

    # Muenchen Stadt als Ort eintragen
    df['Location'] = 'Muenchen-Stadt'

    # Schreiben in eine sqlite Datei rainweather.sqlite
    df.to_sql('rainweather', 'sqlite:///MADE-project/data/rainweather.sqlite', if_exists='replace', index=False)
    print('Done loading the weather database')

def load_accident_data(year):
    # Zweite Datenquelle für die Unfalldaten
    zip_url = f'https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte{year}_EPSG25832_CSV.zip'
    response = requests.get(zip_url)

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
                df_zip = pd.read_table(file, sep=';')

            # Weitere Abweichugen vereinheitlichen
            if year == '2018':
                column_mapping = {'OBJECTID_1': 'OBJECTID'}
                df_zip = df_zip.rename(columns=column_mapping)     

            # Nur auf relevante Spalten reduzieren
            df_zip = df_zip[['OBJECTID', 'ULAND', 'UREGBEZ', 'UKREIS', 'UGEMEINDE', 'UJAHR', 'UMONAT', 'USTUNDE', 'UWOCHENTAG', 'UKATEGORIE', 'UART', 'UTYP1', 'IstRad']]

            # Festlegen der Datentypen
            dtypes_accidents = {
                'OBJECTID': int,
                'ULAND': str,
                'UREGBEZ': int,
                'UKREIS': int,
                'UGEMEINDE': int,
                'UJAHR': int,
                'UMONAT': int, 
                'USTUNDE': int,
                'UWOCHENTAG': int,
                'UKATEGORIE': int,
                'UART': int,
                'UTYP1': int, 
                'IstRad': int, 
                }
            df_zip = df_zip.astype(dtypes_accidents)

            # Schreiben in eine sqlite Datei mit dem Namen crashes.sqlite
            df_zip.to_sql('crashes', f'sqlite:///MADE-project/data/crashes{year}.sqlite', if_exists='replace', index=False)
            print(f'Done loading the {year} crash database') 


def main(): 
    load_weather_data()
    #load_accident_data(year='2016')
    #load_accident_data(year='2017')
    #load_accident_data(year='2018')
    #load_accident_data(year='2019')
    #load_accident_data(year='2020')
    #load_accident_data(year='2021')
    #load_accident_data(year='2022') 


if __name__ == "__main__":
    main()