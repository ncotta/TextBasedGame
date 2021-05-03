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
        """
        Desc: Constructor for a Character object (self and enemy)
        Input: name; a string that you want the character to be named
               charRace; the race instance of the character
               charClass; the class instance of the character
               stats; list of attack, defense, speed numbers
               movesList; a list of move objects
               inventory; a list of items the character possesses, None by default
        """
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
        """
        Desc: Prints out some general info of your character
        Input: None
        Output: None
        """
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
        """
        Desc: Class method, creates a character and fills in parameters with user input when called
        Input: None
        Output: Character() instance
        """
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
    # TODO: combine with Map.py main
    characterObj = Character.get_input()
    characterObj.info()
    print("")
    stats = [10, 10, 10]
    enemyRace = Dummy(stats)
    enemyObj = Character("Dummy", enemyRace, None, stats, enemyRace.movesList)
    enemyObj.hp = 10
    battle = Fight(characterObj, enemyObj).battle()

    # print(characterObj.inventory)
