# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle():
    r = 0
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def get_circumference(self):
        return 2 * self.r * self.pi

    def get_area(self):
        return self.r ** 2 * self.pi

newCircle = Circle(50)
print(newCircle.get_circumference())
print(newCircle.get_area())
