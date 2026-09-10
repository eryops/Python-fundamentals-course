count = 10

while count >= 0:
    print(count)
    count -= 1

correct_password = "password"

password = input("Password: ")

while password != correct_password:
    print("Wrong password!")
    password = input("Enter correct password: ")
print("Yes!!!")

chosen = ""

while chosen != "quit":
    print(f"""
    
    Menu
    1. one
    2. two
    3. three
    quit. to exit
    """)
    chosen = str(input("Make your choice: "))

    if chosen == '1':
        print('one')
    elif chosen == '2':
        print('two')
    elif chosen == '3':
        print('three')
    elif chosen == 'quit':
        print('bye')
    else:
        print('That is not a choice')

number = int(input('Type a number: '))
count = 0

while number != 0:
    print("not the correct number")
    count += number
    number = int(input('Type a new number: '))

print('Yay, you typed the correct number and the amount you created was: ', count)
secret_number = 34

while number != secret_number:
    if number < secret_number:
        number = int(input("You have to choose a higher number: "))
    elif number > secret_number:
        number = int(input("You have to choose a lower number: "))

print("Yes, the number was: ", secret_number)