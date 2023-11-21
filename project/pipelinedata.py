import pandas as pd 

# Daten aus csv Quelle einlesen
df = pd.read_table('https://raw.githubusercontent.com/Pelendones/MADE-project/main/data/produkt_rr_stunde_19970707_20221231_03379.txt', sep=';')

#Nur auf relevante Spalten reduzieren
df = df[['STATIONS_ID', 'MESS_DATUM', 'QN_8', '  R1']]

#Festlegen der Datentypen
dtypes = {'STATIONS_ID': int, 'MESS_DATUM': int, 'QN_8': int, '  R1': float}
df = df.astype(dtypes)

#Bessere Metanamen für die Tabellen
column_mapping = {'QN_8': 'QUALITY', '  R1': 'RAINFALL'}
df = df.rename(columns=column_mapping)

#Muenchen Stadt als Ort eintragen
df['Location'] = 'Muenchen-Stadt'

#Schreiben in eine sqlite Datei mit dem Namen airports.sqlite und dem Tabellennamen airports
df.to_sql('rainweather', 'sqlite:///MADE-project/data/rainweather.sqlite', if_exists='replace', index=False) 

#df = pd.read_table('https://raw.githubusercontent.com/Pelendones/MADE-project/main/data/produkt_rr_stunde_19970707_20221231_03379.txt', sep=';')

#df.to_sql('crashes','sqlite:///crashes.sqlite',if_exists='replace', index=False )