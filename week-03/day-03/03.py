# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate():
    rum_lvl = 0

    def drink_rum(self):
        self.rum_lvl += 1

    def hows_goin_mate(self):
        if self.rum_lvl == 5:
            return "Arrrr!"
        else:
            return "Nothin'"

oldpirate = Pirate()
oldpirate.drink_rum()
print(oldpirate.hows_goin_mate())
oldpirate.drink_rum()
oldpirate.drink_rum()
oldpirate.drink_rum()
oldpirate.drink_rum()
print(oldpirate.hows_goin_mate())
oldpirate.drink_rum()
print(oldpirate.hows_goin_mate())
