import tkinter as tk
from tkinter import messagebox

class DeleteBook:
    def _init_(self):
        self.win = tk.Toplevel()
        self.win.title("Delete Book")
        self.win.geometry("300x300")

        tk.Label(self.win, text="Enter Book Name to Delete").pack(pady=10)
        self.book_entry = tk.Entry(self.win)
        self.book_entry.pack()

        tk.Button(self.win, text="Delete", command=self.delete_book).pack(pady=10)

    def delete_book(self):
        book = self.book_entry.get()
        if book == "":
            messagebox.showerror("Error", "Book name required")
        else:
            messagebox.showinfo("Success", "Book Deleted Successfully")