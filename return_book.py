def return_book(book_id, student_name):
    conn = get_db_connection()
    cur = conn.cursor()

    # Increase quantity based on books.id
    cur.execute("UPDATE books SET quantity = quantity + 1 WHERE id = ?", (book_id,))

    # Update issued_books
    cur.execute("""
        UPDATE issued_books
        SET remark = 'Returned'
        WHERE book_id = ? AND student_name = ?
    """, (book_id, student_name))

    conn.commit()
    conn.close()
