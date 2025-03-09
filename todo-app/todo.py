# todo.py (Handles To-Do management)
from database import load_data, save_data

def user_menu(username):
    while True:
        data = load_data()
        todos = data[username]["todos"]
        print("\nTo-Do List:")
        if todos:
            for i, todo in enumerate(todos, 1):
                print(f"{i}. {todo}")
        else:
            print("No To-Do items.")
        
        print("="*25)
        print("1. Add To-Do")
        print("2. Delete a To-Do")
        print("3. Delete all To-Do")
        print("4. Logout")
        
        choice = input("Select an option: ")
        if choice == "1":
            add_todo(username)
        elif choice == "2":
            delete_todo(username)
        elif choice == "3":
            delete_all_todos(username)
        elif choice == "4":
            print("Logout successful.")
            break
        else:
            print("Invalid choice!")

def add_todo(username):
    data = load_data()
    while True:
        print("\nCurrent To-Do List:")
        for i, todo in enumerate(data[username]["todos"], 1):
            print(f"{i}. {todo}")
        todo = input("Enter a To-Do (0 to cancel): ")
        if todo == "0":
            break
        data[username]["todos"].append(todo)
        save_data(data)
        print("To-Do added successfully!")

def delete_todo(username):
    data = load_data()
    while True:
        print("\nTo-Do List:")
        todos = data[username]["todos"]
        if not todos:
            print("No To-Do items.")
            return
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
        
        choice = input("Enter the number of the To-Do to delete (0 to cancel): ")
        if choice == "0":
            break
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(todos):
                removed_todo = todos.pop(index)
                save_data(data)
                print(f"To-Do '{removed_todo}' delete successfully!")
            else:
                print("Invalid number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_all_todos(username):
    data = load_data()
    data[username]["todos"] = []
    save_data(data)
    print("All To-Dos deleted successfully!")