import unittest
from pymongo import MongoClient
from configs.config import db, collection
from services.db_service import insert_or_update_product, insert_products

class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = MongoClient("mongodb://localhost:27017/")
        cls.db = cls.client['test_product_db']
        cls.collection = cls.db['test_products']

    def setUp(self):
        self.collection.delete_many({})  
        
    def test_insert_or_update_product(self):
        product = {
            "stock_code": "1234-bej",
            "name": "Test Elbise",
            "price": 10.00,
        }
        insert_or_update_product(product)
        self.assertEqual(self.collection.count_documents({}), 1)
        
        product["price"] = 15.00
        insert_or_update_product(product)
        updated_product = self.collection.find_one({"stock_code": "1234-bej"})
        self.assertEqual(updated_product['price'], 15.00)

    @classmethod
    def tearDownClass(cls):
        cls.client.drop_database('test_product_db')

if __name__ == '__main__':
    unittest.main()
