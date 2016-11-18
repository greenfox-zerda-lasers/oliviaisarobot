from todo_view import Visual
from todo_model import Model
import csv
import sys
import os

class To_do_app():
    status = []

    def __init__(self):
        os.system("clear")
        self.view = Visual()
        self.model = Model()
        print(self.view.controls())

    def command(self, filename):
        os.system("clear")
        try:
            if len(sys.argv) == 1:
                quit()
            elif "-l" == sys.argv[1]: #list tasks
                print(self.view.list_tasks(filename))
                quit()
            elif "-a" == sys.argv[1]: #add task
                self.model.add_task(filename, sys.argv[2:])
                print(self.view.list_tasks(filename))
                quit()
            elif "-r" == sys.argv[1]: #remove task
                if len(sys.argv) < 3:
                    print(self.model.noindex())
                    quit()
                else:
                    self.model.remove_task(filename, sys.argv[2])
                    print(self.view.list_tasks(filename))
                    quit()
            elif "-c" == sys.argv[1]: #complete task
                if len(sys.argv) < 3:
                    print(self.model.noindex())
                    quit()
                else:
                    self.model.complete_task(filename, sys.argv[2])
                    print(self.view.list_tasks(filename))
                    quit()
            else:
                print(self.model.invalid_command)
                quit()
        except FileNotFoundError:
            f = open(filename, "w+")
            f.close()
            print("New list created.")
            quit()

mylist = To_do_app()
mylist.command("todo_list.csv")
