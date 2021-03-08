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
                         "a large lizard with green scales that glisten in the sun. You lick your eyeball casually.",
                         "fire")


class Werepus(Race):
    def __init__(self):
        super().__init__("Werepus",
                         "a friendly neighborhood cephalopod, now includes claws!",
                         "water")


class MonsterA(Race):
    def __init__(self):
        super().__init__("Monster-a",
                         "a luscious sentient plant with beautiful fenestrations",
                         "grass")
