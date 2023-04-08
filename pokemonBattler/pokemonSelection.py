from pokemonBase import *
from battleMoves import *


# ========================== Grass ==========================
class Bulbasaur(Grass):
    def __init__(self, name):
        Grass.__init__(self, name, "Bulbasaur", [Tackle("Grass"), VineWhip("Grass")])


# ========================== Water ==========================
class Squirtle(Water):
    def __init__(self, name):
        Water.__init__(self, name, "Squirtle", [Tackle("Water"), WaterGun("Water")])


# ========================== Fire ==========================
class Charmander(Fire):
    def __init__(self, name):
        Fire.__init__(self, name, "Charmander", [Scratch("Fire"), Ember("Fire")])

def getAll():
    poke = []
    poke.append(Bulbasaur("Bulby"))
    poke.append(Squirtle("Squirt"))
    poke.append(Charmander("Charmy"))
    return poke