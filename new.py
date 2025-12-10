DROP TABLE IF EXISTS issued_books;

CREATE TABLE issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id TEXT,
    student_name TEXT,
    issue_date TEXT,
    return_date TEXT,
    remark TEXT
);
