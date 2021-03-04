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


class Acrobat(MyClass):
    def __init__(self):
        super().__init__("Acrobat")


class Magician(MyClass):
    def __init__(self):
        super().__init__("Magician")
