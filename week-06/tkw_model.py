import random

class Entity():
    def dice_roll(self):
        return random.randint(1, 6)

    def conversion_position_to_x(self, posit):
        if posit == 0:
            return 0
        if posit > 0 and posit < 10:
            x = 0 + 50 * (posit)
            return x
        elif posit >= 10:
            x = 0 + 50 * (posit%10)
            return x

    def conversion_position_to_y(self, posit):
        if posit == 0:
            return 0
        if posit > 0 and posit < 10:
            y = 0
            return y
        elif posit >= 10:
            y = 0 + 50 * (posit//10)
            return y

class Hero(Entity):
    def __init__(self):
        self.hero_position = 0
        self.hero_level = 1
        self.hero_health = 20 + 3 * self.dice_roll()
        self.hero_defense = 2 * self.dice_roll()
        self.hero_strike = 5 + self.dice_roll()

    def hero_position_update(self, num):
        self.hero_position += (int(num))
        return self.hero_position

#    def hero_level_update(self):
#        self.hero_level += 1
#        return self.hero_level

#    def hero_health_update(self, num):
#        self.hero_health += (int(num))
#        return self.hero_health

#    def hero_defense_update(self, num):
#        self.hero_defense += (int(num))
#        return self.hero_defense

#    def hero_strike_update(self, num):
#        self.hero_strike += (int(num))
#        return self.hero_strike

class Skeleton(Entity):
    def __init__(self, level):
        self.enemy_position = 1
        self.enemy_level = level
        self.enemy_health = 2 * level * self.dice_roll()
        self.enemy_defense = level/2 * self.dice_roll()
        self.enemy_strike = level * self.dice_roll()

class Boss(Entity):
    def __init__(self, level):
        self.boss_position = 1
        self.boss_level = level
        self.boss_health = 2 * level * self.dice_roll() + self.dice_roll()
        self.boss_defense = level/2 * self.dice_roll() + self.dice_roll()/2
        self.boss_strike = level * self.dice_roll() + self.boss_level

    def boss_position_update(self, num):
        self.boss_position = (int(num))
        return self.boss_position
