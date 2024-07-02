from models import User
import storage

class UserManagement:
    def __init__(self):
        self.users = storage.load_from_file('users.json', User)

    def add_user(self, name, user_id):
        if not name or not user_id:
            print("Name and User ID are required.")
            return
        user = User(name, user_id)
        self.users.append(user)
        self.save_users()

    def search_users(self, attribute, value):
        if attribute not in ['name','user_id'] :
            print("Enter the correct attribute")
            return None
        results = [user for user in self.users if getattr(user, attribute) == value]
        if results:
            for user in results:
                print(user.to_dict())
        else:
            print("No users found.")

    def find_user_for_book(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def list_users(self):
        for user in self.users:
            print(user.to_dict())

    def save_users(self):
        storage.save_to_file(self.users, 'users.json')

user_management = UserManagement()
