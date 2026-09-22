class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return 'PASS' if self.score >= 70 else 'FAIL'

class Teacher:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# --- Main like section ---

student1 = Student("Astrid", 45)
student2 = Student("Stig", 99)
student3 = Student("Ali", 77)
student4 = Student("Lisa", 67)
student5 = Student("Linda", 65)
student6 = Student("Johanna", 88)

students = [student1, student2, student3, student4, student5, student6]

for student in students:
    print(f'{student.name} - score: {student.score}')

for student in students:
    print(f'{student.name} -  {student.get_status()}')

passing_students = [student for student in students if student.get_status() == 'PASS']
for student in passing_students:
    print(student.name, student.score)

teacher_one = Teacher('Nils')
course_one = Course('Python', teacher_one)
course_one.add_student(student1)
course_one.add_student(student2)
course_one.add_student(student3)

print(course_one.teacher, course_one.course_name)

course_students = [student.name for student in course_one.students]
print(course_students)