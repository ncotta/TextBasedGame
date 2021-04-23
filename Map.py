"""
Moves Class
Author: Niklaas Cotta
"""

import random


class Map:
    def __init__(self, size, layout=None):
        if layout is None:
            self.layout = []  # Grid of NxN tiles
        self.size = size

        tileDict = {0: "M", 1: "X", 2: "X", 3: "X", 4: "0"}
        for row in range(self.size):
            self.layout.append([])
            for col in range(self.size):
                tileType = tileDict[random.randint(0, 4)]
                tile = Tile(tileType)
                self.layout[row].append(tile)

    def printMap(self):
        for row in range(self.size):
            print("\n")
            for col in range(self.size):
                print(self.layout[row][col].appearance, end='     ')


class Tile:
    def __init__(self, appearance):
        self.appearance = appearance
        # self.name = mountain, water, grass
        # self.encounter_chance = 10, 25, 50
        # class encounter


if __name__ == '__main__':
    myMap = Map(5)
    myMap.printMap()
