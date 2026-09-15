def unpacking(a, b, c):
    return a + b + c

def show_person(first_name, last_name, city):
    return f"{first_name} {last_name} lives in {city}"

# --- Main like section ---
numbers_list = [4, 5, 6]
print(unpacking(*numbers_list))

person_tuple = ('Olof', 'Gustavsson', 'Berga')
print(show_person(*person_tuple))



values = [10, 20, 30]
first, *middle, last = values
print(first, middle, last)

values = [1, 2, 3, 4]
first, *middle, last = values
print(first, middle, last)

values = ["A", "B"]
first, *middle, last = values
print(first, middle, last)

values = [5, 6, 7, 8, 9, 10]
first, *middle, last = values
print(first, middle, last)