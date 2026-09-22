class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return 'PASS' if self.score >= 70 else 'FAIL'

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

