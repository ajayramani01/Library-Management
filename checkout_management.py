from models import Checkout
import book_management
import user_management
import storage

class CheckoutManagement:
    def __init__(self):
        self.checkouts = storage.load_from_file('checkouts.json', Checkout)

    def checkout_book(self, user_id, isbn):
        if not user_id or not isbn:
            print("User ID and ISBN are required.")
            return None
        user = user_management.user_management.find_user_for_book(user_id)
        if not user:
            print(f"User_id : {user_id} does not exist.")
            return None
        book = book_management.book_management.find_book_by_isbn(isbn)
        if not book:
            print(f"Book with ISBN {isbn} does not exist.")
            return None
        if not book.available:
            print(f"Book with ISBN {isbn} is not available.")
            return None
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        self.save_checkouts()
        book.available = False
        book_management.book_management.save_books()
        print(f"Book with ISBN {isbn} checked out successfully.")

    def save_checkouts(self):
        storage.save_to_file(self.checkouts, 'checkouts.json')

checkout_management = CheckoutManagement()
