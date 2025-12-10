import sqlite3

def get_db_connection():
    conn = sqlite3.connect("library_logic.db")
    return conn