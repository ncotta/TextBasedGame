"""
A Text-Based Adventure Game
Author: Niklaas Cotta
"""

import random


def diceChoices(dice):
    """
    Desc: Helper function for diceRoll(), wanted to get rid of some clutter
    Inputs: dice; the corresponding D'x' dice you want to roll
    Outputs: int
    """
    dices = {
        1: random.randint(1, 20),  # D20
        2: random.randint(1, 12),  # D12
        3: random.randint(1, 10),  # D10
        4: random.randint(1, 8),  # D8
        5: random.randint(1, 6),  # D6
        6: random.randint(1, 4),  # D4
        7: random.randint(1, 2)  # coin!
    }

    return dices[dice]


def diceRoll():
    """
    Desc: Main dice rolling function. Can choose 7 different options.
          Comes with nifty user input
    Inputs: None
    Outputs: None
    """
    diceList = ['D20,', 'D12', 'D10', 'D8', 'D6', 'D4', 'D2']

    while True:
        for i, j in enumerate(diceList):
            print(f"[{i + 1}]", j)

        choice = int(input('What dice would you like to use?'))
        if not (1 <= choice <= 7):
            print("Invalid option. Please try again.")
            pass

        result = diceChoices(choice)
        print('Rolling the dice!')
        print('You rolled a ', choice, ' and got a: ', result)

        dice_next = input('Roll again?\n'
                          '[1] Yes\n'
                          '[2] No\n')

        if not (dice_next == '1'):
            break  # quit


if __name__ == '__main__':
    diceRoll()
