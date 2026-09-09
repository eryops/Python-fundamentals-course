courses = ["Python", "Java", "C++", "JavaScript", "SQL", "Python"]
print("list length:", len(courses))

unique_courses = set(courses)
print("second list length:", len(unique_courses))

skills_person_1 = {"Python", "Java", "C++", "JavaScript", "SQL"}
skills_person_2 = {"Python", "Java", "C#", "JavaScript", "SQL"}

print("unique skills for person 1 that person 2 doesn't have:", skills_person_1.difference(skills_person_2))
print("unique skills combined for both persons:", skills_person_1.union(skills_person_2))
print("skills that both persons have in common:", skills_person_1.intersection(skills_person_2))

skills = {"Python", "Java", "C++", "JavaScript", "SQL"}
skills.add("C#")
skills.remove("SQL")
skills.discard("JavaScript")

print("checking if a skill is in the set:", "Python" in skills)
print("checking if discarded skill is in the set:", "JavaScript" in skills)

# sets are better to use then lists because it is easier to check if a value is in a set or not. A set has to be unique.