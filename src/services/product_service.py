# src/services/product_service.py
from src.repositories.product_repository import ProductRepository
from src.entities.product import Product

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def restock_product(self, product_id: int, quantity: int):
        product = self.repository.get_product(product_id)
        if not product:
            raise ValueError("Product not found")
        product.update_stock(quantity)
        self.repository.update_product(product)
