for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

swedish_vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö'}
sentence = "A long sentence to test against and the letter Å"
count = 0

for letter in sentence: 
    if letter.lower() in swedish_vowels:
        count += 1

print(count)

list_with_numbers = [4, 7, 2, 7, 9, 4, 3, 8, 2, 10, 3, 3, 11, 7]
duplicates = set()
seen = set()

for number in list_with_numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print(duplicates)

numbers = [3, 5, 2]

for number in numbers:
    print('*'*number)
