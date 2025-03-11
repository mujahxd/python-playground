from controllers import ProductController


class ProductView:
    def __init__(self):
        """Initialize the ProductView with a ProductController instance."""
        self.controller = ProductController()

    def show_all_products(self):
        """Display all products in the database."""
        products = self.controller.get_all_products()

        if not products:
            print("\n⚠ No products found.")
            return
        
        print("\n📦 Product List:")
        for product in products:
            print(f"{product.id}. {product.name} - Rp{product.price} (Stock: {product.stock})")
        
    def input_new_product(self):
        """CLI function to add a new product."""

        try:
            name = input("Enter product name: ").strip()
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            success, result = self.controller.add_product(name, price, stock)
            if success:
                print(f"✅ Success: Product '{result.name}' added successfully!")
            else:
                print(f"❌ Error: {result}")

        except ValueError:
            print("❌ Input Error: Price must be a number and stock must be an integer.")
    
    def update_product_stock(self):
        """Update stock of an existing product."""
        self.show_all_products()

        try:
            product_id = int(input("\nEnter product ID to update stock: "))
            new_stock = int(input("Enter new stock quantity: "))

            success, result = self.controller.update_stock(product_id, new_stock)

            if success:
                print(f"✅ Success: Stock for '{result.name}' updated to {result.stock}!")
            else:
                print(f"❌ Error: {result}")

        except ValueError:
            print("❌ Input Error: Product ID and stock must be numbers.")

        

