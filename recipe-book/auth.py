# auth.py (Authentication Management)
from storage import load_data, save_data
from utils import hash_password, verify_password
import getpass

def register():
    """Register a new user with username and password."""
    users = load_data("users.json")


    while True:
        username = input("Enter a username: ")
        if username in users:
            print("Username already exists. Try another.\n")
        else:
            break
    
    while True:
        password = getpass.getpass("Enter a password: ")
        confirm_password = getpass.getpass("Confirm your password: ")

        if password != confirm_password:
            print("Passwords do not match. Try again.\n")
        else:
            break
    
    hashed_password = hash_password(password)
    users[username] = hashed_password
    save_data("users.json", users)
    print("Registration successful!\n")


def login():
    """Login a user by verifying username and password."""
    users = load_data("users.json")

    while True:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        if username not in users or not verify_password(password, users[username]):
            print("Invalid username or password.\n")
            return None
        else:
            print("Login successfull!\n")
            return username
    