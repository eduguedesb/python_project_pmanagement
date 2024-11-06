# tests/integration/test_product_integration.py
import unittest
from src.entities.product import Product
from src.repositories.product_repository import ProductRepository
from src.services.product_service import ProductService

class TestProductIntegration(unittest.TestCase):
    def setUp(self):
        self.repo = ProductRepository()
        self.service = ProductService(self.repo)

    def test_integration(self):
        product = Product(id=1, name="Laptop", price=1500.0, stock=10)
        self.repo.add_product(product)

        self.service.restock_product(product_id=1, quantity=5)
        retrieved_product = self.repo.get_product(1)
        self.assertEqual(retrieved_product.stock, 15)

if __name__ == '__main__':
    unittest.main()
