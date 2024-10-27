from datetime import datetime, timezone

class Product:
    def __init__(self, stock_code, color, discounted_price, images, is_discounted, name, price, price_unit,
                 product_type, quantity, sample_size, series, status, fabric, model_measurements,
                 product_measurements, created_at=None, updated_at=None):
        self.stock_code = stock_code
        self.color = color
        self.discounted_price = discounted_price
        self.images = images
        self.is_discounted = is_discounted
        self.name = name
        self.price = price
        self.price_unit = price_unit
        self.product_type = product_type
        self.quantity = quantity
        self.sample_size = sample_size
        self.series = series
        self.status = status
        self.fabric = fabric
        self.model_measurements = model_measurements
        self.product_measurements = product_measurements
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)

    def to_dict(self):
        return self.__dict__
