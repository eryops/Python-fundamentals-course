RGB = (255, 4, 0) #tuple unpacking

red, green, blue = RGB

print("Red:", red)
print("Green:", green)  
print("Blue:", blue)

person = ("Johanna", 45, "Åkersberga")
name, age, city = person

print(f"{name} is {age} years old and lives in {city}.")

#tuples are immutable, and can´t be changed after they been created. This is good for data that have to be protected and should not be changed.

coordinates = [(4, 5), (6, 7), (8, 9), (10, 11)]

print("first x:", coordinates[0][0])
print("first y:", coordinates[0][1])
