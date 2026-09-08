class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = Grade(grade)

class Grade:
    def __init__(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

    def evaluate(self):
        if self.grade >= 96:
            return "1.00"
        elif self.grade >= 90 and self.grade < 96:
            return "1.25"
        elif self.grade >= 85 and self.grade < 90:
            return "1.50"
        elif self.grade >= 80 and self.grade < 85:
            return "1.75"
        elif self.grade >= 75 and self.grade < 80:
            return "2.00"  
        elif self.grade >= 70 and self.grade < 75:
            return "2.25"
        elif self.grade >= 65 and self.grade < 70:
            return "2.50"
        elif self.grade >= 60 and self.grade < 65:
            return "2.75"
        else:
            return "Failed"

class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

s1 =  student("John", 15, 90)#adding a test student
print(f"{s1.name}'s grade is: {s1.grade.evaluate()}")