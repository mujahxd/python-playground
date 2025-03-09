# auth.py (Handles user authentication)
from database import load_data, save_data
from todo import user_menu
import getpass

def register():
    data = load_data()
    while True:
        username = input("Enter username: ")
        if username in data:
            print("Username already exists, please choose another.")
            continue
        password = getpass.getpass("Enter password: ")
        data[username] = {"password": password, "todos": []}
        save_data(data)
        print("Registration successful!")
        return

def login():
    data = load_data()
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    if username in data and data[username]["password"] == password:
        print(f"\nWelcome, {username}!")
        user_menu(username)
    else:
        print("Incorrect username or password!")