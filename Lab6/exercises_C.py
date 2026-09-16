playlist = ['first song', 'ABCDFU', 'Beautiful', 'Little by little']

for index, song in enumerate(playlist, 1):
    print(f"{index}. {song}")

tasks = ['clean', 'sleep', 'cock dinner', 'eat', 'code']
for index, task in enumerate(tasks, 1):
    print(f"{task} {index}")

values = [1, 34, 56, 89, 4, 6, 7, 67]
for index, value in enumerate(values):
    if value > 30:
        print(f"index {index}, value {value}")

# for i in range(len(values)):
#     print(i, values[i])
# I haven´t used this anywhere because I have used enumerate so I made one up
for index, values in enumerate(values):
    print(index, values)
