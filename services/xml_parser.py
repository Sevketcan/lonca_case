import xml.etree.ElementTree as ET
from models.product import Product
from configs.config import collection
from utils.formatters import capitalize_name, format_currency

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return []

    root = tree.getroot()
    products = []
    
    for item in root.findall('./Product'):
        product = Product(
            stock_code=item.find('StockCode').text,
            color=item.find('Color').text.split(','),
            discounted_price=float(item.find('DiscountedPrice').text),
            images=[img.text for img in item.findall('Images/Image')],
            is_discounted=bool(item.find('IsDiscounted').text == 'True'),
            name=capitalize_name(item.find('Name').text),  # Capitalize name
            price=format_currency(float(item.find('Price').text)),  # Formatted price
            price_unit=item.find('PriceUnit').text,
            product_type=item.find('ProductType').text,
            quantity=int(item.find('Quantity').text),
            sample_size=item.find('SampleSize').text,
            series=item.find('Series').text,
            status=item.find('Status').text,
            fabric=item.find('Fabric').text,
            model_measurements=item.find('ModelMeasurements').text,
            product_measurements=item.find('ProductMeasurements').text,
            created_at=item.find('CreatedAt').text,
            updated_at=item.find('UpdatedAt').text
        )
        products.append(product.to_dict())
    return products

def insert_products_into_db(products):
    for product in products:
        collection.update_one(
            {"stock_code": product['stock_code']},
            {"$set": product},
            upsert=True
        )
