import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    quantity INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    student_name TEXT,
    issue_date TEXT,
    return_date TEXT,
    remark TEXT
)
""")

conn.commit()
conn.close()

print("DATABASE FIXED SUCCESSFULLY!")
