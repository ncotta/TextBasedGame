"""
Battle instance
Author: Niklaas Cotta
"""

import random
from Moves import *


class Fight:
    def __init__(self, char, enemy):
        self.yourSpeed = char.speed
        self.yourHP = char.hp
        self.enemySpeed = enemy.speed
        self.enemyHP = enemy.hp
        # self.yourMoves = char.moves
        self.yourMoves = char.movesList
        # self.enemyMoves = enemy.moves
        self.enemyMoves = enemy.movesList
        print(f"A {enemy.name} attacks!")

    def battle(self):
        result = "LOST"

        youFirst = self.yourSpeed >= self.enemySpeed

        if not youFirst:
            print("The enemy caught you off-guard!")

        while (self.yourHP > 0) and (self.enemyHP > 0):
            print("======================")
            print(f"Your HP: {self.yourHP}")
            print(f"Enemy HP: {self.enemyHP}")
            print("======================")

            if youFirst:  # FIXME: can cut down some if statements
                escaped = self.yourTurn()
                if escaped:
                    result = "RAN"
                    break

                if self.enemyHP <= 0:
                    print("Enemy HP is 0!")
                    print("You've won the battle!")
                    result = "WON"
                    break

                self.enemyAttack()

                if self.yourHP <= 0:
                    print("Your HP is 0!")
                    print("You've lost the battle! :(")
                    print("Game OVER")
                    break

            else:
                self.enemyAttack()

                if self.yourHP <= 0:
                    print("Your HP is 0!")
                    print("You've lost the battle! :(")
                    print("Game OVER")
                    break

                escaped = self.yourTurn()
                if escaped:
                    result = "RAN"
                    break

                if self.enemyHP <= 0:
                    print("Enemy HP is 0!")
                    print("You've won the battle!")
                    result = "WON"
                    break

        return result

    def yourTurn(self):
        escaped = False

        while True:
            print("What are you going to do?")

            print("[1] Attack",
                  "[2] Run")

            choice = int(input('>> '))

            if choice == 1:
                self.yourAttack()
                break
            elif choice == 2:
                escaped = self.run()
                break
            else:
                print("You can't do that!")
                continue

        return escaped

    def yourAttack(self):
        while True:
            print("What move would you like to use?")

            for i, j in enumerate(self.yourMoves):
                print(f"[{i + 1}]", j.name)

            choice = int(input(">> "))

            print(f"You used {self.yourMoves[choice - 1].name}")

            if self.yourMoves[choice - 1].tag == "enemy":
                self.enemyHP -= self.yourMoves[choice - 1].damage
            else:  # tag is self
                self.yourHP -= self.yourMoves[choice - 1].damage

            break

        return self.yourMoves[choice - 1]

    def enemyAttack(self):
        enemyChoice = random.randint(0, len(self.enemyMoves))
        if self.enemyMoves[enemyChoice - 1].tag == "enemy":
            self.yourHP -= self.enemyMoves[enemyChoice - 1].damage
        else:  # tag is self
            self.enemyHP -= self.enemyMoves[enemyChoice - 1].damage

        print(f"The enemy uses {self.enemyMoves[enemyChoice - 1].name}")

        return self.enemyMoves[enemyChoice - 1]

    def run(self):
        escape = (random.randint(0, 100) > 75)  # 25% chance

        if escape:
            print('You ran away successfully!\n')
        else:
            print('Escape unsuccessful!\n')

        return escape
