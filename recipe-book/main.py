# main.py (Entry Point)
# This is the main file to run the application

def main():
    while True:
        print("Welcome to the Recipe Book!")
        print("1. Login")
        print("2. Register")
        print("3. Continue as Guest")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1":
            # Call the login function from auth.py
            pass
        elif choice == "2":
            # Call the register function from auth.py
            pass
        elif choice == "3":
            # Enter as guest
            pass
        elif choice == "4":
            print("Thank you for using the Recipe Book. See you next time!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()