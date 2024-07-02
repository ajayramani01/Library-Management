from models import Book
import storage

class BookManagement:
    def __init__(self):
        self.books = storage.load_from_file('books.json', Book)

    def add_book(self, title, author, isbn):
        if not title or not author or not isbn:
            print("All fields are required.")
            return
        book = Book(title, author, isbn)
        self.books.append(book)

        self.save_books()

    def search_books(self, attribute, value):
        if attribute not in ['title','author','isbn']:
            print("Enter the correct attribute")
            return
        results = [book for book in self.books if getattr(book, attribute) == value]
        if results:
            for book in results:
                print(book.to_dict())
        else:
            print("No books found.")

    def list_books(self):
        if len(self.books) == 0:
            print("No books found.")
        else:
            for book in self.books:
                print(book.to_dict())

    def save_books(self):
        storage.save_to_file(self.books, 'books.json')

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book_by_isbn(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            self.save_books()

book_management = BookManagement()
