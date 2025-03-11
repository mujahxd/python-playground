from models import Product
from models import SessionLocal
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

class ProductController:
    def __init__(self):
        """Initialize a session when the controller is created."""
        self.session = SessionLocal()

    def add_product(self, name, price, stock):
        """Add a new product to the database with validation and error handling"""
        if not name.strip():
            return False, "Product name cannot be empty."
        
        if price <= 0 or stock < 0:
            return False, "Price must be greate than zero and stock cannot be negative."
        
        name = name.strip().lower()  # 🔹 Simpan dalam lowercase
        new_product = Product(name=name, price=price, stock=stock)
        try:
            self.session.add(new_product)
            self.session.commit()
            return True, new_product
        except IntegrityError:  # 🔹 Tangkap error jika nama produk sudah ada
            self.session.rollback()
            return False, f"Product with name '{name}' already exists!"
        except SQLAlchemyError as e:
            self.session.rollback()
            return False, str(e)
        # finally:
        #     self.session.close()

    def get_all_products(self):
        """Retrieve all products from the database safely."""
        return self.session.query(Product).all()
        # finally:
        #     self.session.close()

    def update_stock(self, product_id, new_stock):
        """Update stock of a product."""
        if new_stock < 0:
            return False, "Stock cannot be negative."

        try:
            product = self.session.query(Product).filter_by(id=product_id).first()
            if not product:
                return False, f"Product with ID {product_id} not found."

            product.stock = new_stock
            self.session.commit()
            return True, product
        except SQLAlchemyError as e:
            self.session.rollback()
            return False, str(e)