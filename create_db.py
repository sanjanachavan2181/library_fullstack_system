import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    student_name TEXT NOT NULL,
    issue_date TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully.")
