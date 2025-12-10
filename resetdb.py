import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

print("Deleting old tables...")

cur.execute("DROP TABLE IF EXISTS books")
cur.execute("DROP TABLE IF EXISTS issued_books")

print("Recreating tables...")

cur.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    quantity INTEGER NOT NULL
);
""")

cur.execute("""
CREATE TABLE issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    student_name TEXT,
    issue_date TEXT,
    return_date TEXT,
    remark TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id)
);
""")

conn.commit()
conn.close()

print("Database reset successfully!")
