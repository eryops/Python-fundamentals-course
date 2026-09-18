nested_list = [
    [1, 2, 3],
    ['one', 'two', 'three'],
    ['apple']
]
flat_list = [list_item for sublist in nested_list for list_item in sublist]

multiplication_table = [
    [row * col for col in range(1, 11)] 
    for row in range(1, 11)
]
# I don´t think it is readable enough, everything prints out on the same row
students = [
    {"name": "  Astrid  ", "score": 45},
    {"name": "stig", "score": 99},
    {"name": "ALI", "score": 77},
    {"name": "lisa ", "score": 67},
    {"name": "Linda", "score": 65},
    {"name": "  marcus", "score": 82},
    {"name": "ELLA", "score": 58},
    {"name": "jonas ", "score": 73},
    {"name": "  sofia", "score": 100},
    {"name": "peter", "score": 38},
    {"name": "Mira", "score": 70},
    {"name": "  hakan ", "score": 69}
]

list_name_score = {student['name'].strip().title() : student['score'] for student in students if student['score'] >= 55}
print(list_name_score)

any_perfect = any(student['score'] == 100 for student in students)
all_perfect = all(student['score'] == 100 for student in students)
all_pass = all(student['score'] > 50 for student in students)
any_fail = any(student['score'] < 50 for student in students)

print(f'Any perfect: {any_perfect}')
print(f'All perfect: {all_perfect}')
print(f'All pass: {all_pass}')
print(f'Any fail: {any_fail}')