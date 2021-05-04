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

    def critical(self):
        critHit = (random.randint(0, 100) > 90)  # 10%

        if critHit:
            print("You landed a critical!!")
            self.damage *= 1.5

    def removeCrit(self):
        self.damage /= 1.5

    def effect(self):
        pass


# Dummy
class Splinter(Move):
    def __init__(self):
        super().__init__("Splinter", 1)


class Hammer(Move):
    def __init__(self):
        super().__init__("Wood Hammer", 4)


class Retaliate(Move):
    def __init__(self):
        super().__init__("Retaliate", 2)


class DoNothing(Move):
    def __init__(self):
        super().__init__("Loaf", 0)


# Lizard
class Rake(Move):
    def __init__(self):
        super().__init__("Claw", 4)


class Crunch(Move):
    def __init__(self):
        super().__init__("Crunch", 3)


class Slam(Move):
    def __init__(self):
        super().__init__("Tail Slam", 2)


class Regrowth(Move):
    def __init__(self):
        super().__init__("Regrowth", -2, "self")


# Werepus
class Poison(Move):
    def __init__(self):
        super().__init__("Poison Soak", 3)


class Wrap(Move):
    def __init__(self):
        super().__init__("Wrap", 2)


class Tentacle(Move):
    def __init__(self):
        super().__init__("Tentacle", 3)


class Psywave(Move):
    def __init__(self):
        super().__init__("Psywave", 5)


# MonsterA
class Thorns(Move):
    def __init__(self):
        super().__init__("Thorns", 3)


class Spit(Move):
    def __init__(self):
        super().__init__("Acid Spit", 2)


class Root(Move):
    def __init__(self):
        super().__init__("Root", 1)


class Absorb(Move):
    def __init__(self):
        super().__init__("Absorb", -4, "self")
