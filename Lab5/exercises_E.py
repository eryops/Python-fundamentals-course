def log_event(event_type, *messages, **metadata):
    return {'event_type': event_type, 'messages': list(messages), **metadata}

def calculate_order(customer, *prices, **options):
    total = sum(prices)
    discount = options.get('discount', 0)
    shipping = options.get('shipping', 0)

    if discount:
        total -= total * (discount/100)

    if shipping:
        total += shipping

    return {
        'customer': customer,
        'prices': list(prices),
        'discount': discount,
        'shipping': shipping,
        'total': total
    }

def user_profile_param(name, age, city):
    return {'name': name, 'age': age, 'city':city}
def user_profile_kwargs(**user):
     return {**user}
# It is always clearer to use explicit parameters when you know what data you are getting and what data you want. If there can be data that
# are not known **kwargs or *args are useful to fill out unknown data. Explicit parameters tells you more about what the functions want and dose espessely if the 
# parameters are clearly named

# --- Main like section ---
print(log_event('error', 'file not found', 'type error', code= 404, path= '/user/home/file_name.py'))

print(calculate_order('Adam', 12, 34, 45, discount = 12))
print(calculate_order('Adam', 112, 334, 450, discount = 22, shipping = 34))

print(user_profile_kwargs(name="Johanna"))
print(user_profile_kwargs(name="Anna", age=29))
print(user_profile_kwargs(name="Markus", age=41, city="Göteborg", hobby="climbing"))