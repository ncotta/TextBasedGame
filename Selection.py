"""
User input selection choices
Author: Niklaas Cotta
"""

from DelayPrint import *
from Race import *
from Class import *


class Selection:
    def __init__(self, statsList=None):
        self.statsList = statsList

    def race_select(self):
        # Select a race!
        races = ['Lizard      (very strong, a bit sluggish)', 'Werepus     (very formidable, a bit weak)',
                 'Monster-a   (very fast, a bit fragile)']
        result = None

        while True:
            print("Pick a race!")
            enum_delay(races)

            try:
                choice = int(input(">> "))

            except ValueError:
                print("Invalid input!")
                continue

            if choice <= len(races):  # FIXME: corner cases
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
        # Pick a class!
        classes = ['Brute        (+atk)', 'Monk(ey)     (+spe)', 'Witch Doctor (+def)']
        result = None

        while True:
            print("Pick a class!")

            enum_delay(classes)

            try:
                choice = int(input(">> "))

            except ValueError:
                print("Invalid input!")
                continue

            if choice <= len(classes):
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
