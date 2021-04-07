"""
Character Creator Program
Author: Niklaas Cotta
"""

from DelayPrint import *
from Selection import *
from Battle import *
import time


class Character:
    def __init__(self, name, charRace, charClass, stats, movesList, inventory=None):
        self.name = name
        self.myRace = charRace
        self.myClass = charClass
        self.attack = stats[0]  # attack
        self.defense = stats[1]  # defense
        self.speed = stats[2]  # speed
        self.movesList = movesList
        if inventory is None:
            inventory = []

        self.inventory = inventory
        self.hp = 20

    def info(self):
        time.sleep(1)
        print('\n======= Character Info =======')
        time.sleep(0.5)
        delay_print(f"Hello, {self.name}\n")
        time.sleep(0.5)
        self.myRace.queryLooks()
        self.myClass.queryLooks()
        time.sleep(0.5)
        print(f"You are a {self.myRace.name}, and a {self.myClass.name} to boot!\n")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}\n")
        time.sleep(1.5)

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
            classObj.statsList,  # stats
            raceObj.movesList  # moves
        )


if __name__ == '__main__':
    characterObj = Character.get_input()
    characterObj.info()
    print("")
    stats = [10, 10, 10]
    enemyRace = Dummy(stats)
    enemyObj = Character("Dummy", enemyRace, None, stats, enemyRace.movesList)
    enemyObj.hp = 10
    battle = Fight(characterObj, enemyObj).battle()

    # print(characterObj.inventory)
