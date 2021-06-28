# internal
import settings

# standard
import sqlite3

def db_connection():
    return sqlite3.connect(settings.DATABASE_PATH)
