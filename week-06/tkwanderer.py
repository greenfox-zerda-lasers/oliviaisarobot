from tkinter import *
import texts
import os
from tkw_display import View
from tkw_model import *
#from tkw_model import Hero
#from tkw_model import Boss

class Engine():
    player_alive = True
    boss_alive = True
    key_found = False

    keystroke_counter = 0
    level = 1

    def __init__(self):
        self.view = View()
        self.hero = Hero()
        self.boss = Boss(self.level)

#        self.rules_and_start()

        self.view.root.bind("<Right>", self.position_if_key)
        self.view.root.bind("<Left>", self.position_if_key)
        self.view.root.bind("<Up>", self.position_if_key)
        self.view.root.bind("<Down>", self.position_if_key)
        self.view.root.bind("<Enter>", self.position_if_key)

        self.gameloop()

    def position_if_key(self, event):
        if self.collision() == True:
            self.view.enemy_status_frame(self.select_current_enemy())
            self.battle()
#        elif self.keystroke_counter%2 == 0:
#            self.boss_move()
        else:
            if event.keysym == "Right":
                self.hero_move_right()
            elif event.keysym == "Left":
                self.hero_move_left()
            elif event.keysym == "Up":
                self.hero_move_up()
            elif event.keysym == "Down":
                self.hero_move_down()

    def rules_and_start(self):
        print(texts.game_rules)

    def gameloop(self):
        self.view.status_frame(self.hero.hero_health, self.hero.hero_strike, self.hero.hero_defense)
        self.view.console_frame()
#       self.view.console_message(message)
        self.view.game_board_generator()
        self.generate_boss_spawn()
        self.get_hero_position()
        self.get_boss_position()
        self.view.root.mainloop()

    def get_hero_position(self):
        self.view.hero_position_down(self.hero.conversion_position_to_x(self.hero.hero_position), self.hero.conversion_position_to_y(self.hero.hero_position))

    def generate_boss_spawn(self):
        random_number = random.randint(2, 100)
        if self.view.map[random_number] != "F":
            return self.generate_boss_spawn()
        if self.view.map[random_number] == "F":
            self.boss.boss_position_update(random_number)

    def get_boss_position(self):
        self.view.boss_loadimg(self.boss.conversion_position_to_x(self.boss.boss_position), self.boss.conversion_position_to_y(self.boss.boss_position))

    def hero_move_right(self):
        if self.hero.conversion_position_to_x(self.hero.hero_position) >= 450:
            self.stop_npc_if_wall()
        elif self.view.map[self.hero.hero_position + 1] == "W":
            self.stop_npc_if_wall()
        else:
            self.hero.hero_position_update(1)
            self.view.hero_position_right(self.hero.conversion_position_to_x(self.hero.hero_position), self.hero.conversion_position_to_y(self.hero.hero_position))
            self.keystroke_counter += 1

    def hero_move_left(self):
        if self.hero.conversion_position_to_x(self.hero.hero_position) <= 0:
            self.stop_npc_if_wall()
        elif self.view.map[self.hero.hero_position - 1] == "W":
            self.stop_npc_if_wall()
        else:
            self.hero.hero_position_update(-1)
            self.view.hero_position_left(self.hero.conversion_position_to_x(self.hero.hero_position), self.hero.conversion_position_to_y(self.hero.hero_position))
            self.keystroke_counter += 1

    def hero_move_up(self):
        if self.hero.conversion_position_to_y(self.hero.hero_position) <= 0:
            self.stop_npc_if_wall()
        elif self.view.map[self.hero.hero_position - 10] == "W":
            self.stop_npc_if_wall()
        else:
            self.hero.hero_position_update(-10)
            self.view.hero_position_up(self.hero.conversion_position_to_x(self.hero.hero_position), self.hero.conversion_position_to_y(self.hero.hero_position))
            self.keystroke_counter += 1

    def hero_move_down(self):
        if self.hero.conversion_position_to_y(self.hero.hero_position) >= 450:
            self.stop_npc_if_wall()
        elif self.view.map[self.hero.hero_position + 10] == "W":
            self.stop_npc_if_wall()
        else:
            self.hero.hero_position_update(10)
            self.view.hero_position_down(self.hero.conversion_position_to_x(self.hero.hero_position), self.hero.conversion_position_to_y(self.hero.hero_position))
            self.keystroke_counter += 1

    def boss_available_moves(self):
        self.available = []
    #    print(self.boss.boss_position)
        for i in range(4):
            if i == 0 and self.boss.conversion_position_to_x(self.boss.boss_position) <= 450 and self.view.map[self.boss.boss_position + 1] != "W":
                self.available.append("Move right")
            elif i == 1 and self.boss.conversion_position_to_x(self.boss.boss_position) >= 0 and self.view.map[self.boss.boss_position - 1] != "W":
                self.available.append("Move left")
            elif i == 2 and self.boss.conversion_position_to_y(self.boss.boss_position) >= 0 and self.view.map[self.boss.boss_position - 10] != "W":
                self.available.append("Move up")
            elif i == 3 and self.boss.conversion_position_to_y(self.boss.boss_position) <= 450 and self.view.map[self.boss.boss_position + 10] != "W":
                self.available.append("Move down")
    #    print(self.view.map[self.boss.boss_position])
    #    print(self.view.map[self.boss.boss_position - 1])
    #    print(self.view.map[self.boss.boss_position - 11])
    #    print(self.view.map[self.boss.boss_position + 10])
        return self.available

    def stop_npc_if_wall(self):
        if self.keystroke_counter%2 == 0:
            self.keystroke_counter += 3
        pass

    def boss_move(self):
        self.boss_available_moves()
    #    print(self.available)
        if len(self.available) == 1:
            if self.available[0] == "Move right":
                self.boss.boss_position_update(self.boss.boss_position + 1)
                self.get_boss_position()
            elif self.available[0] == "Move left":
                self.boss.boss_position_update(self.boss.boss_position - 1)
                self.get_boss_position()
            elif self.available[0] == "Move up":
                self.boss.boss_position_update(self.boss.boss_position - 9)
                self.get_boss_position
            elif self.available[0] == "Move down":
                self.boss.boss_position_update(self.boss.boss_position + 9)
                self.get_boss_position()
        elif len(self.available) > 1:
            random_index = random.randint(0, len(self.available))
            if self.available[random_index] == "Move right":
                self.boss.boss_position_update(self.boss.boss_position + 1)
                self.get_boss_position()
            elif self.available[random_index] == "Move left":
                self.boss.boss_position_update(self.boss.boss_position - 1)
                self.get_boss_position()
            elif self.available[random_index] == "Move up":
                self.boss.boss_position_update(self.boss.boss_position - 10)
                self.get_boss_position
            elif self.available[random_index] == "Move down":
                self.boss.boss_position_update(self.boss.boss_position + 10)
                self.get_boss_position()
        else:
            pass

    def collision(self):
        if self.hero.hero_position == self.boss.boss_position:
            return True
        return False

    def select_current_enemy(self):
        if self.hero.hero_position == self.boss.boss_position:
            return(str(self.boss.boss_health) + ", " + str(self.boss.boss_strike) + ", " + str(self.boss.boss_defense))

    def battle(self):
        print("Battle time!")

app = Engine()
