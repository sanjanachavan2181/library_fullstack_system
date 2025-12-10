import tkinter as tk
from library_logic import get_all_books

class DisplayBook:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("display Books")
        self.win.geometry("600x400")

        tk.Label(self.win, text="Books List", font=("Arial", 18, "bold")).pack(pady=10)

        table_frame = tk.Frame(self.win)
        table_frame.pack(pady=10)

        headings = ["Book ID", "Book Name", "Author", "Quantity"]

        for col, heading in enumerate(headings):
            tk.Label(table_frame, text=heading, font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=15).grid(row=0, column=col)

        books = get_all_books()

        for row, book in enumerate(books, start=1):
            tk.Label(table_frame, text=book[0], borderwidth=1, relief="solid", width=15).grid(row=row, column=0)
            tk.Label(table_frame, text=book[1], borderwidth=1, relief="solid", width=15).grid(row=row, column=1)
            tk.Label(table_frame, text=book[2], borderwidth=1, relief="solid", width=15).grid(row=row, column=2)
            tk.Label(table_frame, text=book[3], borderwidth=1, relief="solid", width=15).grid(row=row, column=3)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    DisplayBook()
    root.mainloop()
