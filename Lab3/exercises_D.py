for number in range(10, 0, -1):
    print(number)

user_number = int(input("Write a number: "))

for number in range(0,10):
    print(f"{user_number} x {number} = {number*user_number}")

play_list = ['song', 'song two', 'song three']

for index, song in enumerate(play_list):
    print(index, song)

for x in range(1,4):
    for y in range(1,5):
        print(f"y: {y} x: {x}")

for row in range(5):
    for col in range(5):
        print("text", end=" ")
    print()