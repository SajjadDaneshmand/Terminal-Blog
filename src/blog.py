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

def create_table():
    blog_table = '''
    CREATE TABLE IF NOT EXISTS Blog(
        id INTEGER PRIMARY KEY UNIQUE,
        post VARCHAR(50) NOT NULL,
        description TEXT
    );
    '''
    conn = create_database('Blog.db')
    cursor = conn.cursor()
    cursor.execute(blog_table)
    conn.commit()


#################### INSERT DATA TO DATABASE ####################

def post_and_description(post,description):
    insert_data = '''
        INSERT INTO Blog(id,post,description)
        VALUES({},{})
    '''

#################### READ DATA FROM DATABASE ####################

def read_all_post():
    pass

def read_all_description():
    pass