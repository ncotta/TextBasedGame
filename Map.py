"""
Moves Class
Author: Niklaas Cotta
"""

import random
import time
from CharacterCreation import *


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
        """
        Desc: Places player in map
        Input: coords you want to place player
        Output: None
        """
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
        """
        Desc: Constructor for Tile class, gets x, y value
        Input: None
        """
        self.x = None
        self.y = None

    def printCoords(self):
        print("X: " + self.x + "Y: " + self.y)


class Character(Tile):  # Player Tile
    def __init__(self):
        super().__init__()
        self.appearance = "<>"
        self.name = "Player"
        self.encounterChance = 0


class Grass(Tile):  # Grasslands
    def __init__(self):
        super().__init__()
        self.appearance = "wW"
        self.name = "Grassland"
        self.encounterChance = 15


class Mountain(Tile):  # Mountains
    def __init__(self):
        super().__init__()
        self.appearance = "//"
        self.name = "Mountains"
        self.encounterChance = 25


class Water(Tile):  # Water
    def __init__(self):
        super().__init__()
        self.appearance = "()"
        self.name = "Lake"
        self.encounterChance = 5


# Encounters
class Encounter:
    def __init__(self, character, defStats=None):
        if defStats is None:
            defStats = [10, 10, 10]

        self.character = character
        self.stats = defStats
        self.encounterMap = {1: Character("Dummy", Dummy(self.stats), None, self.stats, Dummy(self.stats).movesList),
                             2: Character("Hulking Dummy", Dummy([12, 12, 12]), None, [12, 12, 12], Dummy([12, 12, 12]).movesList),
                             3: Character("Blighted Rose", MonsterA(self.stats), None, self.stats, MonsterA(self.stats).movesList),
                             4: Character("Hall Monitor", Lizard(self.stats), None, self.stats, Lizard(self.stats).movesList),
                             5: Character("Cuddlefish", Werepus(self.stats), None, self.stats, Lizard(self.stats).movesList)}

    def startBattle(self):
        enemy = self.encounterMap[random.randint(1, 5)]
        mapBattle = Fight(self.character, enemy).battle()


# Map movement
class Movement:
    def __init__(self):
        """
        Desc: Constructor for a movement, moveSpeed = how many tiles per turn
        Input: None
        """
        self.moveSpeed = 1  # Navigate one tile

    def swapTile2D(self, tile1, tile2, layout):
        """
        Desc: Swaps two tile objects in a 2D list
        Input: tile1; first tile to swap
               tile2; tile to swap with first
               layout; the 2D list you want tiles swapped in
        Output: tuple, returns new coords of tile1
        """
        row1 = tile1.y
        col1 = tile1.x

        row2 = tile2.y
        col2 = tile2.x
        # Swap actual layout in map
        layout[row1][col1], layout[row2][col2] = layout[row2][col2], layout[row1][col1]
        row1, row2 = tile2.y, tile1.y  # swap y coord
        col1, col2 = tile2.x, tile1.x  # swap x coord

        return col1, row1  # return new coords

    def getDest(self, direction, coords, layout):
        """
        Desc: Get destination of where tile is going
        Input: direction; up (1), down (2), right (3), left (4)
               coords; coords of tile you're moving
               layout; 2d list you're using
        Output: tuple, destination tile
        """
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
