# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():
    first_name = ""
    last_name = ""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        return "Greetings " + str(self.first_name) + " " + str(self.last_name)

class Student(Person):
    grades = []

    def add_grade(self, grade):
        self.grade = grade
        if self.grade > 0 and self.grade < 6 and self.grade%1 is 0:
            self.grades.append(grade)
            print("Grade", self.grade, "successfully added to", self.first_name, self.last_name + ".")
            return self.grades
        else:
            print("Invalid grade. Please enter a number between 1 and 5.")

    def salute(self):
        sum = 0
        for i in range(0,len(self.grades)):
            sum += self.grades[i]
        return str(self.greet()) + ", your average is " + str(sum/len(self.grades)) + "."

student1 = Student("Jane", "Doe")
print(student1.greet())
student1.add_grade(4)
student1.add_grade(3)
student1.add_grade(5)
print(student1.salute())
