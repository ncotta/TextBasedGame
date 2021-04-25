"""
Moves Class
Author: Niklaas Cotta
"""

import random
import time


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

    def printMap(self):
        for row in range(self.size):
            print("\n")
            for col in range(self.size):
                time.sleep(1/self.size)
                print(self.layout[row][col].appearance, end='     ')


class Tile:
    def __init__(self):
        pass


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


if __name__ == '__main__':
    myMap = Map(5)
    myMap.printMap()
