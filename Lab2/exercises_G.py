usernames_1 = [
    "johanna_l",
    "mintySyntax",
    "emberEcho",
    "pixelPilot",
    "cloudshift"
]

usernames_2 = [
    "mintySyntax",     
    "cloudshift",      
    "nebulaNoodle",
    "lunarSprout",
    "silverpine"
]

unique_usernames = set(usernames_1) | set(usernames_2)

print(unique_usernames)

duplicated_usernames = set(usernames_1) & set(usernames_2)

print(duplicated_usernames)

course_platform = {
    "courses": [
                {
            "name": "Python Basics",
            "teacher": "Anna",
            "students": ["Johanna", "Kalle", "Sofia"],
            "topics": ["variables", "loops", "functions"]
        },
        {
            "name": "Web Development",
            "teacher": "Johan",
            "students": ["Mia", "Oskar", "Johanna"],
            "topics": ["HTML", "CSS", "JavaScript"]
        },
        {
            "name": "Databases",
            "teacher": "Maria",
            "students": ["Leo", "Sara"],
            "topics": ["SQL", "joins", "indexes"]
        }
    ]
}


inventory = {
    "laptop": 12,
    "mouse": 45,
    "keyboard": 30,
    "monitor": 20,
    "usb_cable": 100
}

inventory["laptop"] = 10  
inventory["mouse"] = 101 
inventory["keyboard"] = 30
inventory["monitor"] = 22
inventory["usb_cable"] = 444

total_units = sum(inventory.values())
print(total_units)

# LIST
# Ordered, mutable, allows duplicates. Best for: collections you frequently update
my_list = ["apple", "banana", "banana"]

# TUPLE
# Ordered, immutable, allows duplicates. Best for: fixed data like coordinates
my_tuple = (12.4, 55.2)

# SET
# Unordered, mutable, no duplicates. Best for: storing unique values
my_set = {"johanna", "kalle", "sofia"}

# DICTIONARY
# Key-value pairs, ordered, keys must be unique. Best for: mapping data
my_dict = {"laptop": 12000, "mouse": 250}
