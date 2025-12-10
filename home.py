import tkinter as tk
from pages.add_book import AddBook
from pages.delete_book import DeleteBook
from pages.display_book import DisplayBook

class HomePage:
    def _init_(self, root):
        self.root = root
        
        tk.Label(root, text="Library Home Page", font=("Arial", 18)).pack(pady=20)

        tk.Button(root, text="Add Book", width=20, command=self.open_add_book).pack(pady=10)
        tk.Button(root, text="Delete Book", width=20, command=self.open_delete_book).pack(pady=10)
        tk.Button(root, text="Display Books", width=20, command=self.open_display_book).pack(pady=10)

    def open_add_book(self):
        AddBook()

    def open_delete_book(self):
        DeleteBook()

    def open_display_book(self):
        DisplayBook()