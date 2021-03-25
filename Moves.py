"""
Moves Class
Author: Niklaas Cotta
"""

import random


class Move:
    def __init__(self, name, damage, tag="enemy", effect=None):
        self.name = name  # Name of attack
        self.damage = damage  # damage
        self.tag = tag  # used on self vs enemy
        self.effect = effect  # effects, implementing later

    def critical(self):  # FIXME
        critHit = (random.randint(0, 100) > 90)  # 10%

        if critHit:
            print("You landed a critical!!")
            self.damage *= 1.5

    def effect(self):
        pass


class Splash(Move):
    def __init__(self):
        super().__init__("Splash", 2)


class Loaf(Move):
    def __init__(self):
        super().__init__("Loaf", 0)


class Rake(Move):
    def __init__(self):
        super().__init__("Claw", 5)


class Regrowth(Move):
    def __init__(self):
        super().__init__("Regrowth", -2, "self")


class Tentacle(Move):
    def __init__(self):
        super().__init__("Tentacle", 3)


class Psywave(Move):
    def __init__(self):
        super().__init__("Psywave", 4)


class Thorns(Move):
    def __init__(self):
        super().__init__("Thorns", 3)


class Absorb(Move):
    def __init__(self):
        super().__init__("Absorb", -4, "self")
