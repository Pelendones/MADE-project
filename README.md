
## Made Project bicycle crashes with correlation to rainy weather
[![Bicycle Picture](https://images.unsplash.com/uploads/14122621859313b34d52b/37e28531?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)](https://unsplash.com/de/fotos/schwarzes-mountainbike-in-der-nahe-der-strasse-geparkt-AoSAOV2Vtro)
This project tries to see if there is a correlation between rainy weather and bicycle crashes and if it is a stronger correlation than all accidents in the same area. For more information and sources you can visit the `project/project-plan.md` file.

## Repository Information
This repository is a fork of the [2023-amse-template repository](https://github.com/jvalue/2023-amse-template).  
It was established for the purpose of engaging in data engineering and data science projects and exercises, utilizing open data sources.  
The creation of this repository is aligned with the curriculum of the [AMSE](https://oss.cs.fau.de/teaching/specific/amse/) course offered during the Summer semester in 2023 by the [FAU Chair for Open-Source Software](https://oss.cs.fau.de/).

## Project Structure
The important files to run the project are listed below.
```bash
data/
├── data/                       # Data directory
│   └──                         # The databases will be stored here after the ETL process and Test pipeline
project/ 
├── tests/                      # Test directory
│   ├── __init__.py 
│   └── test_pipeline.py        # Test cases for checking the databases after the ETL process
├── data-exploration.ipynb      # !Important file: A Notebook used to explore the downloaded databases in the data folder
├── pipeline.sh                 # !Important file: The script that runs the ETL and main file of the project 
├── pipelinedata.py             # Main file and entry point of the project 
├── project-plan.md             # The plan and goals for the project
├── report.pdf                  # !Important file: A pdf that contains the report of the project
└── tests.sh                    # !Important file: Script for running all test cases
requirements.txt                # All needed packages needed to build the project
README.md                       # The document you are reading now. 
```

## Correctly install and run/modify the project

1. You can clone the github repository:
```bash
git clone https://github.com/Pelendones/MADE-project.git
```
2. After installing Python you can create a virtual environment inside the repo and activate it:
```bash
python3 -m venv <your_env_name>
source <your_env_name>/bin/activate
```
3. The requirements.txt provides you with all the packages that are needed for the project. You can install all the packages for your virtual enviroment, by running this command:
```bash
pip install -r requirements.txt
```
4. After installing the requirements you can run the pipeline to retrieve the databases that will be stored inside the `data` folder. One database will be called `rainweather` and contain the weather data of the station selected from the source and added to the `pipelinedata.py`. Seven more databases will be created labled `crashesX.sqlite` where X is the year of the database from 2016 until 2022.
```bash
cd project/
chmod +x pipeline.sh
sh pipeline.sh
```
or alternatively you can just run the python file to get the same result:
```bash
cd project/
python3 pipelinedata.py
```

5. If you want to run the test and see if pipeline was executed correctly you can run the included tests.  
Make sure you are in the project folder and make the test script executable:
```bash
chmod +x tests.sh
```
6. Then from the project folder you can run the test script and check the results:
```bash 
sh tests.sh
```
7. The `project/data-exploration.ipynb` is a project notebook where you can view the contents of the databases and modify it for your own project. In the `project/reports.pdf` you can read the detailed report of the data exploration.

## Rest of the folders and files inside the project
The rest of the files inside the `examples` and `exercises` folder were used for the class course for additional work and examples of older projects. These are not needed to build the project and can be optionally ignored or deleted