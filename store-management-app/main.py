from views import ProductView
from models.base import init_db

def main():
    """Main menu for Store Management CLI."""
    init_db()
    view = ProductView()

    while True:
            print("\n===== Store Management CLI =====")
            print("1. Show Products")
            print("2. Add Product")
            print("3. Update Product Stock")  # ✅ Tambah menu baru
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                view.show_all_products()
            elif choice == "2":
                view.input_new_product()
            elif choice == "3":
                view.update_product_stock()  # ✅ Panggil fungsi update stock
            elif choice == "4":
                print("👋 Exiting program. Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()