import sqlite3

def get_db_connection():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    c = conn.cursor()

    # books table
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            quantity INTEGER
        )
    ''')

    # issued books table
    c.execute('''
        CREATE TABLE IF NOT EXISTS issued_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            student_name TEXT,
            issue_date TEXT,
            return_date TEXT,
            remark TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_book(title, author, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
                   (title, author, quantity))
    conn.commit()
    conn.close()