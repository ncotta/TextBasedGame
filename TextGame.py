"""
A Text-Based Adventure Game
Author: Niklaas Cotta
Last Updated: 2/16
"""

# TODO:
# Not sure

import time
import random


def dice_roll_helper(dice):
    """
    Desc: A helper function for the dice roll
    Inputs: dice; a str to determine which dice to roll
    Outputs: int
    """
    print("Rolling the dice!")

    time.sleep(0.5)
    dices = {
        1: random.randint(1, 20),  # D20
        2: random.randint(1, 12),  # D12
        3: random.randint(1, 10),  # D10
        4: random.randint(1, 8),  # D8
        5: random.randint(1, 6),  # D6
        6: random.randint(1, 4),  # D4
        7: random.randint(1, 2)  # D2
    }
    print("You rolled the dice and got a:", dices[dice])

    return dices[dice]


def dice_roll():
    """
    Desc: Contains logic for rolling specified dice
    Inputs: none
    Outputs: none
    """
    dice_choices = ['D20', 'D12', 'D10', 'D8', 'D6', 'D4', 'D2']

    while True:
        for i, j in enumerate(dice_choices):
            print(f"[{i + 1}]", j)

        choice = int(input('What dice would you like to use?:'))
        dice_roll_helper(choice)
        time.sleep(0.5)
        dice_next = input("Roll again?\n"
                          "[1] Yes\n"
                          "[2] No")

        if dice_next == "1":
            continue
        else:
            break


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

    def info(self):
        """
        Desc: print function for race information
        Inputs: none
        Outputs: none
        """
        print('\n======= Character Info =======')
        print(f"Race: {self.name}")
        print(f"Passive: {self.passive}")
        print(f"Max HP: {self.hp}")
        print(f"Attack: {self.attack}\n")

    @classmethod
    def get_race(cls, name):
        """
        Desc: gets the race from user input and creates race object. kinda messy, could clean up
        Inputs: name; str, the name of the race
        Outputs: (function)
        """
        attributes = {'Lizard': {'passive': 'Regrowth', 'hp': 20, 'attack': 4},
                      'Werepus': {'passive': 'Were am I', 'hp': 15, 'attack': 3}
                      }

        return cls(name, attributes[name]['passive'], attributes[name]['hp'], attributes[name]['attack'])

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

            self.ability() # FIXME
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
        super().__init__(name, passive, hp, attack)  # FIXME

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
        super().__init__(name, passive, hp, attack)  # FIXME

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
def race_select():
    """
    Desc: Function for user to choose desired race
    Inputs: none
    Outputs: none
    """
    races = ['Lizard', 'Werepus']
    race_map = {'Lizard': Lizard, 'Werepus': Werepus}

    while True:
        for i, j in enumerate(races):
            print(f"[{i + 1}]", j)

        choice = int(input('Pick a race:'))

        if choice <= len(races):
            print('You are a', races[choice - 1])
            race_initializer = race_map.get(races[choice - 1], None)
            character = race_initializer.get_race(races[choice - 1])
            return character
        else:
            continue


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
            dice_roll()
        elif choice == 3:
            print("Farewell!")
            exit()
        else:
            continue


########################################################################################################################
def opening():
    pass


if __name__ == '__main__':
    # start the game
    start_menu()
    player = race_select()
    opponent = Werepus('Werepus', 'Were am I', 15, 3)
    player.info()
    player.fight(opponent)
