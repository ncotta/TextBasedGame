"""
Character Creator Program
Author: Niklaas Cotta
"""

from Race import *
from Class import *


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

    @classmethod
    def get_input(cls):
        raceObj = None
        race = input("What is your race?\n")

        if race == "Lizard":
            raceObj = Lizard()
        elif race == "Werepus":
            raceObj = Werepus()
        elif race == "Monster-a":
            raceObj = MonsterA()
        else:
            print("Unrecognizable")  # FIXME

        classObj = None
        myClass = input("What is your class?\n")

        if myClass == "Brute":
            classObj = Brute()
        elif myClass == "MonkEY":
            classObj = MonkEY()
        elif myClass == "WitchDoctor":
            classObj = WitchDoctor()
        else:
            print("Unrecognizable")  # FIXME

        return cls(
            input("What is your name?\n"),  # name
            raceObj,
            classObj,
            [20, 10, 5]  # stats
        )

    """
    def fight(self, enemy):
        print(f"{self.name}   VS   {enemy.name}")

        while self.hp > 0 and enemy.hp > 0:
            print(f"Your HP: {self.hp}")
            print(f"Enemy HP: {enemy.hp}")

            if self.speed > enemy.speed:
                pass
    """


if __name__ == '__main__':
    """
    attack = 20
    defense = 10
    speed = 5
    inv = ["50 gp", "Magic sword"]
    testRace = Lizard()
    testClass = Brute()
    characterObj = Character("Bobby Schmurda", testRace, testClass, [attack, defense, speed], inv)
    """
    characterObj = Character.get_input()
    characterObj.info()
    # print(characterObj.inventory)
