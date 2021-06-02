"""
Bringing it all together
Author: Niklaas Cotta
"""

from DiceRoll import *
from Story import *
from CharacterCreation import *


class GameLoop:
    def __init__(self):
        self.characterObject = None

    def createPlayer(self):
        characterObject = Character.generatePlayer()
        characterObject.info()

        self.characterObject = characterObject

    def title(self):
        time.sleep(2)
        delay_print("========================================\n", 0.025)
        time.sleep(0.2)
        print("               ", end='')
        delay_print("MY GAME", 0.25)
        print("\n")
        delay_print("========================================\n", 0.025)

        time.sleep(1)

    def menu(self):
        while True:
            options = ["Start", "Test Dice", "Help", "Quit"]
            enum_delay(options)

            choice = checkChoice(options, self.menu)

            if choice == 1:  # Start
                self.game()

            elif choice == 2:  # Dice roll
                diceRoll()
                continue

            elif choice == 3:  # Help
                # helpOptions()
                print("Not available :(")
                continue

            elif choice == 4:  # Quit
                exit()

    def game(self):
        rows = 5
        cols = 5
        myMap = Map(rows, cols)
        myMap.genLayout()
        playerStart = (myMap.cols // 2, myMap.rows - 1)

        # Create Character
        self.createPlayer()

        newStory = Prison(self.characterObject)
        newStory.title()
        newStory.step0()

        options = ["Continue", "Pause"]

        enum_delay(options)
        userIn = input(">> ")
        if userIn == "1":
            print("===============()===============", end='')
            i = 1
            while True:
                # Place player tile then print map out
                myMap.placePlayer(playerStart)
                myMap.printMap()
                print("\n")
                if i == 1:
                    myMap.printTerrain()
                    print("\n")
                    i = 0
                directions = ["North", "South", "East", "West"]
                enum_delay(directions)

                try:
                    userDir = int(input(">> "))

                except ValueError:
                    print("Invalid input!")
                    continue

                # Movement
                turnMove = Movement()
                dest = turnMove.getDest(userDir, playerStart, myMap)
                # print("Player Position: ", playerStart)
                playerCol, playerRow = playerStart
                playerStart = turnMove.swapTile2D(myMap.layout[playerRow][playerCol], dest, myMap.layout)
                n = random.randint(0, 100)
                print("\n===============()===============")
                if n < dest.encounterChance:  # fix encounter chance lol
                    print("\n A WILD ENEMY APPEARS!! ")
                    Encounter(self.characterObject).startBattle()

            # delay_print("\n       THE END        \n")

        exit()


if __name__ == '__main__':
    game = GameLoop()
    game.title()
    game.menu()
