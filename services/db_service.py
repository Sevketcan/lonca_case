from pymongo import UpdateOne
from configs.config import collection
from utils.date_utils import get_current_utc_timestamp
from utils.validators import validate_product
from utils.error_utils import log_error
import logging

def insert_or_update_product(product):
    if not validate_product(product):
        log_error(f"Incomplete product data: {product}")
        return

    product['updated_at'] = get_current_utc_timestamp()

    try:
        result = collection.update_one(
            {"stock_code": product['stock_code']},
            {"$set": product},
            upsert=True
        )
        if result.upserted_id:
            logging.info(f"Inserted product {product['stock_code']}")
        else:
            logging.info(f"Updated product {product['stock_code']}")
    except Exception as e:
        log_error(f"Failed to insert/update product {product['stock_code']}: {e}")

def insert_products(products):
    for product in products:
        insert_or_update_product(product)
