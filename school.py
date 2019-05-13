class School:
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, student, grade_level):
        self.name = student
        self.grade_level = grade_level
        if grade_level in self.roster:
            self.roster[grade_level].append(student)
        else:
            self.roster[grade_level] = [student]

    def grade(self, grade_level):
        return self.roster[grade_level] if grade_level in self.roster else 'This grade is not a part of our roster'
            
    def sort_roster(self):
        for key in self.roster:
            self.roster[key] = sorted(self.roster[key])
        return self.roster




class Student:
    def __init__(self, name=None, grade=None):
        self.name = name
        self.grade = grade