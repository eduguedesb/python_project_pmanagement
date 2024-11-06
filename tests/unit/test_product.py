# tests/unit/test_product.py
import unittest
from src.entities.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(id=1, name="Laptop", price=1500.0, stock=10)

    def test_update_stock_increase(self):
        self.product.update_stock(5)
        self.assertEqual(self.product.stock, 15)

    def test_update_stock_decrease(self):
        self.product.update_stock(-5)
        self.assertEqual(self.product.stock, 5)

    def test_update_stock_insufficient(self):
        with self.assertRaises(ValueError):
            self.product.update_stock(-15)

if __name__ == '__main__':
    unittest.main()
