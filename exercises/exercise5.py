import os
import pandas as pd
from urllib.request import urlretrieve
import zipfile
import sqlite3 

gtfs_url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
zip_file_path, _ = urlretrieve(gtfs_url, "GTFS.zip")

# Extrahiere die Daten
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall("GTFS_data")

# Lese die daten aus der csv ein
stops_df = pd.read_csv("GTFS_data/stops.txt", usecols=['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id'], encoding='latin1')

# Nur zone id 2001 wird benoetigt
stops_df = stops_df[stops_df['zone_id'] == 2001]

# Validiere daten nach folgenden Kriterien
# stop_name can be any text but must maintain german umlauts
# stop_lat/stop_lon must be a geographic coordinates between -90 and 90, including upper/lower bounds
# Drop rows containing invalid data 
stops_df['stop_name'] = stops_df['stop_name'].apply(lambda x: x.encode('latin1', 'replace').decode('utf-8', 'replace'))
stops_df['stop_lat'] = pd.to_numeric(stops_df['stop_lat'], errors='coerce')
stops_df['stop_lon'] = pd.to_numeric(stops_df['stop_lon'], errors='coerce')
stops_df = stops_df.dropna(subset=['stop_lat', 'stop_lon'])
stops_df = stops_df[(stops_df['stop_lat'] >= -90) & (stops_df['stop_lat'] <= 90)]
stops_df = stops_df[(stops_df['stop_lon'] >= -90) & (stops_df['stop_lon'] <= 90)] 

# Zurueck in die Datenbank schreiben
conn = sqlite3.connect("gtfs.sqlite")

column_types = {
    'stop_id': 'BIGINT',
    'stop_name': 'TEXT',
    'stop_lat': 'FLOAT',
    'stop_lon': 'FLOAT',
    'zone_id': 'BIGINT'
}

stops_df.to_sql('stops', conn, if_exists='replace', index=False)
conn.close() 

# Loesche die Dateien am Ende um aufzuraeumen
os.remove(zip_file_path)

#Loesche alle Dateien in dem Ordner da os.rmdir nur mit leeren Ordner funktioniert und dann loesche den Ordner
for file_name in os.listdir("GTFS_data"):
    file_path = os.path.join("GTFS_data", file_name)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            os.rmdir(file_path)
    except Exception as e:
        print(f"Fehler: {e}")
os.rmdir("GTFS_data")