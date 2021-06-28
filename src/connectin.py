# internal
import settings

# standard
import sqlite3

def db_connection():
    '''This function give me a connection of blog database'''
    return sqlite3.connect(settings.DATABASE_PATH)
