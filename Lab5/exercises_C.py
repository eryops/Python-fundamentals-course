def separator():
    print('-------------------')

def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet('Ali'))
print(greet('Stina', 'Nice to se you'))
separator()

def calculate_price(price, quantity=1, discount=0):
    total = price * quantity
    discount_amount  = total * (discount/100)
    final_price = total - discount_amount 

    return final_price

print(calculate_price(124, 3, 23))
print(calculate_price(345, 3))
print(calculate_price(99))
separator()

def create_profile(name, city='Unknown', active=True):
    return {'name': name, 'city': city, 'active': active}

print(create_profile('Adam'))
print(create_profile('Jonas', 'Märsta'))
print(create_profile('Johannes', 'Årsta', False))
separator()

print(create_profile(active=False, name="Berit"))
separator()

#create_profile(name="Uppsala", city, active=True)