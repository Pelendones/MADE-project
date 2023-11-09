import pandas as pd 

# Daten aus csv einlesen
df = pd.read_csv('https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv', sep=';') 

dtype_dict = {
    'column_1': 'INTEGER',
    'column_2': 'TEXT',
    'column_3': 'TEXT',
    'column_4': 'TEXT',
    'column_5': 'TEXT',
    'column_6': 'TEXT',
    'column_7': 'REAL',
    'column_8': 'REAL',
    'column_9': 'INTEGER',
    'column_10': 'TEXT',
    'column_11': 'TEXT',
    'column_12': 'TEXT',
    'geo_punkt': 'TEXT'
} 

#Schreiben in eine sqlite Datei mit dem Namen airports.sqlite und dem Tabellennamen airports und manuelles setzen der Datentypen BIGINT, TEXT or FLOAT
df.to_sql('airports','sqlite:///airports.sqlite',if_exists='replace', index=False, #dtype=dtype_dict
          )
