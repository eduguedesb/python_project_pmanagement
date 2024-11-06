# tests/unit/test_product_service.py
import unittest
from src.entities.product import Product
from src.repositories.product_repository import ProductRepository
from src.services.product_service import ProductService

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.repo = ProductRepository()
        self.service = ProductService(self.repo)
        self.product = Product(id=1, name="Laptop", price=1500.0, stock=10)
        self.repo.add_product(self.product)

    def test_restock_product(self):
        self.service.restock_product(product_id=1, quantity=5)
        self.assertEqual(self.repo.get_product(1).stock, 15)

    def test_restock_nonexistent_product(self):
        with self.assertRaises(ValueError):
            self.service.restock_product(product_id=2, quantity=5)

if __name__ == '__main__':
    unittest.main()
