def celsius_to_fahrenheit(temperature_celsius):
    return temperature_celsius*1.8 + 32

def temperature_classification(temperature_celsius):
    if temperature_celsius < 5:
        return 'COLD'
    if temperature_celsius < 24:
        return 'WARM'
    return 'HOT'

def temperature_formatting(temperature_celsius):
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
    classification = temperature_classification(temperature_celsius)

    return f"Today it is {classification} outside, the temperature is {temperature_celsius}°C ({temperature_fahrenheit}°F)"

def subtotal(price, quantity):
    return price * quantity

def total_discount(subtotal, discount_percentage):
    return subtotal * (discount_percentage/100)

def final_total(price, quantity = 1, discount_percentage = 0):
    total = subtotal(price, quantity)
    discount =  total_discount(total, discount_percentage)

    return total - discount

# this is pretty much the exercise in part C 2 in three functions 

# --- Main like section ---

print('Temperature reporting:')
print(temperature_formatting(22))
print(temperature_formatting(-8))
print(temperature_formatting(25))

print('\nTotal price calculator')
print(final_total(35, 5, 23))
print(final_total(100, 2, 93))
print(final_total(8790))
print(final_total(67, 6, 7))