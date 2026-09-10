number = int(input("Write a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

age = int(input("Write your age: "))

if age < 9:
    print("You are a child")
elif age < 13:
    print("You are a tweeny")
elif age < 20:
    print("You are a teenager")
else:
    print("You are an adult")

score = int(input("Write the score 0 to 100: "))

if score <= 10:
    print("one star")
elif 11 <= score <= 20:
    print("two star")
elif 21 <= score <= 30:
    print("three star")
elif 31 <= score <= 40:
    print("four star")
elif 41 <= score <= 50:
    print("five star")
elif 51 <= score <= 60:
    print("six star")
elif 61 <= score <= 70:
    print("seven star")
elif 71 <= score <= 80:
    print("eight star")
elif 81 <= score <= 90:
    print("nine star")
elif 91 <= score <= 100:
    print("ten star")
else:
    print("your score is to low or to high")

username = input("Username: ")
password = input("Password: ")

saved_username = "user"
saved_password = "password"

if username == saved_username and password == saved_password:
    print("You are logged in")
else:
    print("That was not the right password")

print(5 == 2) # False
print(5 >= 3) # True
print("string" == "String") # False 
print("string" == "string") # True
print(5 != 4) # True