list_of_words = ['Ord', 'Skog', 'El', 'Julgran']
sort_words = sorted(list_of_words, key=lambda word: len(word))
print(sort_words)

students = [
    {'name': 'Astrid', 'score': 45},
    {'name': 'Stig', 'score': 99},
    {'name': 'Ali', 'score': 77},
    {'name': 'Lisa', 'score': 67},
    {'name': 'Linda', 'score': 65}
]
sort_by_score_ascending  = sorted(students, key=lambda student: student['score'] )
print(sort_by_score_ascending)
sort_by_score_descending  = sorted(students, key=lambda student: student['score'], reverse=True)
print(sort_by_score_descending)

products = [
    {"name": "Keyboard", "price": 499},
    {"name": "Mouse", "price": 299},
    {"name": "Monitor", "price": 1999},
    {"name": "USB Cable", "price": 99},
]
products_order_by_price = sorted(products, key=lambda product: product['price'], reverse=True)
print(products_order_by_price)

names = [
    {'first_name': 'Bengt', 'last_name': 'Svensson'},
    {'first_name': 'Alexandra', 'last_name': 'Axelsson'},
    {'first_name': 'Lisa', 'last_name': 'Svensson'},
    {'first_name': 'Ali', 'last_name': 'Alexander'},
    {'first_name': 'Stina', 'last_name': 'Whalström'}
]
name_by_last_name = sorted(names, key=lambda name: name['last_name'])
print(name_by_last_name)

# Same but in an normal function
def get_lastname(person):
    return person['last_name']
sorted_people = sorted(names, key=get_lastname)
print(sorted_people)

# using normal functions makes sense when it is longer functions or if you want to reuse the function more then once