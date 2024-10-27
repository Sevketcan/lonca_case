def is_valid_price(price) -> bool:
    return isinstance(price, (int, float)) and price > 0

def validate_product(product: dict) -> bool:
    required_fields = ["stock_code", "name", "price", "quantity"]
    return all(field in product for field in required_fields)
