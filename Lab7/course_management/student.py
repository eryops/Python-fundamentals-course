class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return 'PASS' if self.score >= 70 else 'FAIL'

    def update_score(self, new_score):
        if 0 <= new_score <= 100:
            self.score = new_score
        else:
            raise ValueError('Score needs to be between 0 and 100')

    def __repr__(self):
        return f'{self.name} - score {self.score}'