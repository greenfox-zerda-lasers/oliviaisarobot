from random import randint
from random import choice
import outputs
import rooms


class Adventure_game():

    def __init__(self):
        self.player_hp = 5
        self.player_bravery = 0
        self.visited = []
        self.round = 0
        self.found = False
        self.player_name = ""
        print(outputs.title)

        self.intro()

    #RULES AND START
    def intro(self):
        print(outputs.greet)
        player_name = input()
        self.player_name = player_name
        print(outputs.intro.format(self.player_name, self.player_name))
        print(outputs.rules)
        print(outputs.ruleset)
        self.first_room()

    #START A NEW GAME
    def first_room(self):
        print(outputs.newgame)
        print(outputs.start)
        game_start = input()
        if game_start.lower() == "y":
            self.gameloop()
        else:
            quit

    #ASK IF YOU WANT TO ENTER THE NEXT ROOM
    def next_room(self):
        print(outputs.query)
        next_room = input()
        if next_room.lower() == "n":
            quit
        else:
            pass

    #MAIN GAME
    def gameloop(self):
        while self.found == False:
            self.round += 1
            print(outputs.divider)
            print("ROOM {}\n".format(self.round))
            self.random_room() #ROLL ROOM, DESCRIBE THE ROOM YOU ARE IN
            print(self.visited[-1])
            self.roll_danger() #ROLL FOR DANGER, THERE IS A CHANCE TO DIE AND EXIT LOOP
            self.check_if_alive()
            self.player_bravery += 1
            print(outputs.success)
            self.try_golden_door() #IF BRAVERY IS HIGHER THAN 3, TRY FOR GOLDEN DOOR, IF FOUND, EXIT LOOP
            print(outputs.notyet)
            self.status() #DISPLAY HP AND BRAVERY STATUS
            if len(self.visited) > 0: #CHECK IF FIRST ROOM, TO OFFER DIFFERENT QUEST
                self.next_room()
            else:
                pass

    #GAMELOOP FUNCTIONS
    def status(self):
        print(outputs.check.format(self.player_name, self.player_hp, self.player_bravery))

    def random_room(self):
        current_room = (choice(rooms.roomslib))
        if current_room in self.visited:
            return self.random_room()
        else:
            self.visited.append(current_room)

    def roll_danger(self):
        danger_level = randint(0, 100)
        print("\nThe room's danger level is {}.\n".format(danger_level))
        if danger_level >= 50:
            self.player_hp -= 1
            print(outputs.dangerous)
        else:
    #        self.player_hp -= 1 #ENABLE IF YOU WANT TO LOSE THE GAME
            print(outputs.nodanger)

    def check_if_alive(self):
        if self.player_hp == 0:
            self.found = True
            return self.game_over()

    def try_golden_door(self):
        chance = randint(1, 10)
        if self.player_bravery >= 3 and self.player_bravery < 10:
            if chance > 8:
                self.found = True
                print(outputs.golden_door)
                return self.game_won()
            else:
                pass
        elif self.player_bravery >= 10: #IF STILL ALIVE AFTER BRAVERY LEVEL 10, INCREASE CHANCE OF WINNING
            if chance > 5:
                self.found = True
                print(outputs.golden_door)
                return self.game_won()
            else:
                pass

    def game_over(self):
        print(outputs.game_over.format(self.player_name))
        print(outputs.lose)
        return self.play_again()

    def game_won(self):
        print(outputs.game_won)
        print(outputs.win)
        return self.play_again()

    def play_again(self):
        play_again = input(outputs.retry)
        if play_again.lower() == "y":
            self.reset()
            self.first_room()
        else:
            quit

    def reset(self):
        self.player_hp = 5
        self.player_bravery = 0
        self.visited = []
        self.round = 0
        self.found = False

newgame = Adventure_game()
newgame.gameloop()
