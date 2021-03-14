"""
Character Creator Program
Author: Niklaas Cotta
"""

from Selection import *
from Battle import *


class Character:
    def __init__(self, name, charRace, charClass, stats, inventory=None):
        self.name = name
        self.myRace = charRace
        self.myClass = charClass
        self.attack = stats[0]
        self.defense = stats[1]
        self.speed = stats[2]
        if inventory is None:
            inventory = []

        self.inventory = inventory
        self.hp = 20

    def info(self):
        print('\n======= Character Info =======')
        print(f"Hello, {self.name}")
        self.myRace.queryLooks()
        self.myClass.queryLooks()
        print(f"You are a {self.myRace.name}, and a {self.myClass.name} to boot!")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")

    def fight(self, style):
        # getFight = Fight(1v1)
        pass

    @classmethod
    def get_input(cls):
        mySelection = Selection()
        raceObj = mySelection.race_select()
        classObj = mySelection.class_select()
        print("What is your name?\n")

        return cls(
            input(">> "),  # name
            raceObj,  # race choice
            classObj,  # class choice
            classObj.statsList  # stats
        )


if __name__ == '__main__':
    characterObj = Character.get_input()
    characterObj.info()
    test = [10, 10, 10]
    print("")
    enemyObj = Character("Scary boi", Lizard(test), Brute(test), test)
    battle = Fight(characterObj, enemyObj).battle()

    # print(characterObj.inventory)
