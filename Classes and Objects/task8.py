# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 8: Library System
# Run with: python task8.py

class Book:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.borrowed_by = None          # None means it is on the shelf

    def is_available(self):
        return self.borrowed_by is None


class Library:
    def __init__(self):
        self.books = {}                  # code -> Book object

    def add_book(self, code, title):
        self.books[code] = Book(code, title)

    def borrow(self, code, student):
        book = self.books.get(code)
        if book is None:
            return "No such book."
        if not book.is_available():
            return f"'{book.title}' is already out with {book.borrowed_by}."
        book.borrowed_by = student
        return f"{student} borrowed '{book.title}'."

    def give_back(self, code):
        book = self.books.get(code)
        if book is None or book.is_available():
            return "That book is not on loan."
        book.borrowed_by = None
        return f"'{book.title}' is back on the shelf."

    def report(self):
        for book in self.books.values():
            if book.is_available():
                status = "available"
            else:
                status = f"out: {book.borrowed_by}"
            print(f"  {book.code}  {book.title:<26}{status}")


library = Library()
library.add_book("B1", "Python Crash Course")
library.add_book("B2", "Networking Essentials")
library.add_book("B3", "Web Design with HTML")

print(library.borrow("B1", "Omar Farah"))
print(library.borrow("B1", "Mercy Achieng"))
print(library.borrow("B9", "Mercy Achieng"))
print(library.give_back("B1"))
print(library.borrow("B3", "Mercy Achieng"))
print("Library report:")
library.report()
