"""
Class Program
Author: Niklaas Cotta
"""


class MyClass:
    def __init__(self, name, appearance, statsList):
        self.name = name
        self.appearance = appearance
        self.statsList = statsList

    def queryLooks(self):
        print(f"{self.appearance}")


class Brute(MyClass):
    def __init__(self, statsList):
        super().__init__("Brute", "Your arms are corded with muscles, with a wicked-looking greataxe slung behind "
                         "your back.", statsList)

        statsList[0] += 2


class MonkEY(MyClass):
    def __init__(self, statsList):
        super().__init__("Monk(ey)",
                         "As one of the monks from beyond the Great Eastern Sea, your unique fighting style usually "
                         "involves flinging poo", statsList)

        statsList[2] += 2


class WitchDoctor(MyClass):
    def __init__(self, statsList):
        super().__init__("Witch Doctor",
                         "Dark and mysterious, are you a witch or are you a doctor? No one knows...well, except you",
                         statsList)

        statsList[1] += 2
