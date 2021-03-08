"""
A Text-Based Adventure Game
Author: Niklaas Cotta
Last Updated: 2/16
"""

# TODO:
# Not sure

import time
from DiceRoll import *


########################################################################################################################
class Race:
    def __init__(self, name, passive, hp, attack, inventory=None):
        """
        Desc: Class for character's race
        Inputs: name; str, name of race
                passive; str, passive of race
                hp; int, number of hitpoints
                attack; int, hp dealt per attack
                inventory; list, a list of items in inventory
        Outputs: none
        """
        if inventory is None:
            inventory = []

        self.name = name
        self.attack = attack
        self.passive = passive
        self.hp = hp
        self.inventory = inventory

    def fight(self, enemy):
        """
        Desc: Fight sequence between two race objects
        Inputs: enemy; a Race object that the character (self) will battle
        Outputs: none
        """
        time.sleep(2)
        print("An attack!")
        options = ['Attack', 'Run']
        options2 = ['attacked', 'tried to run']

        print(f"{self.name}\t\tVS\t\t{enemy.name}")

        while (self.hp > 0) and (enemy.hp > 0):
            print(f"Your HP: {self.hp}\t\tEnemy HP: {enemy.hp}\n")

            # enemy turn. for now, attacks automatically
            self.hp -= enemy.attack

            # check if self defeated
            if self.hp <= 0:
                print("You've lost the battle! :(")
                print("Game OVER")
                exit()

            # your turn
            for i, j in enumerate(options):
                print(f"[{i + 1}]", j)

            choice = int(input('\nWhat will you do? '))
            print(f"{self.name} {options2[choice - 1]}")

            if choice == 2:
                escape = (random.randint(0, 100) > 25)

                if escape:
                    print('You ran away successfully!\n')
                    break
                else:
                    print('Escape unsuccessful!\n')
                    continue

            enemy.hp -= self.attack

            # check if opponent defeated
            if enemy.hp <= 0:
                print("You've won the battle!")
                break

            self.ability()
            enemy.ability()


class Lizard(Race):
    def __init__(self, name, passive, hp, attack):
        """
        Desc: Lizard class, inherits from race
        Inputs: name; str, name of race
                passive; str, passive of race
                hp; int, number of hitpoints
                attack; int, hp dealt per attack
        Outputs: none
        """
        super().__init__(name, passive, hp, attack)

        self.name = 'Lizardman'
        self.passive = 'Regrowth'
        self.hp = 20
        self.attack = 4

    def ability(self):
        """
        Desc: Lizard race's ability. "Regenerate"
        Inputs: none
        Outputs: none
        """
        if 0 < self.hp <= 18:
            self.hp += 2


class Werepus(Race):
    def __init__(self, name, passive, hp, attack):
        """
        Desc: Werepus class, inherits from race
        Inputs: name; str, name of race
                passive; str, passive of race
                hp; int, number of hitpoints
                attack; int, hp dealt per attack
        Outputs: none
        """
        super().__init__(name, passive, hp, attack)

        self.name = 'Werepus'
        self.passive = 'Were am I'
        self.hp = 15
        self.attack = 3

    def ability(self):
        """
        Desc: Werepus' race's ability. "Savage"
        Inputs: none
        Outputs: none
        """
        if self.attack < 8:
            self.attack += 1


########################################################################################################################
########################################################################################################################
def start_menu():
    """
    Desc: Function that prints out the start menu, main hub of menu
    Inputs: none
    Outputs: none
    """
    print("==========================================================================================")
    print("Greetings. This is a text-based adventure game created by Niklaas Cotta. Hope you enjoy ;)")
    print("==========================================================================================")
    time.sleep(0.5)

    options = ['Begin', 'Test dice roll', 'Quit']
    while True:

        for i, j in enumerate(options):
            print(f"[{i + 1}]", j)

        choice = int(input(''))

        time.sleep(0.5)
        if choice == 1:
            print("Good luck adventurer")
            # race_select()
            break
        elif choice == 2:
            diceRoll()  # from DiceRoll.py
        elif choice == 3:
            print("Farewell!")
            exit()
        else:
            continue


########################################################################################################################

if __name__ == '__main__':
    # start the game
    start_menu()
    player = Lizard('Lizard', 'Regrowth', 10, 5)
    opponent = Werepus('Werepus', 'Were am I', 15, 3)
    player.info()
    player.fight(opponent)
