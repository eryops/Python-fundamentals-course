def separator():
    print('-------------------')

def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(calculate_total([1,2,3,4]))
separator()

def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count

print(count_even([1,2,3,4]))
separator()

def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)
    return long_words

print(get_long_words(["groda", "frog", "cykel"], 5))
separator()

students = [
    {"name": "Anna", "age": 21, "city": "Stockholm", "score": 99, 'is_active': True},
    {"name": "Björn", "age": 23, "city": "Göteborg", "score": 67, 'is_active': True},
    {"name": "Cecilia", "age": 20, "city": "Uppsala", "score": 24, 'is_active': False},
    {"name": "David", "age": 22, "city": "Malmö", "score": 69, 'is_active': True},
]

def find_student(students, name):
    for student in students:
       if student['name'] == name:
           return student

    return None
        

    
print(find_student(students, 'Anna'))
print(find_student(students, 'Berit'))
separator()

def average_score(students):
    total_score = 0;
    for student in students:
        total_score += student['score']

    return total_score/len(students)

print(average_score(students))
separator()

def get_active_users(users):
    active_users = []

    for user in users:
        if user['is_active'] == True:
            active_users.append(user)

    return active_users

print(get_active_users(students))
separator()