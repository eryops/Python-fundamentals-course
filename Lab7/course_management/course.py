from student import Student
from teacher import Teacher

class Course:
    def __init__(self, course_name, teacher):
        if not isinstance(teacher, Teacher):
             raise ValueError('Teacher must be a Teacher object')

        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError('Student must be a Student object')
        
        self.students.append(student)

    def count_students(self):
         return len(self.students)

    def passed_students(self):
         return [student for student in self.students if student.get_status() == 'PASS']

    def students_above(self, threshold):
        return [student for student in self.students if student.score > threshold]

    def __repr__(self):
            return f'{self.course_name} - teacher {self.teacher}, students {self.students}'