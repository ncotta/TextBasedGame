"""{1: Character("Dummy", Dummy(self.stats), None, self.stats, Dummy(self.stats).movesList),
     2: Character("Hulking Dummy", Dummy([12, 12, 12]), None, [12, 12, 12], Dummy([12, 12, 12]).movesList),
     3: Character("Blighted Rose", MonsterA(self.stats), None, self.stats, MonsterA(self.stats).movesList),
     4: Character("Hall Monitor", Lizard(self.stats), None, self.stats, Lizard(self.stats).movesList),
     5: Character("Cuddlefish", Werepus(self.stats), None, self.stats, Lizard(self.stats).movesList)}"""


from Race import *


# Stats generation
def randomStats():
    strength = random.randint(8, 12)
    defense = random.randint(8, 12)
    speed = random.randint(8, 12)

    return [strength, defense, speed]


# Race generation
stats = randomStats()
races = [Dummy(stats), MonsterA(stats), Lizard(stats), Werepus(stats)]

# Name generation
prefixDummy = ["Overgrown", "Rotted", "Cursed"]
prefixMonsterA = ["Blighted", "Withered", "Diseased"]
prefixLizard = ["Hulking", "Spiny", "Rabid"]
prefixWerepus = ["Violent", "Cruel", "Malicious"]

# Moves lists
movesDummy = [Splinter(), Hammer(), Retaliate(), DoNothing()]
movesMonsterA = [Thorns(), Spit(), Root(), Absorb()]
movesLizard = [Rake(), Crunch(), Slam(), Regrowth()]
movesWerepus = [Poison(), Wrap(), Tentacle(), Psywave()]


def randomRace():
    randNum = random.randint(0, 3)
    race = races[randNum]
    return race


def randomClass():
    # prolly want to fix sometime
    return None


def randomName(race):
    randNum = random.randint(0, 2)
    if race.name == "Dummy":
        prefix = prefixDummy[randNum]
    elif race.name == "Monster-a":
        prefix = prefixMonsterA[randNum]
    elif race.name == "Lizard":
        prefix = prefixLizard[randNum]
    else:  # race is Werepus
        prefix = prefixWerepus[randNum]

    name = prefix + " " + race.name
    return name


def randomMoves(race):
    n = random.randint(1, 4)
    if race.name == "Dummy":
        movesList = movesDummy
    elif race.name == "Monster-a":
        movesList = movesMonsterA
    elif race.name == "Lizard":
        movesList = movesLizard
    else:  # race is Werepus
        movesList = movesWerepus

    return random.sample(movesList, n)


# Debugging
if __name__ == '__main__':
    testRace = randomRace()
    testName = randomName(testRace)
    testMoves = randomMoves(testRace)
    print(testName)
    print(testRace.statsList)
    [print(move.name, end=', ') for move in testMoves]

