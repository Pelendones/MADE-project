import pandas as pd 

# Daten aus csv Quelle einlesen
df = pd.read_csv('https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv', sep=';') 

# Schreiben in eine sqlite Datei mit dem Namen airports.sqlite und dem Tabellennamen airports
df.to_sql('airports','sqlite:///airports.sqlite',if_exists='replace', index=False )
