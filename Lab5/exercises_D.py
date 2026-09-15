def show_profile(**info):
    return {key: value for key, value in info.items()}

def create_profile(username, **details):
    return {'username': username, **details}

def build_product(name, price, **metadata):
    return{'product_name': name, 'price': price, **metadata}

def user_settings(**settings):
    used_settings = {}
    for key, setting in settings.items():
        if setting is not None:
            used_settings[key] = setting
    return used_settings

def user_info(name, age, city):
    return f"{name} is {age} and lives in {city}."

# --- Main like section ---
print(show_profile(name= 'Johanna', age = 3, city = 'Stockholm'))

print(create_profile('user', name= 'Johanna', age = 3, city = 'Stockholm'))

print(build_product('ice cream', 42, flavor = 'vanilla', sugar = 'allot'))

print(user_settings(active = None, name = 'Love', opened = 'on'))

user = {'name':'Abbe', 'age': 32, 'city': 'Knivsta'}
print(user_info(**user))