## Main File ##

## Imported Modules ##

from game_files.game_components.player import *
from game_files.game_components.inventory import *
from game_files.areas.forest_area import *

## Global Variables ##

inventory = Inventory()

## START GAME ##
       
def start_game(): #start of the game
    clear_screen()

    start = f"""The Forest of Morrowfield Adventure Game!
    
STARTING STATS         INVENTORY
Skill: {player.skill}               Gold: {player.gold}
Stamina: {player.stamina}            Health Potions: {player.health_potions}
Luck: {player.luck}                Bag: {player.inventory.show_inventory()}


   
You have been tasked with the retrieval of the Dagger of Arkathor which was sealed within
a temple in the centre of the Enchanted Forest of Morrowfield over 100 year ago for its own 
protection. As the days grow closer that this sacred relic will be needed, the Arkathorian 
Council have beseeched their Order of Baruabus to send one of their warriors to retrieve it.
As one of their best, you have been chosen for this task.

You stand at the edge of the forest, studying the ancient trees and discover two faint paths leading in.

Do you take the faint trail that runs between two giant oaks? (type 1 para 1)

Or do you take the other trail that runs amongst thick bushes? (type 2 para UNWRITTEN)

"""
    print(start)
    choice_start_game = input("Make a choice and press Enter: ")
    if choice_start_game == "1":
        paragraph_1()
    elif choice_start_game == "2":
        pass #unwritten
    else:
        start_game()


############### MAIN PROGRAM ##################

start_game()    
