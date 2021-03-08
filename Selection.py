"""
User input selection choices
Author: Niklaas Cotta
"""

from CharacterCreation import *
from Race import *
from Class import *


def race_select():
    races = ['Lizard', 'Werepus', 'Monster-a']

    while True:
        print("Pick a race!")

        for i, j in enumerate(races):
            print(f"[{i + 1}]", j)

        choice = int(input('>> '))

        if choice <= len(races):
            # print('You are a', races[choice - 1])
            if choice == 1:
                result = Lizard()
                break
            elif choice == 2:
                result = Werepus()
                break
            elif choice == 3:
                result = MonsterA()
                break
            else:
                print("Unrecognizable, try again.")
                continue

    return result


def class_select():
    classes = ['Brute', 'Monk(ey)', 'Witch Doctor']

    while True:
        print("Pick a class!")

        for i, j in enumerate(classes):
            print(f"[{i + 1}]", j)

        choice = int(input('>> '))

        if choice <= len(classes):
            # print('You are a', classes[choice - 1])
            if choice == 1:
                result = Brute()
                break
            elif choice == 2:
                result = MonkEY()
                break
            elif choice == 3:
                result = WitchDoctor()
                break
            else:
                print("Unrecognizable, try again.")
                continue

    return result


# FIXME: don't need?
def character_selection(name):
    race = race_select()
    myClass = class_select()

    return Character(name, race, myClass, [20, 10])
