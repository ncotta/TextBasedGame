"""
Moves Class
Author: Niklaas Cotta
"""

import random
import time


# Map
class Map:
    def __init__(self, size):
        """
        Desc: Sets up map
        Input: size; how big a map you want, size x size large
               layout; nothing for now
        Output: None (creates map)
        """
        self.layout = []
        self.size = size

    def genLayout(self):
        for row in range(self.size):
            self.layout.append([])  # rows
            for col in range(self.size):
                tileChance = random.randint(1, 10)  # different chances for different tiles
                if tileChance <= 7:  # 70%
                    tile = Grass()
                elif 8 <= tileChance <= 9:  # 20%
                    tile = Mountain()
                else:  # 10%
                    tile = Water()

                if (col == (self.size - 1)) and (row == (self.size -1)):
                    tile = Character()

                self.layout[row].append(tile)  # cols

                # x and y values, future use?
                tile.x = col
                tile.y = row

    def printMap(self):
        for row in range(self.size):
            print("\n")
            for col in range(self.size):
                time.sleep(1 / self.size)
                tileImage = self.layout[row][col].appearance
                print(tileImage, end='     ')

    def returnPlayer(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.layout[row][col].name == "Player":
                    return col, row


# Tiles
class Tile:
    def __init__(self):
        self.x = None
        self.y = None

    def printCoords(self):
        print("X: " + self.x + "Y: " + self.y)


class Character(Tile):
    def __init__(self):
        super().__init__()
        self.appearance = "<>"
        self.name = "Player"
        self.encounterChance = 0


class Grass(Tile):
    def __init__(self):
        super().__init__()
        self.appearance = "wW"
        self.name = "Grassland"
        self.encounterChance = 15


class Mountain(Tile):
    def __init__(self):
        super().__init__()
        self.appearance = "//"
        self.name = "Mountains"
        self.encounterChance = 25


class Water(Tile):
    def __init__(self):
        super().__init__()
        self.appearance = "()"
        self.name = "Lake"
        self.encounterChance = 5


# Encounters
class Encounter:
    def __init__(self, enemy):
        self.enemy = enemy


# Map movement
class Movement:
    def __init__(self):
        self.moveSpeed = 1  # Navigate one tile

    def swapTile2D(self, tile1, tile2, layout):
        row1 = tile1.y
        col1 = tile1.x

        row2 = tile2.y
        col2 = tile2.x
        layout[row1][col1], layout[row2][col2] = layout[row2][col2], layout[row1][col1]

    def getDest(self, direction, row, col, layout):
        if direction == 1:  # North
            row -= self.moveSpeed
        elif direction == 2:  # South
            row += self.moveSpeed
        elif direction == 3:  # East
            col += self.moveSpeed
        elif direction == 4:  # West
            col -= self.moveSpeed

        return layout[row][col]


if __name__ == '__main__':
    myMap = Map(5)
    myMap.genLayout()
    while True:
        print("\n==============================================")
        myMap.printMap()
        turnMove = Movement()
        getColPlayer, getRowPlayer = myMap.returnPlayer()
        player = myMap.layout[getRowPlayer][getColPlayer]
        dest = turnMove.getDest(1, getRowPlayer, getColPlayer, myMap.layout)

        turnMove.swapTile2D(player, dest, myMap.layout)

