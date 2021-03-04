"""
Class Program
Author: Niklaas Cotta
"""


class MyClass:
    def __init__(self, name):
        self.name = name


class Brute(MyClass):
    def __init__(self):
        super().__init__("Brute")


class MonkEY(MyClass):
    def __init__(self):
        super().__init__("Monk(ey)")


class WitchDoctor(MyClass):
    def __init__(self):
        super().__init__("Witch Doctor")
