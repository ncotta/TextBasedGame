"""
User input selection choices
Author: Niklaas Cotta
"""

from CharacterCreation import *


def race_select():
    races = ['Lizard', 'Werepus', 'Monster-a']

    while True:
        for i, j in enumerate(races):
            print(f"[{i + 1}]", j)

        choice = int(input('Pick a race: '))

        if choice <= len(races):
            print('You are a', races[choice - 1])
            if choice == '0':
                result = Lizard()
                break
            elif choice == '1':
                result = Werepus()
                break
            else:
                result = MonsterA()
                break

    return result


def class_select():
    classes = ['Brute', 'Monk(ey)', 'Witch Doctor']

    while True:
        for i, j in enumerate(classes):
            print(f"[{i + 1}]", j)

        choice = int(input('Pick a class: '))

        if choice <= len(classes):
            print('You are a', classes[choice - 1])
            if choice == '0':
                result = Brute()
                break
            elif choice == '1':
                result = MonkEY()
                break
            else:
                result = WitchDoctor()
                break

    return result


def character_selection():
    race = race_select()
    myClass = class_select()

    Character(race, myClass, [20, 10])  # FIXME
