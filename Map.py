"""
Moves Class
Author: Niklaas Cotta
"""

import random
import time


# Map
class Map:
    def __init__(self, mapSize):
        """
        Desc: Constructor for map class
        Input: size; how big a map you want, size x size large
        """
        self.layout = []
        self.size = mapSize

    def genLayout(self):
        """
        Desc: Generates map layout
        Input: None
        Output: None
        """
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

                self.layout[row].append(tile)  # cols

                # x and y values of tile
                tile.x = col
                tile.y = row

    def printMap(self):
        """
        Desc: Prints map out row by row
        Input: None
        Output: None
        """
        for row in range(self.size):
            print("\n")
            for col in range(self.size):
                time.sleep(1 / self.size)
                tileImage = self.layout[row][col].appearance
                print(tileImage, end='     ')

    def returnPlayer(self):
        """
        Desc: Finds player in map
        Input: None
        Output: tuple x,y coords
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.layout[row][col].name == "Player":
                    return col, row

    def placePlayer(self, coords):
        x, y = coords
        for row in range(self.size):
            for col in range(self.size):
                if (row == y) and (col == x):
                    self.layout[row][col] = Character()
                    player = self.layout[row][col]
                    player.x = col
                    player.y = row


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
        row1, row2 = tile2.y, tile1.y
        col1, col2 = tile2.x, tile1.x

        return col1, row1  # return new coords

    def getDest(self, direction, coords, layout):
        col, row = coords
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
    # Generate map and get start position
    size = 5
    myMap = Map(size)
    myMap.genLayout()
    playerStart = (myMap.size//2, myMap.size-1)

    while size != 0:
        # Place player tile then print map out
        print("\n==============================================")
        myMap.placePlayer(playerStart)
        myMap.printMap()

        # Movement
        turnMove = Movement()
        dest = turnMove.getDest(1, playerStart, myMap.layout)
        # print("Player Position: ", playerStart)
        playerCol, playerRow = playerStart
        playerStart = turnMove.swapTile2D(myMap.layout[playerRow][playerCol], dest, myMap.layout)
        size -= 1
