import logging
from numpy import NaN
from project.pipelinedata import load_accident_data, load_weather_data, main

import sys
import os
import sqlite3
import pandas as pd
from pandas.testing import assert_frame_equal

db_name_test = 'test_db'

def load(data, db_name):
    conn = sqlite3.connect(db_name)
    data.to_sql('load_table', conn, if_exists='replace', index=False)
    conn.close()

def test_load_weather():
    datadirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}.sqlite') 
    data_expected = load_weather_data(db_name_test)
    try:
        connection = sqlite3.connect(datadirectory)
        result = pd.read_sql_query(f"SELECT * FROM rainweather", connection)
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()

    assert_frame_equal(data_expected,result)
    os.remove(datadirectory)

def test_load_crashes_2016():
    year = '2016'
    crashdirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}{year}.sqlite') 
    data_expected = load_accident_data(db_name_test,year) 
    try:
        connection = sqlite3.connect(crashdirectory)
        result = pd.read_sql_query(f"SELECT * FROM crashes", connection) 
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()    

    assert_frame_equal(data_expected,result)
    os.remove(crashdirectory)

def test_load_crashes_2017():
    year = '2017'
    crashdirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}{year}.sqlite') 
    data_expected = load_accident_data(db_name_test,year) 
    try:
        connection = sqlite3.connect(crashdirectory)
        result = pd.read_sql_query(f"SELECT * FROM crashes", connection) 
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()    

    assert_frame_equal(data_expected,result)
    os.remove(crashdirectory)

def test_load_crashes_2018():
    year = '2018'
    crashdirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}{year}.sqlite') 
    data_expected = load_accident_data(db_name_test,year) 
    try:
        connection = sqlite3.connect(crashdirectory)
        result = pd.read_sql_query(f"SELECT * FROM crashes", connection) 
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()    

    assert_frame_equal(data_expected,result)
    os.remove(crashdirectory)

def test_load_crashes_2019():
    year = '2019'
    crashdirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}{year}.sqlite') 
    data_expected = load_accident_data(db_name_test,year) 
    try:
        connection = sqlite3.connect(crashdirectory)
        result = pd.read_sql_query(f"SELECT * FROM crashes", connection) 
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()    

    assert_frame_equal(data_expected,result)
    os.remove(crashdirectory)

def test_load_crashes_2020():
    year = '2020'
    crashdirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}{year}.sqlite') 
    data_expected = load_accident_data(db_name_test,year) 
    try:
        connection = sqlite3.connect(crashdirectory)
        result = pd.read_sql_query(f"SELECT * FROM crashes", connection) 
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()    

    assert_frame_equal(data_expected,result)
    os.remove(crashdirectory)

def test_load_crashes_2021():
    year = '2021'
    crashdirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}{year}.sqlite') 
    data_expected = load_accident_data(db_name_test,year) 
    try:
        connection = sqlite3.connect(crashdirectory)
        result = pd.read_sql_query(f"SELECT * FROM crashes", connection) 
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()    

    assert_frame_equal(data_expected,result)
    os.remove(crashdirectory)

def test_load_crashes_2022():
    year = '2022'
    crashdirectory = os.path.join(os.getcwd(),'data',f'{db_name_test}{year}.sqlite') 
    data_expected = load_accident_data(db_name_test,year) 
    try:
        connection = sqlite3.connect(crashdirectory)
        result = pd.read_sql_query(f"SELECT * FROM crashes", connection) 
    except sqlite3.Error as e:
        logging.error(msg=f"Error while creating SQLite DB: {e}")
        sys.exit(1)
    finally:
        connection.close()    

    assert_frame_equal(data_expected,result)
    os.remove(crashdirectory)
            

