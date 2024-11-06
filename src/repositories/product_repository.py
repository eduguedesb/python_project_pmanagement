# src/repositories/product_repository.py
from src.entities.product import Product

class ProductRepository:
    def __init__(self):
        self._products = {}

    def add_product(self, product: Product):
        self._products[product.id] = product

    def get_product(self, product_id: int) -> Product:
        return self._products.get(product_id)

    def update_product(self, product: Product):
        if product.id in self._products:
            self._products[product.id] = product
        else:
            raise ValueError("Product not found")
