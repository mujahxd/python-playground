# auth.py (Authentication Management)
from storage import load_data, save_data
from utils import hash_password, verify_password

def register():
    """Register a new user with username and password."""
    users = load_data("users.json")


    while True:
        username = input("Enter a username: ")
        if username in users:
            print("Username already exists. Try another.")
        else:
            break
    
    while True:
        password = input("Enter a password: ")
        confirm_password = input("Confirm your password: ")

        if password != confirm_password:
            print("Passwords do not match. Try again.")
        else:
            break
    
    hashed_password = hash_password(password)
    users[username] = hashed_password
    save_data("users.json", users)
    print("Registration successful!")


def login():
    """Login a user by verifying username and password."""
    users = load_data("users.json")

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username not in users or not verify_password(password, users[username]):
            print("Invalid username or password.")
            return None
        else:
            print("Login successfull!")
            return username
    