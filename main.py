import book_management
import user_management
import checkout_management

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Books")
    print("4. Add User")
    print("5. List Users")
    print("6. Search Users")
    print("7. Checkout Book")
    print("8. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_management.book_management.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            book_management.book_management.list_books()
        elif choice == '3':
            attribute = input("Search by (title/author/isbn): ")
            value = input(f"Enter {attribute}: ")
            book_management.book_management.search_books(attribute, value)
        elif choice == '4':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_management.user_management.add_user(name, user_id)
            print("User added.")
        elif choice == '5':
            user_management.user_management.list_users()
        elif choice == '6':
            attribute = input("Search by (name/user_id): ")
            value = input(f"Enter {attribute}: ")
            user_management.user_management.search_users(attribute, value)
        elif choice == '7':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            res = checkout_management.checkout_management.checkout_book(user_id, isbn)
            if res is not None:
                print("Book checked out.")
        elif choice == '8':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
