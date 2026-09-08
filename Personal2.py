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
        if self.grade >= 90:
            return "1.25+"
        elif self.grade >= 80:
            return "1.75+"
        elif self.grade >= 70:
            return "2.25+"
        elif self.grade >= 60:
            return "2.75+"
        else:
            return "Failed"

s1 =  student("John", 20, 95)
print(f"{s1.name}'s grade is: {s1.grade.evaluate()}")