# main.py (Entry point for the application)
from auth import register, login

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using the To-Do App!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()