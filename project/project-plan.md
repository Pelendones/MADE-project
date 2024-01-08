# Project Plan

## Title
<!-- Give your project a short title. -->
MADE Project correlation between weather and bicycle accidents.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Does rainy weather influence the frequency of bicycle accidents?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Understanding the influences in bicycle accidents can us help identifying the possible dangers and correlations. 
The data from the first Datasources only describe the condition of the road and not the current weather. 
I want to combine this data with a dataset of current weather in the month of the bicycle accident and see if there is a correlation with the amount of accidents.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1 GOVDATA: 
* Metadata URL: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/DSB_Unfallatlas.pdf
* Metadata URL ENG: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/DSB_Unfallatlas_EN.pdf
* Data URL 2016: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte2016_EPSG25832_CSV.zip
* Data URL 2017: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte2017_EPSG25832_CSV.zip
* Data URL 2018: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte2018_EPSG25832_CSV.zip
* Data URL 2019: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte2019_EPSG25832_CSV.zip
* Data URL 2020: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte2020_EPSG25832_CSV.zip
* Data URL 2021: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte2021_EPSG25832_CSV.zip
* Data URL 2022: https://www.opengeodata.nrw.de/produkte/transport_verkehr/unfallatlas/Unfallorte2022_EPSG25832_CSV.zip
* Data Type: CSV
* URI: https://unfallatlas.statistikportal.de/
* License: dl-de/by-2-0 https://www.govdata.de/dl-de/by-2-0

GOVDATA provides a "Unfallatlas Deutschland" which can be translated to "Accident Atlas Germany". It provides a good dataset of accidents with personal injuries on the streets in Germany.

### Datasource2 Weatherdata Deutscher Wetterdienst:
* Metadata URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/precipitation/historical/stundenwerte_RR_03379_19970707_20221231_hist.zip
  * Inside the ZIP File
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/precipitation/historical/stundenwerte_RR_03379_19970707_20221231_hist.zip
* Data Type: Zip File as a TXT
* License: https://opendata.dwd.de/climate_environment/CDC/Nutzungsbedingungen_German.pdf

The German Wetterdienst is providing the amount of historical rainfall in hourly measure points. The study will look at the data of München, but can be expanded to other cities, too.