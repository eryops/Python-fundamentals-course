def separator():
    print('-------------------')

def is_even(number):
    return number % 2 == 0

print(is_even(2))
print(is_even(1))
separator()

def get_larger(a,b): 
    if a > b:
        return a
    return b

print(get_larger(8,7))
separator()

def classify_score(score):
    if score > 50:
        return 'PASS'
    return 'FAIL'

print(classify_score(55))
separator()

def full_name(first_name, last_name):
    return f"Name: {first_name} {last_name}"

print(full_name('Jonas', 'Björkman'))
separator()

def calculate_discount(price: int, percentage: int):
    calculated_discount = price * (percentage/100)
    return f"The discount is {calculated_discount:.2f}kr and the new price is {price-calculated_discount:.2f}kr"

print(calculate_discount(100, 20))
separator()

# differences between return and print in a function
def print_function(name):
    print(f"A name: {name}")

print_function('Olof') # prints the name and there are no return value so you can´t use it to anything else then just to print the string

def return_function(name):
    return name

result = return_function("Berit")
print(result)  # Now I can reuse the function to more then just call it and print it
