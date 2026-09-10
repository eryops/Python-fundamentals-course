study_sessions = [
    {"subject": "Math", "minutes": 45},
    {"subject": "English", "minutes": 30},
    {"subject": "Biology", "minutes": 60},
    {"subject": "History", "minutes": 40},
    {"subject": "Programming", "minutes": 90},
    {"subject": "Physics", "minutes": 50},
    {"subject": "Chemistry", "minutes": 55},
    {"subject": "Art", "minutes": 25},
    {"subject": "Music", "minutes": 35},
    {"subject": "Geography", "minutes": 20}
]

# total_minutes = 0

# for session in study_sessions:
#     total_minutes += session["minutes"]

# print(total_minutes)

total_minutes_subject = {}

for session in study_sessions:
    subject = session["subject"]
    minutes = session["minutes"]

    if subject not in total_minutes_subject:
        total_minutes_subject[subject] = 0

    total_minutes_subject[subject] += minutes

# print(total_minutes_subject)

# longest_session = None

# for subject in total_minutes_subject:
#     minutes = total_minutes_subject[subject]

#     if not longest_session or minutes > longest_session["minutes"]:
#         longest_session = {"subject": subject, "minutes": minutes}

# print(longest_session)

# for subject in total_minutes_subject:
#     minutes = total_minutes_subject[subject]

#     if minutes > 45:
#         print(subject)

while True:
    print(f"""
    Menu
    1. View all sessions
    2. View total time per subject
    3. Filter by subject
    4. Quit
    """)
    choice = str(input("Choose an option: "))

    if choice == "1":
        print(f"All sessions {total_minutes_subject}")
    elif choice == "2":
        print(f"All sessions {total_minutes_subject}")
    elif choice == "3":
        subject = input("Enter subject: ")
        print(f"\nSessions for {subject}:")
        found = False
        for s in study_sessions:
            if s["subject"].lower() == subject.lower():
                print(f"{s['subject']}: {s['minutes']} minutes")
                found = True
        if not found:
            print("No sessions found for that subject.")
    elif choice == "4":
        print("Bye")
        break;