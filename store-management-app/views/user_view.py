from controllers import ProductController

class UserView:
    def __init__(self, username):
        """Initialize UserView with a username."""
        self.username = username
        self.controller = ProductController()

    def show_products(self):
        """Display all available products."""
        products = self.controller.get_all_products()

        if not products:
            print("\n⚠ No products found.")
            return []

        print(f"\n📦 Available Products for {self.username}:")
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product.name} - Rp{product.price} (Stock: {product.stock})")
        
        return products
    
    def buy_product(self):
        """Allow user to buy products until they type 'done'"""
        products = self.show_products()
        if not products:
            return
        
        cart = []
        total_price = 0

        while True:
            choice = input("\nEnter product number (or 'done' to finish): ").strip().lower()
            if choice == 'done':
                break

            try:
                product_index = int(choice) - 1
                if product_index < 0 or product_index >= len(products):
                    print("❌ Invalid product number. Please try again.")
                    continue
                    
                product = products[product_index]
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("❌ Quantity must be at least 1.")
                    continue

                if quantity > product.stock:
                    print(f"❌ Not enough stock available. Current stock: {product.stock}")
                    continue

                # Update stock in database
                success, _ = self.controller.update_stock(product.id, product.stock - quantity)
                if success:
                    cart.append((product.name, quantity, product.price * quantity))
                    total_price += product.price * quantity
                    print(f"✅ {quantity}x {product.name} added to cart!")
                else:
                    print("❌ Error updating stock. Please try again.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        
        if not cart:
            print("\n🛒 No items purchased.")
            return
    
        # Display Invoice
        print("\n🧾 Invoice")
        print("-" * 30)
        for item in cart:
            print(f"{item[0]}  x{item[1]}  = Rp{item[2]}")
        print("-" * 30)
        print(f"Total:       Rp{total_price}")