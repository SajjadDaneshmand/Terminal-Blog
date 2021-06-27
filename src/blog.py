# standard
import sqlite3
import os

################### CREATE TABLE AND DATABASE ###################

def create_database(path):
    try:
        conn = sqlite3.connect(path)
        return conn
    except:
        print('something went wrong at create_database func')

def create_table(name):
    pass

#################### INSERT DATA TO DATABASE ####################

def insert_post(post):
    pass

def insert_description(description):
    pass

#################### READ DATA FROM DATABASE ####################

def read_all_post():
    pass

def read_all_description():
    pass