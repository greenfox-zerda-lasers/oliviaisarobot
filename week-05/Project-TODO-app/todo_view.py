
class Visual():

    def controls(self):
        return("\n\nPython Todo application\n=======================\n\nCommand line arguments:\n -l   Lists all the tasks\n -a   Adds a new task by name\n -r   Removes an task by number\n -c   Completes a task by number\n")

    def header(self):
        return("\n=========== ToDo List ===========\n")

    def list_tasks(self, filename):
        f = open(filename, "r")
        tasks = f.readlines()
        f.close()
        output = ""
        if len(tasks) == 0:
            output = "No todos for today! :)\n"
        else:
            num = 0
            for item in tasks:
                num += 1
                if "0" in item[0:2]:
                    output += str(num) + " - [ ] " + item[2:]
                else:
                    output += str(num) + " - [x] " + item[2:]
        print(self.header() + "\n" + output)

#new = Visual()
#print(new.list_tasks("todo_list.csv"))
