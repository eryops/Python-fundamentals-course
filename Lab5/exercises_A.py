def greet():
    return 'Hello'

def show_course_name():
    return 'Python fundamentals'

def print_separator():
    print('-------------------')


print(greet())
print(show_course_name())
print_separator()
print(greet())
print(show_course_name())
print_separator()
print(greet())
print(show_course_name())
print_separator()
print(greet())
print(show_course_name())
print_separator()

def greet_person(name):
    return f"Hello {name}!"

def introduce(name, city):
    # parameters name and city
    return f"This is {name} and they are from {city}"

print(greet_person('Johanna'))
print(introduce('Johanna', 'Åkersberga')) # arguments are sent in to the function (Johanna, Åkersberga)
print_separator()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(add(10, 56))
print(subtract(10, 56))
print(multiply(10, 56))
print(divide(10, 56))
print_separator()

def calculate_area(area_width, area_height):
    return area_width * area_height

def cost_per_square_meter(total_cost):
    return total_cost / calculate_area(120, 30)

print(cost_per_square_meter(2500000))