# internal
import functions

# standard
import sqlite3
import os


from colorama import Fore


#################### INSERT DATA TO DATABASE ####################

def insert_post(title,description,category_id):
    '''This function insert title, descripton and category_id to post table from blog database'''
    insert_data = """
        INSERT INTO post(title, description, category_id)
        VALUES(?, ?, ?)
    """
    info = (title, description, category_id)
    conn = functions.db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_data, info)
    conn.commit()
    conn.close()
    

def insert_category(name):
    '''This function insert name of category to category table'''
    insert_data = """
        INSERT INTO category(name)
        VALUES(?)
    """
    info = (name,)
    conn = functions.db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_data, info)
    cursor.close()
    conn.commit()
    conn.close()

#################### READ DATA FROM DATABASE ####################

def id_and_title():
    '''This function return id and title column from post table'''
    conn = functions.db_connection()
    cursor = conn.cursor()
    titles = """
            SELECT id, title
            FROM post
        """
    data = ['id : title']
    for row in cursor.execute(titles):
        data.append(f'{row[0]} : {row[1]}')
    return data

def categories():
    '''This function return name column from category table'''
    conn = functions.db_connection()
    cursor = conn.cursor()
    names = """
            SELECT id, name
            FROM category
        """
    data = ['id : name']
    for row in cursor.execute(names):
        data.append(f'{row[0]} : {row[1]}')
    return data
def get_description():
    while True:
        try:
            ID = int(input(Fore.WHITE + 'Give me the ID you want: '))
        except:
            print(Fore.RED+'give me a number not string or None')
            continue
        description = """
                SELECT title, description
                FROM post
                WHERE id = ?
            """
        info = (ID,)
        conn = functions.db_connection()
        cursor = conn.cursor()
        try:
            for row in cursor.execute(description, info):
                row = f'{Fore.GREEN}{row[0]} : {Fore.WHITE}{row[1]}'
                print(row)
            break
        except:
            print(Fore.RED + 'your number is out of range' + Fore.WHITE)