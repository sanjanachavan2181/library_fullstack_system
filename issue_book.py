from flask import Blueprint, render_template, request
from datetime import datetime, timedelta
import sqlite3

issue_book_bp = Blueprint('issue_book', __name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

@issue_book_bp.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        student_name = request.form['student_name']
        issue_date = request.form['issue_date']
        return_date = request.form['return_date']
        remark = request.form['remark']

        conn = get_db_connection()
        c = conn.cursor()

        c.execute("""
            INSERT INTO issued_books (book_id, student_name, issue_date, return_date, remark)
            VALUES (?, ?, ?, ?, ?)
        """, (book_id, student_name, issue_date, return_date, remark))

        conn.commit()
        conn.close()

        return render_template("issue_success.html")

    return render_template("issue_book.html")
