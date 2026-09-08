first_name = input("Enter your first name: ").strip().capitalize()
last_name = input("Enter your last name: ").strip().capitalize()
city = input("Enter your city: ").strip().capitalize()
year_of_birth = int(input("Enter your year of birth: "))
favorite_programming_language = input("Enter your favorite programming language: ").strip()

user_id = first_name[:3].lower() + last_name[:3].lower() + str(year_of_birth)[-2:]

initials = first_name[0] + last_name[0]
full_name_length = len(first_name) + len(last_name)
favorite_language_reverse = favorite_programming_language[::-1]

full_name_upper = first_name.upper() + " " + last_name.upper()
birth_year_last_two_digits = str(year_of_birth)[-2:]
birth_year_century = str(year_of_birth)[:2]



print(f"""
User Information:
First Name: {first_name}
Last Name: {last_name}
City: {city}
Year of Birth: {year_of_birth}
Favorite Programming Language: {favorite_programming_language}
User ID: {user_id}
Initials: {initials}
Full Name Length: {full_name_length}
Favorite Language (Reversed): {favorite_language_reverse}
Full Name (Uppercase): {full_name_upper}
Birth Year (Last Two Digits): {birth_year_last_two_digits}
Birth Year (Century): {birth_year_century}
""")