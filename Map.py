"""
Moves Class
Author: Niklaas Cotta
"""

import random
import time


# Map
class Map:
    def __init__(self, size, layout=None):
        if layout is None:
            self.layout = []  # Grid of NxN tiles
        self.size = size

        for row in range(self.size):
            self.layout.append([])
            for col in range(self.size):
                tileChance = random.randint(1, 10)
                if tileChance <= 7:  # 70%
                    tile = Grass()
                elif 8 <= tileChance <= 9:  # 20%
                    tile = Mountain()
                else:  # 10%
                    tile = Water()

                self.layout[row].append(tile)
                tile.x = row
                tile.y = col

        # Character gen
        oldTile = self.layout[-1][(self.size // 2)]
        player = Character(oldTile)
        self.layout[-1][(self.size // 2)] = player
        player.x = oldTile.x
        player.y = oldTile.y

    def printMap(self):
        for row in range(self.size):
            print("\n")
            for col in range(self.size):
                time.sleep(1 / self.size)
                print(self.layout[row][col].appearance, end='     ')

    def returnPlayer(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.layout[row][col].appearance == "<>":
                    return row, col


# Tiles
class Tile:
    def __init__(self):
        self.x = None
        self.y = None

    def printCoords(self):
        print("X: " + self.x + "Y: " + self.y)


class Character(Tile):
    def __init__(self, tile):
        super().__init__()
        self.appearance = "<>"
        self.name = "Player"
        self.stored = tile.appearance[:]


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
        self.sourceAppearance = None

    def movePlayer(self, direction, source):  # FIXME, doesn't actually update tile :(
        if direction == 1:  # North
            source.x -= self.moveSpeed
        elif direction == 2:  # South
            source.x += self.moveSpeed
        elif direction == 3:  # East
            source.y += self.moveSpeed
        elif direction == 4:  # West
            source.y -= self.moveSpeed


if __name__ == '__main__':
    myMap = Map(5)
    while True:
        print("\n==============================================")
        myMap.printMap()
        movement = Movement()
        x, y = myMap.returnPlayer()
        movement.movePlayer(1, myMap.layout[x][y])
