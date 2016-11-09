class Pirate():
    v = 0

    def drink_rum(self):
        self.v += 1

    def hows_goin_mate(self):
        if self.v >= 5:
            return "Arrrrr!"
        else:
            return "Nothin'"


pr = Pirate()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
print(pr.hows_goin_mate())
