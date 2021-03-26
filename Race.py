"""
File for races
Author: Niklaas Cotta
"""

from Moves import *


class Race:
    def __init__(self, name, appearance, attribute, statsList, movesList):
        self.name = name
        self.appearance = appearance
        self.attribute = attribute
        self.statsList = statsList  # [attack, defense, speed]
        self.movesList = movesList

    def queryName(self):
        suffix = ["clan.", "people.", "race."]
        print("You are one of the", self.name, suffix[random.randint(0, 2)])

    def queryLooks(self):
        print("You appear to be...", self.appearance)

    def passive(self):
        # gets overridden by subclass method, implement later
        pass


class Lizard(Race):
    def __init__(self, statsList):  # [12, 10, 8]
        super().__init__("Lizard",
                         "a large lizard with green scales that glisten in the sun. You lick your eyeball casually.",
                         "fire",
                         statsList,
                         [Rake(), Regrowth()])


class Werepus(Race):
    def __init__(self, statsList):  # [8, 12, 10]
        super().__init__("Werepus",
                         "a friendly neighborhood cephalopod, now includes claws!",
                         "water",
                         statsList,
                         [Tentacle(), Psywave()])


class MonsterA(Race):
    def __init__(self, statsList):  # [10, 8, 12]
        super().__init__("Monster-a",
                         "a luscious sentient plant with beautiful fenestrations",
                         "grass",
                         statsList,
                         [Thorns(), Absorb()])
