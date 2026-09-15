def normalize_name(name):
    return name.strip()

def age_validation(age):
    if 18 <= age <= 99:
        return True
    return False

def registration_fee(age, is_student):
    if age < 25 or is_student:
        return 150
    return 250

def create_participant(name, age, is_student):
    return {
        'name': normalize_name(name),
        'age': age,
        'is_age_valid': age_validation(age),
        'is_student': is_student,
        'fee': registration_fee(age, is_student)
    }

def total_revenue(participants):
    total = 0
    for participant in participants:
        if participant['is_age_valid']:
            total += participant['fee']
    return total

def student_list(participants):
    students = []

    for participant in participants:
        if participant['is_student']:
            students.append(participant)
    return students

def oldest(participants):
    oldest_person = None

    for participant in participants:
        if  oldest_person is None or participant['age'] > oldest_person['age']:
            oldest_person = participant
    return oldest_person

def student_to_text(is_student):
    if is_student:
        return "is a student"
    return "is not a student"

def valid_age_to_text(is_valid_age):
    if is_valid_age:
        return "and is in the valid age range"
    return "and ar not in the valid age range"

def readable_information(participants, name):
    normalized_name = normalize_name(name)

    for participant in participants:
        if participant['name'] == normalized_name:
            return f"""
                {participant['name']} is {participant['age']} years old and {student_to_text(participant['is_student'])}
                 {valid_age_to_text(participant['is_age_valid'])}. 
                 They should pay the fee {participant['fee']}."""
        

# --- Main like section ---
participants = [
    create_participant('  Erik Johansson   ', 66, False),
    create_participant('Ali Wetser  ', 33, True),
    create_participant('Kim Andersson', 17, True),
    create_participant(' Stina Abrahamsson', 24, True),
    create_participant('Lisa Jhonsson', 34, False),
    create_participant('Hélen Nilsson', 67, True),
    create_participant(' Stig Wänner ', 35, True),
    create_participant('Lisa Karlsson', 24, True)
]

total = total_revenue(participants)
list_of_students = student_list(participants)
oldest_person = oldest(participants)


print(f'total revenue {total}')
print(f'\n List of students {list_of_students}')
print(f'\n Oldest person in the list is {oldest_person}')
print(readable_information(participants, 'Lisa Karlsson'))
