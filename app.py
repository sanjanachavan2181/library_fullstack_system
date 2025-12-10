import sqlite3
from flask import Flask, render_template, request, redirect
from db_connection import get_db_connection
from add_book import insert_book

from library_logic import (
    add_book,
    get_all_books,
    issue_book,
    return_book as return_book_logic,   # IMPORTANT FIX
    get_issued_books
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book_route():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        quantity = request.form['quantity']

        result = insert_book(title, author, quantity)

        if result == "SUCCESS":
            return redirect('/')
        else:
            return result

    return render_template('add_book.html')
@app.route("/view_books")
def view_books():
    books = get_all_books()
    return render_template("display_books.html", books=books)




@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book_route():
    if request.method == 'POST':
        book_id = request.form['book_id']
        student_name = request.form['student_name']
        issue_date = request.form['issue_date']
        return_date = request.form['return_date']
        remark = request.form['remark']

        issue_book(book_id, student_name, issue_date, return_date, remark)

        return redirect('/view_issued_books')

    return render_template('issue_book.html')




@app.route('/return_book', methods=['GET', 'POST'])
def return_book_route():     # NEW UNIQUE NAME
    if request.method == 'POST':
        book_id = request.form['book_id']
        student_name = request.form['student_name']

        return_book_logic(book_id, student_name)   # FIXED CALL
        return redirect('/')

    return render_template('return_book.html')

@app.route('/view_issued_books')
def view_issued_books():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM issued_books")
    issued_books = cur.fetchall()
    print("DEBUG:", issued_books)

    conn.close()

    return render_template("view_issued_books.html", issued_books=issued_books)



if __name__ == '__main__':
    app.run(debug=True)
