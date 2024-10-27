import logging

class DatabaseConnectionError(Exception):
    pass

def log_error(error_message: str):
    logging.error(f"Error: {error_message}")
