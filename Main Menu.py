"""
Bringing it all together
Author: Niklaas Cotta
"""

from DiceRoll import *
from Map import *


def title():
    time.sleep(2)
    print("========================================\n")
    time.sleep(0.2)
    print("               ", end='')
    delay_print("MY GAME")
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
    size = 5
    myMap = Map(size)
    myMap.genLayout()
    playerStart = (myMap.size // 2, myMap.size - 1)

    # Create Character
    characterObject = Character.generatePlayer()
    characterObject.info()

    print(" [1] Go!\n",
          "[2] Exit")

    userIn = input(">> ")
    if userIn == "1":
        while size != 0:
            # Place player tile then print map out

            myMap.placePlayer(playerStart)
            myMap.printMap()

            # Movement
            turnMove = Movement()
            dest = turnMove.getDest(1, playerStart, myMap.layout)
            # print("Player Position: ", playerStart)
            playerCol, playerRow = playerStart
            playerStart = turnMove.swapTile2D(myMap.layout[playerRow][playerCol], dest, myMap.layout)
            n = random.randint(0, 100)
            print("\n==============================================")
            if n < dest.encounterChance:  # fix encounter chance lol
                print("\n A WILD ENEMY APPEARS!! ")
                Encounter(characterObject).startBattle()
            size -= 1

        delay_print("\n       THE END        \n")

    exit()


if __name__ == '__main__':
    title()
    menu()
