# empty_string = ""
# string = "en sträng"
# zero_int = 0
# not_zero_int = 10
# empty_list = []
# not_empty_list = ['element']

# if not empty_string:
#     print('empty string')
# if string:
#     print('Not empty string')
# if not zero_int:
#     print('int zero')
# if not_zero_int:
#     print('Int not zero', not_zero_int)
# if not empty_list:
#     print('empty list')
# if not_empty_list:
#     print('List with data', not_empty_list)

# language_list = ['Swedish', 'Germen', 'English', 'Norwegian']

# print('Swedish' in language_list)
# print('swedish' in language_list)

# blocked_users = ['Erik', 'Jonas', 'John']

# username = input("Your username: ")

# if username in blocked_users:
#     print('You are blocked')
# else:
#     print('Welcome')

is_member = False

if not is_member:
    print('You have to be a member')
else:
    print('Welcome')

username = input("Write your username: ")
approved_users = ['Johanna', 'Jonas', 'Ali', 'Greta']

if not username:
    print("You have to write your username")
else:
    print(f"Your user name is {username}")

if username not in approved_users:
    print('You are note an approved user')