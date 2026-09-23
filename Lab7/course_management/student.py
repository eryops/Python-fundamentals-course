class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return 'PASS' if self.score >= 70 else 'FAIL'

    def __repr__(self):
        return f'{self.name} - score {self.score}'