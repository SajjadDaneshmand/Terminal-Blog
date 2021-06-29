# internal
import connectin

# standard
import sqlite3
import os


#################### INSERT DATA TO DATABASE ####################

def insert_post(title,description,category_id):
    insert_data = """
        INSERT INTO post(title, description, category_id)
        VALUES(?, ?, ?)
    """
    info = (title, description, category_id)
    conn = connectin.db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_data, info)
    conn.commit()
    conn.close()
    

def insert_category(name):
    insert_data = """
        INSERT INTO category(name)
        VALUES(?)
    """
    info = (name,)
    conn = connectin.db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_data, info)
    cursor.close()
    conn.commit()
    conn.close()

#################### READ DATA FROM DATABASE ####################

def read_posts():
    conn = connectin.db_connection()
    cursor = conn.cursor()
    data = []
    data_showing = """
            SELECT title, description FROM post
        """
    for i in cursor.execute(data_showing):
        data.append(i)
    return data

def read_all_category():
    pass