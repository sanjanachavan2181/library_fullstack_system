import sqlite3

DB_NAME = "library.db"

def insert_book(title, author, quantity):
    """
    Inserts a new book into the books table.
    Validates all fields before insertion.
    """

    # -------- VALIDATION --------
    if not title.strip() or not author.strip() or not quantity:
        return "ERROR: All fields are required."

    try:
        quantity = int(quantity)
        if quantity <= 0:
            return "ERROR: Quantity must be greater than 0."
    except:
        return "ERROR: Quantity must be a number."


    # -------- DATABASE INSERT --------
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO books (title, author, quantity)
            VALUES (?, ?, ?)
        """, (title, author, quantity))

        conn.commit()
        conn.close()

        return "SUCCESS"

    except sqlite3.OperationalError as e:
        return f"Database Error: {e}"

    except Exception as ex:
        return f"Unexpected Error: {ex}"
