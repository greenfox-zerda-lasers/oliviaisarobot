from tkinter import *
from PIL import Image, ImageTk
import random
import texts
import os

class View():

    def __init__(self):
        self.root = Tk()
        self.root.title("T K W A N D E R E R")
        self.hero_img = ""
        self.enemy_img = ""
        self.boss_img = ""
        self.map = []

    def resize(self, img_path, width, height): # unused at the moment
        image = Image.open(img_path)
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def status_frame(self, player_health, player_strike, player_defense):
        player_status = Message(text="HP  {} | SP  {} | DP  {}".format(player_health, player_strike, player_defense), anchor="w")
        player_status.pack(expand=True, fill="x")
        player_status.bind("<Configure>", lambda e: player_status.configure(width=e.width-10))

    def enemy_status_frame(self, enemy_health, enemy_strike, enemy_defense):
        separator = Frame(height=2, bd=2, relief=RIDGE)
        separator.pack()
        enemy_status = Message(text="HP | {} DP | {} SP | {}".format(enemy_health, enemy_strike, enemy_defense))
        enemy_status.pack()

    def console_frame(self):
        self.console = Frame(height=72, bd=2, relief=RIDGE, bg="#888888")
        self.console.pack(fill=X, padx=5, pady=5)

#    def console_message(self, message):
#        self.current_message = Message(master=self.console, text=message, anchor="w", font="Courier", bg="#888888")
#        self.current_message.pack(expand=True, fill="x")
#        self.current_message.bind("<Configure>", lambda e: self.current_message.configure(width=e.width-10))

    def game_board_generator(self):
        self.game_board = Canvas(self.root, width=720, height=520)
        self.game_board.pack(padx=20, pady=20)
        self.draw_map()

    def draw_map(self):
        self.floor = self.resize("images/tiles/floor.png", 50, 50)
        self.wall = self.resize("images/tiles/wall.png", 50, 50)
        x = 0
        y = 0
        for i in range(100):
            if i == 0:
                self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                self.map += "F"
            elif i > 0 and i < 10:
                x += 50
                self.random_tile(x, y)
            elif i == 10:
                x = 0
                y += 50
                self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                self.map += "F"
            elif i > 10:
                x += 50
                if i%10 == 0:
                    y += 50
                    x = 0
                    if self.map[i-10] == "F" and self.map[i-9] == "W":
                        self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                        self.map += "F"
                    elif self.map[i-1] == "W" and self.map[i-2] == "W":
                        self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                        self.map += "F"
                    elif self.map[i-10] == "W" and self.map[i-9] == "W":
                        self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                        self.map += "F"
                    else:
                        self.random_tile(x, y)
                else:
                    if self.map[i-1] == "F" and self.map[i-9] == "W":
                        self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                        self.map += "F"
                    elif self.map[i-1] == "W" and self.map[i-2] == "W":
                        self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                        self.map += "F"
                    elif self.map[i-10] == "W":
                        self.game_board.create_image(x, y, image=self.floor, anchor=NW)
                        self.map += "F"
                    else:
                        self.random_tile(x,y)
        print(self.map)

    def random_tile(self, x, y):
        random_index = random.randint(0, 1)
        if random_index == 1:
            self.game_board.create_image(x, y, image=self.floor, anchor=NW)
            self.map += "F"
        else:
            self.game_board.create_image(x, y, image=self.wall, anchor=NW)
            self.map += "W"

    def hero_position_up(self, x, y):
        self.hero_img = self.resize("images/hero-up.png", 50, 50)
        self.game_board.create_image(x, y, image=self.hero_img, anchor=NW)

    def hero_position_down(self, x, y):
        self.hero_img = self.resize("images/hero-down.png", 50, 50)
        self.game_board.create_image(x, y, image=self.hero_img, anchor=NW)

    def hero_position_left(self, x, y):
        self.hero_img = self.resize("images/hero-left.png", 50, 50)
        self.game_board.create_image(x, y, image=self.hero_img, anchor=NW)

    def hero_position_right(self, x, y):
        self.hero_img = self.resize("images/hero-right.png", 50, 50)
        self.game_board.create_image(x, y, image=self.hero_img, anchor=NW)

    def enemy_loadimg(self, x, y):
        self.enemy_img = self.resize("images/skeleton.png", 50, 50)
        self.game_board.create_image(x, y, image=self.enemy_img, anchor=NW)

    def boss_loadimg(self, x, y):
        self.boss_img = self.resize("images/boss.png", 50, 50)
        self.game_board.create_image(x, y, image=self.boss_img, anchor=NW)

#app = View()
#app.load_all_frames(texts.game_greet)
