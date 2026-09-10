for number in range(1,101):
    if number % 7 == 0 and number % 9 == 0:
        print(number)
        break

list_of_strings = ["sträng", "", "ett", "skriv"]

for string in list_of_strings:
    if not string:
        continue
    print("string", string)

input_string = str(input("Write a word: "))
found = False

for string in list_of_strings:
    if string == input_string:
        print("Found")
        found = True
        break

if not found: 
    print("Your word was not found")

list_of_numbers = [10, -3, 5, -1, 20, 999, 30, 40]

for number in list_of_numbers:
    if number < 0:
        continue
    if number == 999:
        print(number)
        break
    print(f"number {number}")