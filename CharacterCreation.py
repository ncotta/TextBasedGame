"""
Character Creator Program
Author: Niklaas Cotta
"""

from Race import *
from Class import *


class Character:
    def __init__(self, charRace, charClass, stats, inventory=None):
        self.myRace = charRace
        self.myClass = charClass
        self.attack = stats[0]
        self.defense = stats[1]
        if inventory is None:
            inventory = []

        self.inventory = inventory
        self.maxHP = 20

    def info(self):
        print('\n======= Character Info =======')
        print(f"Race: {self.myRace.name}")
        print(f"Class: {self.myClass.name}")
        print(f"HP: {self.maxHP}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")

    def getInventory(self):
        return self.inventory


if __name__ == '__main__':
    attack = 20
    defense = 10
    testRace = Lizard()
    testClass = Brute()
    characterObj = Character(testRace, testClass, [attack, defense], ["50 gp", "Magic sword"])
    characterObj.info()
