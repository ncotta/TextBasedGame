"""
User input selection choices
Author: Niklaas Cotta
"""

from Race import *
from Class import *


class Selection:
    def __init__(self, statsList=None):
        self.statsList = statsList

    def race_select(self):
        races = ['Lizard', 'Werepus', 'Monster-a']
        result = None

        while True:
            print("Pick a race!")

            for i, j in enumerate(races):
                print(f"[{i + 1}]", j)

            choice = int(input('>> '))

            if choice <= len(races):
                # print('You are a', races[choice - 1])
                if choice == 1:
                    self.statsList = [12, 10, 8]
                    result = Lizard(self.statsList)
                    break
                elif choice == 2:
                    self.statsList = [8, 12, 10]
                    result = Werepus(self.statsList)
                    break
                elif choice == 3:
                    self.statsList = [10, 8, 12]
                    result = MonsterA(self.statsList)
                    break
                else:
                    print("Unrecognizable, try again.")
                    continue

        return result

    def class_select(self):
        classes = ['Brute', 'Monk(ey)', 'Witch Doctor']
        result = None

        while True:
            print("Pick a class!")

            for i, j in enumerate(classes):
                print(f"[{i + 1}]", j)

            choice = int(input('>> '))

            if choice <= len(classes):
                # print('You are a', classes[choice - 1])
                if choice == 1:
                    result = Brute(self.statsList)
                    break
                elif choice == 2:
                    result = MonkEY(self.statsList)
                    break
                elif choice == 3:
                    result = WitchDoctor(self.statsList)
                    break
                else:
                    print("Unrecognizable, try again.")
                    continue

        return result

    def character_selection(self, name):
        pass
