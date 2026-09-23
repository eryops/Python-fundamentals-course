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

course_two = Course('JavaScript', teacher_one)
course_two.add_student(student2)
course_two.add_student(student3)

print(f'Course One: {course_one}')
print(f'Course Two: {course_two}')
print(f'Passed students: {course_one.passed_students()}')
print(f'Number of students: {course_one.count_students()}')
print(f'Students above threshold: {course_one.students_above(87)}')