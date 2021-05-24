"""
Story aspect
Author: Niklaas Cotta
"""

from CharacterCreation import *
from DelayPrint import *


class Chapter:
    def __init__(self, chapName, chapNum, character):
        self.chapName = chapName
        self.chapNum = chapNum
        self.character = character
        self.attack = character.attack

    def story(self):
        pass


class Prison(Chapter):
    def __init__(self, character):
        super().__init__("Prison", 1, character)

    def title(self):
        delay_print(f"Chapter {self.chapNum}: {self.chapName}\n", 0.1)
        delay_print("=======================================================\n", 0.05)
        time.sleep(1)

    def step0(self):
        print("You wake up in a dark prison cell. The only source of light\n"
              "is the remnants of a sputtering torch. You feel an oppressive\n"
              "presence in the darkness.\n")

        options = ["Try the door", "Search for something useful", "Do nothing"]
        enum_delay(options)
        print("=======================================================")

        choice = checkChoice(options, self.step1)

        if choice == 1:
            if self.attack < 12:
                self.step2()
            else:
                self.step3()
        elif choice == 2:
            self.step4()
        else:  # choice == 3
            self.step5()

    def step1(self):
        time.sleep(1.5)
        print("Time ebbs slowly", end='')
        delay_print(". . .", 0.4)
        print("You lose yourself in oblivion for a short while.\n")

        options = ["Try the door", "Search for something useful", "Do nothing"]
        enum_delay(options)
        print("=======================================================")

        choice = checkChoice(options, self.step1)

        if choice == 1:
            if self.attack < 12:
                self.step2()
            else:
                self.step3()
        elif choice == 2:
            self.step4()
        else:  # choice == 3
            self.step5()

    def step2(self):
        time.sleep(1.5)
        print("You grab the handle of the door with a white-knuckled grip\n"
              "and shake it vigorously. The door solemnly refuses your attempts\n"
              "to escape.\n")
        print("=======================================================")
        self.step1()

    def step3(self):
        time.sleep(1.5)
        print("The rusty hinges break away with ease. The dilapidated corridor\n"
              "reeks of filth and mold. Something compels you to the left.")
        print("=======================================================")
        self.step6()

    def step4(self):
        time.sleep(1.5)
        print("You do a thorough job of looking for something that can get you out\n"
              "of this mess. In the process you ruined a decent mattress. Stuffing is\n"
              "strewn across the floor. Your search was in vain and you are feeling\n"
              "a bit grumpy.\n")
        print("=======================================================")
        self.step1()

    def step5(self):
        time.sleep(1.5)
        print("The air begins to tingle. Like the feel of the wind before a\n"
              "roiling thunderstorm. With a flash of brilliant white light\n"
              "and a quiet but persistent buzz in your ears...you suddenly feel\n"
              "a delicate key in your hands.\n")
        print("=======================================================")
        self.step6()

    def step6(self):
        time.sleep(1.5)
        print("The door reluctantly permits your leave. Starting off to the right\n"
              "you slow. You can hear soft moaning and guttural howls far off into\n"
              "the damp recesses behind you. You redouble your pace.")

        print("=======================================================")
        delay_print(". . .", 0.75)

        print("You step outside. The swaying grassy plains and sharp mountains look\n"
              "no more familiar than did the prison")

        print("=======================================================")
        time.sleep(1.5)
