names = ['Johanna', 'Greta', 'Adam', 'Ali']

for index, name in enumerate(names):
    print(index, name)

for number in range(1, 51): 
    if number % 2 == 0:
        print(number)

numbers = [1, 4, 9, 6]

sum_of_numbers = 0;

for number in numbers:
    sum_of_numbers += number
print(sum_of_numbers)

largest_number = 0;

for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)


list_of_strings = ['words', 'spinning', 'flying', 'running', 'sit', 'cat']

count = 0

for word in list_of_strings:
    if len(word) > 5:
        count += 1

print(count)

scores = [55, 72, 88, 69, 90, 40, 73, 100]

passes = 0
fails = 0

for score in scores:
    if score >= 70:
        passes += 1
    else:
        fails += 1
        
print(f"fails {fails}")
print(f"passes {passes}")

person = {
    "name": "Johanna",
    "age": 34,
    "city": "Stockholm"
}

for key in person.keys():
    print("key", key) 

for value in person.values():
    print("value", value)

for item in person.items():
    print('item', item)