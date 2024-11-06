# src/entities/product.py
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

    def update_stock(self, quantity: int):
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Insufficient stock")
        self.stock += quantity
