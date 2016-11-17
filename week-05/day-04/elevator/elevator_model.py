# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class Model():

    def __init__(self):
        self.capacity = 5
        self.people = 0
        self.position = 1

    def set_position(self, pos):
        if pos.lstrip("-").isdigit():
            if int(pos) < 1:
                print("You can't move further down than floor 1.")
                self.if_error()
            elif int(pos) > 12:
                print("You are trying to go higher than the top floor. Please enter a smaller number.")
                self.if_error()
            else:
                self.position = int(pos)
        else:
            print("Please enter a number.")
            self.if_error()
        return self.position

    def people(self):
        self.people = people
        return self.people

    def add_people(self, add):
        free = self.capacity - self.people
        if add.lstrip("-").isdigit():
            if int(add) < 0:
                print("Please enter a positive number.")
                self.if_error()
            elif int(add) > free:
                if free == 0:
                    print("There is no more room in the elevator.")
                    self.if_error()
                elif free == 1:
                    print("Too many people are trying to enter the elevator. There is only enough room for 1 person.")
                    self.if_error()
                else:
                    print("Too many people are trying to enter the elevator. There is only enough room for {} people.".format(free))
                    self.if_error()
            else:
                self.people += int(add)
        else:
            print("Please enter a number.")
            self.if_error()
        return self.people

    def remove_people(self, rm):
        if rm.lstrip("-").isdigit():
            if int(rm) < 0:
                print("Please enter a positive number.")
                self.if_error()
            elif int(rm) > self.people:
                print("The number of people leaving can not exceed the number of people in the elevator.")
                self.if_error()
            else:
                self.people -= int(rm)
        else:
            print("Please enter a number.")
            self.if_error()
        return self.people

    def if_error(self):
        print("\nPress any key to continue.")
        user_error = input()
