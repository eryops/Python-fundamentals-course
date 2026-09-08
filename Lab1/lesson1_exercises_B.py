name = input("Enter your name: ")
year_of_birth = input("Enter your year of birth: ")

print(f"Hello {name}, you are about {2026 - int(year_of_birth)} years old.")

item_price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

total_price = item_price * (1 - discount_percentage / 100)
print(f"Price after discount: {total_price:.2f}")

temperature_celsius = float(input("Enter the temperature in Celsius: "))
temperature_fahrenheit = (temperature_celsius * 9/5) + 32

print(temperature_fahrenheit)

room_width = float(input("Enter the width of the room in meters: "))
room_length = float(input("Enter the length of the room in meters: "))

room_area = room_width * room_length
room_perimeter = 2 * (room_width + room_length)
print(f"The area of the room is: {room_area} square meters")
print(f"The perimeter of the room is: {room_perimeter} meters")

# I have used a float data type to ensure that we get the right data from the user. If the user uses a string instead (as an example) the program will throw an error