# Gloabl imports
import random
import time
from pokemonBase import *
from pokemonSelection import *

# Global Variables
myHP = 0
enemyHP = 0

def main():
    global myHP, enemyHP

    
    play = True
    while play:

        # Character Selection Stage
        options = ["Bulbasaur", "Squirtle", "Charmander"]
        myTeam = []
        while len(myTeam) < 3:
            print(f"\nAvailable Pokemon:\n {' - '.join(options)}")
            type = input("\nChoose your pokemon's type\n").lower()
            name = input("Choose your pokemon's name\n")

            if type == "bulbasaur":
                myTeam.append(Bulbasaur(name))

            elif type == "squirtle":
                myTeam.append(Squirtle(name))
                
            elif type == "charmander":
                myTeam.append(Charmander(name))
            
            else:
                print("Invalid Option provided")
                continue

            options.remove(type[:1].upper()+type[1:])

            enemyTeam = getAll()

        for poke in myTeam:
            myHP += poke.health

        for poke in enemyTeam:
            enemyHP += poke.health

        print('\n')
        print(f"I currently have an HP of {round(myHP, 1)}")
        print(f"I currently fight with {myTeam[0].name}, {myTeam[1].name}, and {myTeam[2].name}\n")

        print(f"Enemy currently has an HP of {round(enemyHP, 1)}")
        print(f"They fight with {enemyTeam[0].name}, {enemyTeam[1].name}, and {enemyTeam[2].name}\n")


        myPokemon = random.choice(myTeam)
        enemyPokemon = random.choice(enemyTeam)
        while len(myTeam) > 0 and len(enemyTeam) > 0:

            fight = True
            while fight:
                [fight, winner] = Pokemon.battle(myPokemon, enemyPokemon)

                time.sleep(2)
                if not fight:
                    if winner == myPokemon:
                        enemyTeam.remove(enemyPokemon)
                        enemyHP -= enemyPokemon.baseHealth
                        print(f"{enemyPokemon.name} has fallen in battle. Enemy has lost {enemyPokemon.baseHealth} health")

                        if len(enemyTeam) > 0:
                            enemyPokemon = random.choice(enemyTeam)
                            fight = True
                    
                    else:
                        myTeam.remove(myPokemon)
                        myHP -= myPokemon.baseHealth
                        print(f"{myPokemon.name} has fallen in battle. You have lost {myPokemon.baseHealth} health")

                        if len(myTeam) > 0:
                            myPokemon = random.choice(myTeam)
                            fight = True
            
            time.sleep(2)
            if len(myTeam) > 0:
                print(f"You have won the battle with {' - '.join([m.name for m in myTeam])} surviving")
            else:
                print(f"You have lost the battle with {' - '.join([m.name for m in myTeam])} beating you")

        restart = input("Do you want to play again? Y/N \n")
        if restart == "n" or restart == "no":
            play = False



if __name__ == "__main__": # Process running
    main()

# poke = p.getRandomPokemon()
# print(poke.name, poke.health, poke.attack, poke.defense)
# for move in poke.moveSet:
#   print(f"{move.name} - {move.basePower}")