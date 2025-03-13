from views import ProductView, UserView
from models import init_db
from controllers import UserController


def main():
    """Main menu for Store Management CLI."""
    init_db()
    user_controller = UserController()

    print("\n===== Welcome to Store Management CLI =====")
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, result = user_controller.login(username, password)

            if success:
                print(f"✅ Login successful! Role: {result}")
                if result == "admin":
                    admin_menu()
                else:
                    user_menu(username)  # 🔹 Akan dibuat nanti
                break
            else:
                print(f"❌ Error: {result}")

        elif choice == "2":
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            confirm_password = input("Confirm password: ")
            role = input("Enter role (admin/user): ").strip().lower()

            success, result = user_controller.register(username, password, confirm_password, role)
            print(f"{'✅' if success else '❌'} {result}")

        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a valid option.")

    

def admin_menu():
    """Admin menu for managing products."""
    view = ProductView()
    
    while True:
        print("\n===== Admin Panel =====")
        print("1. Show Products")
        print("2. Add Product")
        print("3. Update Product Stock")
        print("4. Delete Product")
        print("5. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            view.show_all_products()
        elif choice == "2":
            view.input_new_product()
        elif choice == "3":
            view.update_product_stock()
        elif choice == "4":
            view.delete_product()
        elif choice == "5":
            print("🔐 Logging out...")
            main()
            break
        else:
            print("❌ Invalid choice! Please enter a valid option.")
    

def user_menu(username):
    """User menu interface."""
    view = UserView(username)
    while True:
        print(f"\n===== Welcome, {username}! =====")
        print("1. Buy Product")
        print("2. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            view.buy_product()
        elif choice == "2":
            print("🔐 Logging out...")
            main()
            break
        else:
            print("❌ Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
