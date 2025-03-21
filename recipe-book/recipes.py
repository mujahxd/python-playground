# recipes.py (Recipe Management)
from storage import load_data, save_data

def add_recipe(username):
    """Add a new recipe."""
    recipes = load_data("recipes.json")

    if username not in recipes:
        recipes[username] = []

    title = input("Enter recipe title: ")
    ingredients = input("Enter ingridients (comma-separated): ").split(",")
    steps = []

    print("Enter cooking steps (type 'done' to finish)\n")
    while True:
        step = input(f"Step {len(steps)+1}: ")
        if step.lower() == "done":
            break
        steps.append(step)

    recipe = {
        "title": title,
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "steps": steps
    }

    recipes[username].append(recipe)
    save_data("recipes.json", recipes)
    print("Recipe added successfully!\n")

def view_guest_recipes():
    """View all recipes for guest users."""
    recipes = load_data("recipes.json")

    if not recipes:
        print("No recipes available.\n")  
        return

    print("\nAll Recipes:")
    
    for user, user_recipes in recipes.items():
        for recipe in user_recipes:
            print(f"\nRecipe by {user}: {recipe['title']}")
            print("Ingredients:", ", ".join(recipe['ingredients']))
            print("Steps:")
            for step_num, step in enumerate(recipe['steps'], start=1):
                print(f"  {step_num}. {step}")

def view_user_recipes(username):
    """View only the logged-in user's recipes."""
    recipes = load_data("recipes.json")

    if not recipes or username not in recipes or not recipes[username]:
        print("You have no recipes yet.\n")  
        return

    for index, recipe in enumerate(recipes[username], start=1):
        print(f"\nRecipe: {recipe['title']}")
        print("Ingredients:", ", ".join(recipe['ingredients']))
        print("Steps:")
        for step_num, step in enumerate(recipe['steps'], start=1):
            print(f"  {step_num}. {step}")


def delete_recipe(username):
    """Delete a recipe created by the logged-in user."""
    recipes = load_data("recipes.json")

    if username not in recipes or not recipes[username]:
        print("You have no recipes to delete.\n")
        return
    
    for index, recipe in enumerate(recipes[username], start=1):
        print(f"{index}. {recipe['title']}")

    choice = int(input("Enter the number of the recipe to delete: "))
    if 1 <= choice <= len(recipes[username]):
        deleted_recipe = recipes[username].pop(choice - 1)
        save_data("recipes.json", recipes)
        print(f"Recipe '{deleted_recipe['title']}' deleted successfully!\n")
    else:
        print("Invalid selection.")

def delete_all_recipes(username):
    """Delete all recipes created by the logged-in user."""
    recipes = load_data("recipes.json")
    
    if username in recipes:
        del recipes[username]
        save_data("recipes.json", recipes)
        print("All your recipes have been deleted.\n")
    else:
        print("You have no recipes to delete.\n")