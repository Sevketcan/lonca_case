# Product Data Scraper

A Python-based product data scraper that parses product information from an XML file, validates required fields, formats data, and inserts it into a MongoDB database.

## Features

- **XML Parsing**: Reads product data from an XML file and processes it into structured data.
- **Data Validation**: Ensures required fields (`stock_code`, `name`, `price`, `quantity`) are present; logs an error if any field is missing.
- **Data Formatting**: Formats fields such as `price` and `discounted_price` for consistency.
- **Database Interaction**: Inserts or updates product data in MongoDB.
- **Error Handling**: Logs errors and continues with other valid products.

## Project Structure

```plaintext
lonca_case/
├── configs/
│   └── config.py          # MongoDB connection configuration
├── main.py                # Main entry point
├── models/
│   └── product.py         # Product data model
├── services/
│   ├── xml_parser.py      # XML parsing and validation
│   └── db_service.py      # Database operations
├── utils/                 # Utility functions for formatting, validation, and logging
│   ├── formatters.py
│   ├── date_utils.py
│   ├── validators.py
│   ├── logging_utils.py
│   ├── error_utils.py
└── tests/                 # Unit tests
    └── test_db_service.py
