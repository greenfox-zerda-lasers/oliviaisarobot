# Create a class the displays the Elevator art and navigation (list of commands)

class View():
    building_levels = 12
    building_width = 35

    def intro(self, position, people):
        print("\n----- THE MIGHTY ELEVATOR -----\n")
        print("People in the elevator: {} (max. 5)\nElevator position: {}\n".format(people, position))
        print(self.draw_top())
        print(self.draw_levels(position, people))
        print(self.draw_bottom())
        print(self.nav())
        print("\nWhat would you like to do?")

    def draw_top(self):
        top1 = ""
        for i in range(self.building_width):
            top1 += "_"
        top2 = "'"
        for j in range(1, self.building_width-1):
            top2 += " "
        top2 += "'"
        top3 = " '"
        for i in range(2, self.building_width-2):
            top3 += "_"
        top3 += "'"
        return top1 + "\n" + top2 + "\n" + top3

    def draw_levels(self, position, people):
        levels = ""
        for i in range(self.building_levels, 0, -1):
            if i == 1 and position != 1:
                levels += " "*2 + "_" + "||_"*2 + "_"*6 + "||_"*2 + "_"*6 + "||_"*2
            elif i == position and position != 1:
                levels += self.draw_elevator(position, people)
            elif i == position and position == 1:
                levels += self.draw_elevator(position, people)
            else:
                levels += " "*3 + "|| "*2 + " "*6 + "|| "*2 + " "*6 + "|| "*2 + "\n"
        return levels

    def draw_bottom(self):
        line2 = "'"
        for j in range(1, self.building_width-1):
            line2 += " "
        line2 += "'"
        line3 = "|"
        for i in range(1, self.building_width-1):
            line3 += "_"
        line3 += "|"
        return line2 + "\n" + line3

    def draw_elevator(self, position, people):
        elevator = ""
        if position != 1 and people == 0:
            elevator += " "*3 + "|| "*2 + "[   ] " + "|| "*2 + " "*6 + "|| "*2 + "\n"
        elif position == 1 and people == 0:
            elevator += " "*2 + "_" + "||_"*2 + "[___]_" + "||_"*2 + "_"*6 + "||_"*2
        elif position != 1 and people > 0:
            elevator += " "*3 + "|| "*2 + "[ X ] " + "|| "*2 + " "*6 + "|| "*2 + "\n"
        elif position == 1 and people > 0:
            elevator += " "*2 + "_" + "||_"*2 + "[_X_]_" + "||_"*2 + "_"*6 + "||_"*2
        return elevator

    def nav(self):
        return("\n---- CONTROLS ----\n\nto X - enter a number to move to floor\nin X - enter a number to add people to the elevator\nout X - enter a number to remove people from the elevator\nexit - exit the application")

    def invalid_command(self):
        print("Please enter a valid command.")
        print("\nPress a button to refresh!")
        user_error = input()

#newele = View()
#print(newele.draw_top())
#print(newele.draw_levels(1, 1))
#print(newele.draw_bottom())
#print(newele.nav())
