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

def order_processing(customer, *products, **metadata):
    prices = [product['price'] for product in products]
    subtotal = calculate_subtotal(*prices)
    final_cost = subtotal

    discount = metadata.get('discount', 0)
    shipping_fee = metadata.get('shipping', 0)

    if metadata.get('priority') == 'express':
        shipping_fee += 45

    if discount: 
        final_cost -= subtotal * (discount / 100)
    final_cost += shipping_fee

    return {
        'customer': customer,
        'products': products,
        'subtotal': subtotal,
        'discount': discount,
        'shipping_cost': shipping_fee,
        'final_total': final_cost,
        'options': metadata
    }

order_1 = order_processing(customers[1], products[0], discount = 22)
order_2 = order_processing(customers[0], products[7], products[5], shipping = 43)
order_3 = order_processing(customers[2], products[3], products[4], products[6], shipping = 99, discount = 10)
order_4 = order_processing(customers[3], products[5], products[0], products[4], shipping = 65, priority = 'express')
order_5 = order_processing(customers[4], products[3], products[4], shipping = 44)

all_orders = [order_1, order_2, order_3, order_4, order_5]

# print(order_processing(customers[2], products[0], products[5], products[3], priority = 'express', shipping = 44, discount = None))

def create_report(title, *sections, **metadata):
    return {
        'title': title,
        'sections': sections,
        'metadata': metadata
    }

def report_to_string(report):
    text = f'REPORT: {report['title']}\n'
    for section in report['sections']:
        text += f'{section}\n'

    if report['metadata']:
        text += 'Metadata:\n'
        for key, value in report['metadata'].items():
            text += f'{key}: {value}\n'

    return text
num_orders = len(all_orders)
total_revenue = sum(order['final_total'] for order in all_orders)
average_value = total_revenue / num_orders
largest_order = max(all_orders, key=lambda order: order['final_total'])
smallest_order = min(all_orders, key=lambda order: order['final_total'])

report = create_report(
    'Daily Order Report', 
    f'Number of orders: {num_orders}', 
    f"Total revenue: {total_revenue}",
    f"Average order value: {average_value:.2f}",
    f"Largest order: {largest_order['final_total']}",
    f"Smallest order: {smallest_order['final_total']}",
    generated_by ='Bot Bottson',
    version = '0.1.2-v',
)
print(report_to_string(report))