"""
Race Program
Author: Niklaas Cotta
"""

import random


class Race:
    def __init__(self, name, appearance):
        self.name = name
        self.appearance = appearance

    def queryName(self):
        suffix = ["clan.", "people.", "race."]
        i = random.randint(0, 2)
        print("You are one of the", self.name, suffix[i])

    def queryLooks(self):
        print("You appear to be...", self.appearance)


class Lizard(Race):
    def __init__(self):
        super().__init__("Lizard",
                         "a large, green, and frighteningly ferocious reptile")


class Werepus(Race):
    def __init__(self):
        super().__init__("Werepus",
                         "your friendly neighborhood cephalopod but with a wild side!")


if __name__ == '__main__':
    myLizard = Lizard()
    myLizard.queryName()
    myLizard.queryLooks()

    myWerepus = Werepus()
    myWerepus.queryName()
    myWerepus.queryLooks()
