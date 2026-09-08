name = "Johanna"
course_name = "Python fundamentals"
lab_goal = "Learn the basics of Python programming"

print(name)
print(course_name)
print(lab_goal)

student_name = "Johanna"
student_age = 45
student_height_m = 1.69
is_student = True

print(student_name, type(student_name))
print(student_age, type(student_age))
print(student_height_m, type(student_height_m))
print(is_student, type(is_student))

print(type(student_age))
student_age = 45.5 #  Changes the type for the variable student_age from int to float which shows that python is a dynamically typed language
print(type(student_age))

x = 6
y = 7

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} // {y} = {x // y}")

# string to integer to be able to perform calculations
z = "10"
print(f"{z} + {y} = {int(z) + y}")

# integer to float to be able to get decimal values
a = float(y)
print(a)

# number to string to easily concatenate with other strings
b = str(y)
print(type(b))




