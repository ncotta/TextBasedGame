"""
Moves Class
Author: Niklaas Cotta
"""

import random


class Move:
    def __init__(self, name, damage, tag, effect=None):
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


class Rake(Move):
    def __init__(self):
        super().__init__("Rake", 5, "enemy")


class Regrowth(Move):
    def __init__(self):
        super().__init__("Regrowth", -4, "self")


class Splash(Move):
    def __init__(self):
        super().__init__("Splash", 2, "enemy")
