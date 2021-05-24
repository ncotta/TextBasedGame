"""
Moves Class
Author: Niklaas Cotta
"""

from Battle import *
import random


# Map
class Map:
    def __init__(self, rows, cols):
        """
        Desc: Constructor for map class
        Input: size; how big a map you want, size x size large
        """
        self.layout = []
        self.rows = rows
        self.cols = cols

    def genLayout(self):
        """
        Desc: Generates map layout
        Input: None
        Output: None
        """
        for row in range(self.rows):
            self.layout.append([])  # rows
            for col in range(self.cols):
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
        for row in range(self.rows):
            print("\n")
            for col in range(self.cols):
                time.sleep(1 / self.rows)
                tileImage = self.layout[row][col].appearance
                print(tileImage, end='     ')

    def printTerrain(self):
        print("Map Key!")
        print("================================")
        terrains = {"[<>]": "This is you!",
                    "[wW]": "Grassy plains",
                    "[//]": "Sparse mountains",
                    "[()]": "Glassy lakes"}
        for i in terrains:
            print(i, terrains[i])

        print("================================")

    def returnPlayer(self):
        """
        Desc: Finds player in map
        Input: None
        Output: tuple x,y coords
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.layout[row][col].name == "Player":
                    return col, row

    def placePlayer(self, coords):
        """
        Desc: Places player in map
        Input: coords you want to place player
        Output: None
        """
        x, y = coords
        for row in range(self.rows):
            for col in range(self.cols):
                if (row == y) and (col == x):
                    self.layout[row][col] = Player()
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


class Player(Tile):  # Player Tile
    def __init__(self):
        super().__init__()
        self.appearance = "<>"
        self.name = "Player"
        self.encounterChance = 0

    @classmethod
    def generatePlayer(cls):
        pass


class Grass(Tile):  # Grasslands
    def __init__(self):
        super().__init__()
        self.appearance = "wW"
        self.name = "Grassland"
        self.encounterChance = 60


class Mountain(Tile):  # Mountains
    def __init__(self):
        super().__init__()
        self.appearance = "//"  # /\
        self.name = "Mountains"
        self.encounterChance = 35


class Water(Tile):  # Water
    def __init__(self):
        super().__init__()
        self.appearance = "()"
        self.name = "Lake"
        self.encounterChance = 10


# Encounters
class Encounter:
    def __init__(self, character):
        self.character = character

    def startBattle(self):
        enemy = self.character.generateEnemy()
        Fight(self.character, enemy).battle()


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

    def getDest(self, direction, coords, myMap):
        """
        Desc: Get destination of where tile is going
        Input: direction; up (1), down (2), right (3), left (4)
               coords; coords of tile you're moving
               layout; 2d list you're using
        Output: tuple, destination tile
        """
        col, row = coords
        if direction == 1:  # North
            if row == 0:  # Top edge
                print("Cannot go any further North!")
            else:
                row -= self.moveSpeed
        elif direction == 2:  # South
            if row == (myMap.rows - 1):  # Bottom edge
                print("Cannot go any further South!")
            else:
                row += self.moveSpeed
        elif direction == 3:  # East
            if col == (myMap.cols - 1):  # Right edge
                print("Cannot go any further East!")
            else:
                col += self.moveSpeed
        elif direction == 4:  # West
            if col == 0:  # Left edge
                print("Cannot go any further West!")
            else:
                col -= self.moveSpeed

        return myMap.layout[row][col]
