products = [
    {"name": "  keyboard ", "category": "Tech", "price": 499, "stock": 12},
    {"name": "MOUSE", "category": "tech", "price": 299, "stock": 34},
    {"name": " Monitor  ", "category": "TECH", "price": 1999, "stock": 0},
    {"name": "usb cable", "category": "Accessories", "price": 99, "stock": 120},
    {"name": "USB Cable ", "category": "accessories", "price": 79, "stock": 200},
    {"name": "Laptop Stand", "category": "Office", "price": 349, "stock": 18},
    {"name": " LAPTOP stand ", "category": "office", "price": 299, "stock": 22},
    {"name": "Desk Lamp", "category": "Home", "price": 199, "stock": 50},
    {"name": "desk   lamp", "category": "home", "price": 149, "stock": 60},
    {"name": "HeadPhones", "category": "Tech", "price": 899, "stock": 0},
    {"name": "head phones ", "category": "tech", "price": 799, "stock": 20},
    {"name": " Chair ", "category": "Home", "price": 999, "stock": 8}
]

normalize_products = [
    {
        "name": product['name'].strip().title(),
        "category": product['category'].strip().lower(),
        "stock": product['stock'],
        "price": product['price']
    }
    for product in products
]

products_in_stock = [product for product in normalize_products if product['stock'] > 0]

uniq_categories = {product['category'] for product in normalize_products}

products_value = {product['name']: product['price']*product['stock'] for product in normalize_products}

sort_products_by_value = sorted(products_value.items(), key=lambda item: item[1], reverse=True)

for rank, (product_name, inventory_value) in enumerate(sort_products_by_value, 1):
    print(f'{rank}. {product_name}´s inventory value: {inventory_value}')

