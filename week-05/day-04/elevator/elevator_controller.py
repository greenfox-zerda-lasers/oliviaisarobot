# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

from elevator_model import Model
from elevator_view import View
import os

class Ele_main():
    running = False

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.running = True

    def controller(self):
        #main loop begins
        while self.running is True:
            os.system("clear")
            self.view.intro(self.model.position, self.model.people)
            user_input = input()
            command = user_input.split()
            if len(command) > 2:
                self.view.invalid_command()
            else:
                if command[0] == "to":
                    self.model.set_position(command[1])
                elif command[0] == "in":
                    self.model.add_people(command[1])
                elif command[0] == "out":
                    self.model.remove_people(command[1])
                elif user_input == "exit":
                    self.running = False
                    quit()
                else:
                    self.view.invalid_command()

elevator = Ele_main()
elevator.controller()
