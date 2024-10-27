from services.xml_parser import parse_xml
from services.db_service import insert_products
from utils.logging_utils import setup_logging

logger = setup_logging()  # Loglama başlatılır

def run_scraper():
    logger.info("Starting XML parsing and database update.")
    products = parse_xml('products.xml')  # XML dosyasından ürün verilerini oku
    insert_products(products)             # Veritabanına ürünleri ekle/güncelle
    logger.info("Database update completed.")

if __name__ == "__main__":
    run_scraper()  # İşlemi çalıştır ve ardından programı kapat
