programming_languages = ["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "Rust"]

print("First", programming_languages[0])
print("Last", programming_languages[-1])
print("Third", programming_languages[2])
print("Second-to-last", programming_languages[-2])
print("First three:", programming_languages[:3])
print("Last three:", programming_languages[-3:])
print("All except the first and last:", programming_languages[1:-1])
print("Every second:", programming_languages[::2])
print("Reverse order:", programming_languages[::-1])

programming_languages.append("Swift")
print("append",programming_languages)
programming_languages.insert(2, "Kotlin")
print("insert",programming_languages)
programming_languages.remove("C#")
print("remove",programming_languages)
programming_languages.pop(-1)
print("pop",programming_languages)

numeric_list = [6, 2, 3, 4, 5]
numeric_list_2 = [1, 2, 3, 4, 5]

numeric_list.sort()
numeric_list_2.sort(reverse=True)
print("length:", len(numeric_list))
print("min value:", min(numeric_list))
print("max value:", max(numeric_list))
print("sum:", sum(numeric_list))

print("sort ascending:", numeric_list)
print("sort descending:", numeric_list_2)

# sort sorts the existing list. Sorted creates a new list so the old list remains intact.

list_a = [1, 2, 3, 4, 5]
list_b = list_a

list_a.append(6)

print(list_b) # list b is just a reference to list a, so it will also show the appended value.

list_b = list_a.copy()
list_a.append(7)

print(list_b) # list b is now a copy of list a, so it will not show the appended value.