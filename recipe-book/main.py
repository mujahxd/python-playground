# main.py (Entry Point)
# This is the main file to run the application

from auth import register, login
from recipes import add_recipe, delete_recipe, delete_all_recipes, view_recipes

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
        elif choice == "3":
            user = "guest"
        elif choice == "4":
            print("Thank you for using the Recipe Book. See you next time!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

def recipe_menu(user):
    while True:
        print("\nRecipe Management")
        print("1. View Recipes")
        if user != "guest":
            print("2. Add Recipe")
            print("3. Delete Recipe")
            print("4. Delete All My Recipes")
        print("5. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_recipes()
        elif choice == "2" and user != "guest":
            add_recipe(user)
        elif choice == "3" and user != "guest":
            delete_recipe(user)
        elif choice == "4" and user != "guest":
            delete_all_recipes(user)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()