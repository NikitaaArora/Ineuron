from book_users import Book, User


class Admin:
    def __init__(self):
        self.books=[]
        self.users= {}

    def add_book(self, book_id, book_name, book_quantity):
        book = Book(book_id, book_name, book_quantity)
        self.books.append(book)
        print(f"Book {book.name} added successfulyy")
        