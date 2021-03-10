"""
Character Creator Program
Author: Niklaas Cotta
"""

from Selection import *
import random


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

    def critical(self):
        critHit = (random.randint(0, 100) > 90)  # 10%

        if critHit:
            self.attack *= 1.5  # FIXME: temporary, maybe put in attack class or something

    @classmethod
    def get_input(cls):
        mySelection = Selection()
        raceObj = mySelection.race_select()
        classObj = mySelection.class_select()

        return cls(
            input("What is your name?\n"),  # name
            raceObj,  # race choice
            classObj,  # class choice
            classObj.statsList  # stats
        )

    """
    def fight(self, enemy):
        print(f"{self.name}   VS   {enemy.name}")

        while self.hp > 0 and enemy.hp > 0:
            print(f"Your HP: {self.hp}")
            print(f"Enemy HP: {enemy.hp}")

            if self.speed > enemy.speed:
    """


if __name__ == '__main__':
    characterObj = Character.get_input()
    characterObj.info()
    # print(characterObj.inventory)
