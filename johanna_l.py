# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.
# Write your solution below:

for product in products:
    print(f"product name: {product['name']}, price {product['price']}, number of items in stock: {product['stock']}")

products_name_in_stock = [product['name'] for product in products if product['stock'] ]
print(products_name_in_stock)
 
total_value = 0
for product in products: 
    if product['stock']:
        total_value += product['stock'] * product['price']
print(total_value)

products_in_stock = [product for product in products if product['stock'] ]
product_with_highest_price = None
for product in products_in_stock:
    if product_with_highest_price is None or product['price'] > product_with_highest_price['price']:
        product_with_highest_price = product
print(product_with_highest_price['name'])



# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.

# Write your solution below:

def calculate_average(scores):
    return sum(scores)/len(scores)

def create_result(scores):
    average = calculate_average(scores)
    if average >= 70:
        return 'PASS'
    return 'FAIL'
print(calculate_average(scores))
print(create_result(scores))


# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.

# Write your solution below:

def calculate_order(customer_name, *product_prices, **settings):
    sub_total = sum(product_prices)
    final_total = sub_total

    discount = settings.get('discount')
    shipping = settings.get('shipping')

    if discount:
        final_total -= sub_total * (discount/100)
    if shipping:
        final_total += shipping

    return { 'customer': customer_name, 'subtotal': sub_total, 'final_total': final_total, 'settings': settings}

print(calculate_order('Anna', *product_prices, **order_settings))


# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

normalized_names_list = [player['name'].strip().title() for player in players]
active_players_with_min_80 = [player['name'].strip().title() for player in players if player['active'] and player['score'] >= 80]
order_players_by_score = sorted(players, key=lambda player: player['score'], reverse=True)

for ranking, player in enumerate(order_players_by_score, 1):
    player_name = player['name'].strip().title()
    print(f"{ranking}. {player_name}")

player_scores = [player['score'] for player in players]

zipped_name_and_score_list = list(zip(normalized_names_list, player_scores)) # using the list I already have created for names
