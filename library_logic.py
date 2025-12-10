import sqlite3

def get_db_connection():
    conn = sqlite3.connect("library.db")
    return conn


# ------------------- ADD BOOK -------------------
def add_book(book_id, book_name, author, qty):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO books (book_id, book_name, author, qty)
        VALUES (?, ?, ?, ?)
    """, (book_id, book_name, author, qty))

    conn.commit()
    conn.close()


# ------------------- GET ALL BOOKS -------------------
def get_all_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()
    return books


# ------------------- ISSUE BOOK -------------------
def issue_book(book_id, student_name, issue_date, return_date, remark):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO issued_books (book_id, student_name, issue_date, return_date, remark)
        VALUES (?, ?, ?, ?, ?)
    """, (book_id, student_name, issue_date, return_date, remark))

    conn.commit()
    conn.close()






# ------------------- RETURN BOOK -------------------

def return_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("UPDATE books SET qty = qty + 1 WHERE book_id = ?", (book_id,))

    conn.commit()
    conn.close()

def get_issued_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM issued_books")
    data = cursor.fetchall()
    conn.close()
    return data
