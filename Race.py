"""
Race Program
Author: Niklaas Cotta
"""

import random


class Race:
    def __init__(self, name, appearance, attribute):
        self.name = name
        self.appearance = appearance
        self.attribute = attribute

    def queryName(self):
        suffix = ["clan.", "people.", "race."]
        i = random.randint(0, 2)
        print("You are one of the", self.name, suffix[i])

    def queryLooks(self):
        print("You appear to be...", self.appearance)

    def passive(self):
        # gets overridden by subclass method
        pass


class Lizard(Race):
    def __init__(self):
        super().__init__("Lizard",
                         "a large, green, and frighteningly ferocious reptile",
                         "fire")


class Werepus(Race):
    def __init__(self):
        super().__init__("Werepus",
                         "your friendly neighborhood cephalopod, now including a wild side!",
                         "water")


class MonsterA(Race):
    def __init__(self):
        super().__init__("Monster-a",
                         "a luscious sentient plant with beautiful fenestrations",
                         "grass")


if __name__ == '__main__':
    """
    myLizard = Lizard()
    myLizard.queryName()
    myLizard.queryLooks()
    print(myLizard.attribute)

    myWerepus = Werepus()
    myWerepus.queryName()
    myWerepus.queryLooks()
    print(myWerepus.attribute)

    myMonsterA = MonsterA()
    myMonsterA.queryName()
    myMonsterA.queryLooks()
    print(myMonsterA.attribute)
    """
    pass
