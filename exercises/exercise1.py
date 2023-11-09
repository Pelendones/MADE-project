import pandas as pd

# Daten aus csv einlesen
df = pd.read_csv('rhein-kreis-neuss-flughafen-weltweit.csv', sep=';') 

#Schreiben in eine sqlite Datei mit dem Namen airports.sqlite und dem Tabellennamen airports und manuelles setzen der Datentypen BIGINT, TEXT or FLOAT
df.to_sql('airports','airports.sqlite',if_exists='replace', index=False, dtype={
        'column_1':'INT',
        'column_2': 'TEXT',
        'column_3': 'TEXT',
        'column_4': 'TEXT',
        'column_5': 'TEXT ',
        'column_6': 'TEXT',
        'column_7': 'FLOAT',
        'column_8': 'FLOAT',
        'column_9': 'INT',
        'column_10': 'TEXT',
        'column_11': 'TEXT',
        'column_12': 'TEXT',
        'geo_punkt': 'TEXT'
})
