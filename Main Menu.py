"""
Bringing it all together
Author: Niklaas Cotta
"""

import time
from CharacterCreation import *
from DiceRoll import *
# from Help import *


def title():
    time.sleep(2)
    print("========================================\n")
    time.sleep(0.2)
    print("               ", end='')
    delay_print("NIK'S GAME")
    print("\n")
    print("========================================\n")

    time.sleep(1)


def menu():
    while True:
        options = ["Start", "Test Dice", "Help", "Quit"]
        for i, j in enumerate(options):
            print(f"[{i + 1}]", j)

        choice = input(">> ")
        try:
            choice = int(choice)
            if not (1 <= choice <= 4):
                print("Invalid option. Please try again.")
                menu()

        except ValueError:
            print("Invalid option. Please try again.")
            menu()

        if choice == 1:  # Start
            game()

        elif choice == 2:  # Dice roll
            diceRoll()
            continue

        elif choice == 3:  # Help
            # helpOptions()
            print("Implement later")  # FIXME
            continue

        elif choice == 4:  # Quit
            exit()


def game():
    characterObject = Character.get_input()
    characterObject.info()

    enemyObject = getEnemy()
    charStatus = Fight(characterObject, enemyObject).battle()

    if charStatus == "LOST":
        exit()
    else:  # ran away or won the battle
        print("\n")
        print("========================================")
        time.sleep(0.2)
        print("               ", end='')
        delay_print("YOU WIN!!")
        print("========================================")


def getEnemy():
    randEnemy = random.randint(1, 3)

    if randEnemy == 1:  # Lizard
        stats = [12, 10, 8]
        enemyName = "Red Lizard"
        enemyRace = Lizard(stats)
    elif randEnemy == 2:  # Werepus
        stats = [8, 12, 10]
        enemyName = "Rotten Werepus"
        enemyRace = Werepus(stats)
    else:  # MonsterA
        stats = [10, 8, 12]
        enemyName = "Wilted MonsterA"
        enemyRace = MonsterA(stats)

    randClass = random.randint(1, 3)

    if randClass == 1:  # Brute
        enemyClass = Brute(stats)
    elif randClass == 2:  # MonkEY
        enemyClass = MonkEY(stats)
    else:  # WitchDoctor
        enemyClass = WitchDoctor(stats)

    extraMoves = [Splash(), Loaf()]
    enemyMoves = enemyRace.movesList + extraMoves

    return Character(enemyName, enemyRace, enemyClass, stats, enemyMoves)




if __name__ == '__main__':
    title()
    menu()
