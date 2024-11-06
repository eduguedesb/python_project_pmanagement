# src/main.py
from src.entities.product import Product
from src.repositories.product_repository import ProductRepository
from src.services.product_service import ProductService

if __name__ == "__main__":
    repo = ProductRepository()
    service = ProductService(repo)
    
    product = Product(id=1, name="Laptop", price=1500.00, stock=10)
    repo.add_product(product)
    
    print(f"Initial Stock: {product.stock}")
    service.restock_product(product_id=1, quantity=5)
    print(f"Updated Stock: {product.stock}")
