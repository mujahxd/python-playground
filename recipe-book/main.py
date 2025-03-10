# main.py (Entry Point)
# This is the main file to run the application

from auth import register, login
from recipes import add_recipe, delete_recipe, delete_all_recipes, view_guest_recipes, view_user_recipes

def main():
    user = None

    while True:
        print("Welcome to the Recipe Book!")
        print("1. Login")
        print("2. Register")
        print("3. Continue as Guest")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1":
            user = login()
        elif choice == "2":
            register()
            continue
        elif choice == "3":
            user = "guest"
        elif choice == "4":
            print("Thank you for using the Recipe Book. See you next time!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")
            continue

        if user:
            recipe_menu(user)

def recipe_menu(user):
    while True:
        print("Recipe Management")
        print("1. View Recipes")
        if user != "guest":
            print("2. Add Recipe")
            print("3. Delete Recipe")
            print("4. Delete All My Recipes")
        print("5. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_guest_recipes() if user == "guest" else view_user_recipes(user)
        elif choice == "2" and user != "guest":
            add_recipe(user)
        elif choice == "3" and user != "guest":
            delete_recipe(user)
        elif choice == "4" and user != "guest":
            delete_all_recipes(user)
        elif choice == "5":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()