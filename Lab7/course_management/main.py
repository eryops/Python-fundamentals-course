from student import Student
from teacher import Teacher
from course import Course

student1 = Student("Astrid", 45)
student2 = Student("Stig", 99)
student3 = Student("Ali", 77)
student4 = Student("Lisa", 67)
student5 = Student("Linda", 65)
student6 = Student("Johanna", 88)

students = [student1, student2, student3, student4, student5, student6]

teacher_one = Teacher('Nils')
course_one = Course('Python', teacher_one)

for student in students:
    course_one.add_student(student)

print(f'Course: {course_one}')
print(f'Passed students: {course_one.passed_students()}')
print(f'Number of students: {course_one.count_students()}')