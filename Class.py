"""
Class Program
Author: Niklaas Cotta
"""


class MyClass:
    def __init__(self, name, appearance):
        self.name = name
        self.appearance = appearance

    def queryLooks(self):
        print(f"{self.appearance}")


class Brute(MyClass):
    def __init__(self):
        super().__init__("Brute",
                         "Your arms are corded with muscles, with a wicked-looking greataxe slung behind your back.")


class MonkEY(MyClass):
    def __init__(self):
        super().__init__("Monk(ey)",
                         "As one of the monks from beyond the Great Eastern Sea, your unique fighting style usually "
                         "involves flinging poo")


class WitchDoctor(MyClass):
    def __init__(self):
        super().__init__("Witch Doctor",
                         "Dark and mysterious, are you a witch or are you a doctor? No one knows...well, except you")
