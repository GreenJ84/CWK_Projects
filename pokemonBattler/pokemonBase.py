import random
import time
from battleMoves import *

class Pokemon:
    def __init__(self, name, species, element, weakeness, resistance, moveSet):
    # name
    # species
    # element
    # weakness
    # resistance
    # moves
        self.health = random.randint(115,150)
        self.baseHealth = self.health
        self.attack = random.randint(80,115)
        self.defense = random.randint(80,115)
        self.speed = random.randint(80,115)
        self.name = name
        self.species = species
        self.element = element
        self.weakness = weakeness
        self.resistance = resistance
        self.moveSet = moveSet # Move class

    def battle(myPokemon, enemyPokemon):
        prompt = True
        while prompt:
            myMove = input(f"\nChose your attack: { ' - '.join([m.name for m in myPokemon.moveSet])}\n") # string
            if myMove == myPokemon.moveSet[0].name:
                myMove = myPokemon.moveSet[0] # Move object
            elif myMove == myPokemon.moveSet[1].name:
                myMove = myPokemon.moveSet[1]
            else:
                print("Invalid move choice")
                continue
            prompt = False

        enemyMove = random.choice(enemyPokemon.moveSet)

        print('\n')

        if myPokemon.speed > enemyPokemon.speed:
            enemyPokemon.calculateDamage(myPokemon, myMove)
            if enemyPokemon.health > 0:
                myPokemon.calculateDamage(enemyPokemon, enemyMove)
                if myPokemon.health <= 0:
                    print(f"\nMy pokemon, {myPokemon.name} has fainted")
                    return [False, enemyPokemon]
            else:
                print(f"\nEnemy pokemon, {enemyPokemon.name} has fainted")
                return [False, myPokemon]

        else:
            myPokemon.calculateDamage(enemyPokemon, enemyMove)
            if myPokemon.health > 0:
                enemyPokemon.calculateDamage(myPokemon, myMove)
                if enemyPokemon.health <= 0:
                    print(f"\nEnemy pokemon, {enemyPokemon.name} has fainted")
                    return [False, myPokemon]
            else:
                print(f"\nMy pokemon, {myPokemon.name} has fainted")
                return [False, enemyPokemon]

        time.sleep(2)
        print('\n')
        print(f"My pokemon, {myPokemon.name} has {round(myPokemon.health, 1)} health left")
        print(f"Enemy pokemon, {enemyPokemon.name} has {round(enemyPokemon.health, 1)} health left")
        return [True, None]


    def calculateDamage(self, attacker, move):
        time.sleep(1)
        STAB = move.STAB
        if move.element in self.weakness:
            print(f"{move.name} was Super Effective on {self.name}")
            typeEffect = 2
        elif move.element in self.resistance:
            print(f"{move.name} was not Effective on {self.name}")
            typeEffect = .5
        else:
            print(f"{move.name} was Effective on {self.name}")
            typeEffect = 1

        randMod = random.uniform(0.85, 1.0)
        crit = random.randint(1,2)
        atkMod = STAB * typeEffect * crit * randMod
        defense = self.defense
        attack = attacker.attack

        damage = ((0.44) * (attack/defense) * move.basePower + 2) * atkMod
        self.health -= damage

# ===============   ELEMENTS ===========================
# Grass
class Grass(Pokemon): # Pokemon -> SuperClass / Grass -> SubClass
    def __init__(self, name, species, moveSet):
        Pokemon.__init__(self, name, species, "Grass", "Fire", ["Water", "Grass"], moveSet)


# Water
class Water(Pokemon):
    def __init__(self, name, species, moveSet):
        Pokemon.__init__(self, name, species, "Water", "Grass", ["Fire", "Water"], moveSet)


# Fire
class Fire(Pokemon):
    def __init__(self, name, species, moveSet):
        Pokemon.__init__(self, name, species, "Fire", "Water", ["Grass", "Fire"], moveSet)
