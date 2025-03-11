from sqlalchemy import Column, Integer, String, Float
from models import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock})>"