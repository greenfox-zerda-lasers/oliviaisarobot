import sys
import csv

class Model():
    def add_task(self, filename, name):
        if len(sys.argv) < 3:
            print("ERROR: Unable to add, no task is provided.")
        else:
            f = open(filename, "a")
            f.writelines("0,"+" ".join(name)+"\n")
            f.close()

    def remove_task(self, filename, num):
        if num.lstrip("-").isdigit():
            f = open(filename, "r")
            tasks = f.readlines()
            f.close()
            if int(num) < 1:
                print(self.negative())
            elif int(num) > len(tasks):
                print(self.outofbound())
            else:
                tasks.pop(int(num)-1)
                f = open(filename, "w")
                f.writelines(tasks)
                f.close()
        else:
            print(self.notnumber())

    def complete_task(self, filename, num):
        if num.lstrip("-").isdigit():
            f = open(filename, "r")
            tasks = f.readlines()
            f.close()
            if int(num) < 1:
                print(self.negative())
            elif int(num) > len(tasks):
                print(self.outofbound())
            else:
                for i in range(len(tasks)):
                    if i == int(num)-1:
                        temp = list(tasks[i])
                        temp[0] = "1"
                        tasks[i] = "".join(temp)
                f = open(filename, "w")
                f.writelines(tasks)
                f.close()
        else:
            print(self.notnumber())

    def invalid_command(self):
        return("ERROR: Unsupported argument.")

    def negative(self):
        return("ERROR: Index can't be negative.")

    def notnumber(self):
        return("ERROR: Index is not a number.")

    def outofbound(self):
        return("ERROR: Index is out of bound.")

    def noindex(self):
        return("ERROR: No index is provided.")

#new = Model()
#print(new.complete_task("todo_list.csv", sys.argv[2]))
