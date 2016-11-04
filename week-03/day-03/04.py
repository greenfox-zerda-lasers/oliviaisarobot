# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():

    def __init__(self, name):
        self.grades = []
        self.name = name

    def add_grade(self, newgrade):
        self.newgrade = newgrade
        if self.newgrade > 0 and self.newgrade < 6 and self.newgrade%1 is 0:
            self.grades.append(self.newgrade)
            print("Grade", self.newgrade, "successfully added to", self.name + ".")
            return self.grades
        else:
            print("Invalid grade. Please enter a number between 1 and 5.")

    def get_grades(self):
        return "Grades of " + str(self.name) + ": "+ str(self.grades) + "."

    def get_average(self):
        sum = 0
        for i in range(0,len(self.grades)):
            sum += self.grades[i]
        return "Average of " + str(self.name) + ": " + str(sum/len(self.grades))

student1 = Student("Anna")
student1.add_grade(3)
student1.add_grade(4)
student1.add_grade(0)
student1.add_grade(5)
print(student1.get_grades())
print(student1.get_average())
student2 = Student("Bernie")
student2.add_grade(2)
student2.add_grade(5)
student2.add_grade(4)
print(student2.get_grades())
print(student2.get_average())
