"""
Battle instance
Author: Niklaas Cotta
"""

import random


class Fight:
    def __init__(self, char, enemy):
        self.yourSpeed = char.speed
        self.yourHP = char.hp
        self.enemySpeed = enemy.speed
        self.enemyHP = enemy.hp
        # self.yourMoves = char.moves
        self.yourMoves = ["Rake", "Claw", "Bite"]
        # self.enemyMoves = enemy.moves
        self.enemyMoves = ["Rake", "Claw", "Bite"]
        print(f"A {enemy.name} attacks!")

    def order(self):
        youFirst = self.yourSpeed >= self.enemySpeed

        if youFirst:
            self.choices()
            self.enemyAttack()

        else:
            self.enemyAttack()
            self.choices()

    def choices(self):  # Two choices, attack or run away
        escape = False

        while not escape and (self.yourHP > 0) and (self.enemyHP > 0):  # FIXME
            print("What are you going to do?")

            print("[1] Attack",
                  "[2] Run")

            choice = int(input('>> '))

            if choice == 1:
                self.yourAttack()
                break
            elif choice == 2:
                escape = self.run()
            else:
                print("You can't do that!")
                continue

    def yourAttack(self):
        while True:
            print("What move would you like to use?")

            for i, j in enumerate(self.yourMoves):
                print(f"[{i + 1}]", j)

            choice = int(input(">> "))

            print("You used a move!")
            break

    def enemyAttack(self):
        enemyChoice = random.randint(0, 3)
        print("The enemy attacks!")

        return self.enemyMoves[enemyChoice - 1]

    def run(self):
        escape = (random.randint(0, 100) > 25)

        if escape:
            print('You ran away successfully!\n')
        else:
            print('Escape unsuccessful!\n')

        return escape


class Move:
    def __init__(self, name, attack, effect=None):
        self.name = name
        self.attack = attack
        self.effect = effect

    def critical(self):
        critHit = (random.randint(0, 100) > 90)  # 10%

        if critHit:
            self.attack *= 1.5


class Rake(Move):
    def __init__(self):
        super().__init__("Rake", 5)
