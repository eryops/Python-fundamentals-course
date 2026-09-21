products = [
    {"name": "Laptop", "price": 8999, "category": "Electronics"},
    {"name": "Headphones", "price": 1299, "category": "Electronics"},
    {"name": "Coffee Mug", "price": 149, "category": "Kitchen"},
    {"name": "Gaming Mouse", "price": 799, "category": "Gaming"},
    {"name": "Notebook", "price": 39, "category": "Office"},
    {"name": "Backpack", "price": 499, "category": "Accessories"},
    {"name": "Keyboard", "price": 999, "category": "Gaming"},
    {"name": "Water Bottle", "price": 199, "category": "Sports"},
]

customers = [
    {"name": "Anna Andersson", "email": "anna@example.com", "id": "C001"},
    {"name": "Jonas Jonasson", "email": "jonas@example.com", "id": "C002"},
    {"name": "Maria Berg", "email": "maria@example.com", "id": "C003"},
    {"name": "Peter Nilsson", "email": "peter@example.com", "id": "C004"},
    {"name": "Sara Lind", "email": "sara@example.com", "id": "C005"},
]

def create_order(order_id, customer, *products, **options):
    return{
        'order_id': order_id,
        'customer': customer,
        'products': list(products),
        'options': options
    }


order1 = create_order(22, customers[1], 'Headphones', 'Backpack', shipping_method = 'pick up', shipping = None)
order2 = create_order(23, customers[0], 'Notebook', 'Keyboard', shipping_method = 'pick up')
order3 = create_order(24, customers[1], 'Notebook', 'Backpack', 'Water Bottle', shipping_method = 'post', campaign_code = 'free-delivery')
order4 = create_order(25, customers[1], 'Keyboard', 'Notebook', 'Backpack', shipping_method = 'post', priority = 'next_day')
order5 = create_order(26, customers[1], 'Notebook', 'Backpack', shipping_method = 'pick up')


def calculate_subtotal(*prices): 
    return sum(prices) if prices else 0

def order_configuration(**options):
    return { key: value for key, value in options.items() if value is not None }

def order_summary(order_id, customer, *messages, **metadata):
    summery = f'Order Summary for {customer['name']} order {order_id}\nEmail: {customer['email']}\n'
    if messages:
        summery += 'Messages:\n'
        for message in messages:
            summery += f'{message}\n'
    if metadata:
        summery += 'Metadata\n'
        for key, value in metadata.items():
            summery += f'{key}: {value}\n'

    return summery
print(order_summary(22, customers[0], "snyggt kör", 'bra pris', shipping = 33, discount = 5))