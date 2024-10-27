from pymongo import MongoClient
from dotenv import load_dotenv
from utils.error_utils import DatabaseConnectionError, log_error
import os

load_dotenv()  # Load environment variables from .env file

try:
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise DatabaseConnectionError("MONGO_URI not set in environment variables.")
    client = MongoClient(mongo_uri)

    db = client['product_db']
    collection = db['products']
except Exception as e:
    log_error(f"Database connection error: {e}")
    raise
