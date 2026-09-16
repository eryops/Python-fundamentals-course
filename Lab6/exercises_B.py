square_dictionary = {number: number ** 2 for number in range(1, 21)}
print(square_dictionary)

list_of_words = ['Ord', 'Skog', 'El', 'Julgran']
word_length = {len(word): word for word in list_of_words}
print(word_length)

names = ['Erik', 'ERIK', 'Ali', 'GUSS', 'GUSS']
normalized_name_set = {name.strip().lower() for name in names}
print(normalized_name_set)

products = [
    {"name": "Keyboard", "price": 499},
    {"name": "Mouse", "price": 299},
    {"name": "Monitor", "price": 1999},
    {"name": "USB Cable", "price": 99},
]
expensive_products = [product for product in products if product['price'] >= 400]
cheap_products = [product for product in products if product['price'] < 400]
print(expensive_products)
print(cheap_products)

students = [
    {'name': 'Astrid', 'score': 45},
    {'name': 'Stig', 'score': 99},
    {'name': 'Ali', 'score': 77},
    {'name': 'Lisa', 'score': 67},
    {'name': 'Linda', 'score': 65}
]
student_score_status = {student['name']: 'PASS' if student['score'] >= 70 else 'FAIL' for student in students}
print(student_score_status)