## Main File ##

## Imported Modules ##

import random
import msvcrt
from combat import *
from player import *
from utilities import *
from enemies import *
from endings import *
from tree_dungeon_area import *

## Global Variables ##

inventory = ["Rope", "Flint"]

################ START GAME AND GAME OVER ################
#        
def start_game(): #start of the game
    clear_screen()
    global inventory

    start = f"""The Forest of Morrowfield Adventure Game!
    
STARTING STATS         INVENTORY
Skill: {player.skill}               Gold: {player.gold}
Stamina: {player.stamina}            Health Potions: {player.health_potions}
Luck: {player.luck}                Bag: {inventory}
    
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

############### PARAGRAPHS ###################

def paragraph_1(): #dense trees and a noise
    clear_screen()
    para_1_text = """The forest is dense, with tall trees blocking out most of the sunlight. You
follow a narrow path when you hear rustling in the bushes.

Do you investigate the noise? (type 1 {para 2})

Or do you continue along the path? (type 2 {para 23})

"""

    print(para_1_text)
    choice_para_1 = input("Make a choice and press Enter: ")
    if choice_para_1 == "1":
        paragraph_2()
    elif choice_para_1 == "2":
        paragraph_23()
    else:
        paragraph_1() #investigate noise

def paragraph_2(): #goblin encounter
    clear_screen()
    para_2_text = """You cautiously approach the source of the noise. Suddenly a goblin leaps
out at you!

Goblin: Skill 5, Stamina 10
"""
    print(para_2_text)
    encounter_enemy(goblin)
    if player.stamina > 0:
        paragraph_4() # goblin defeated
    else:
        game_over() #player death
               
def paragraph_4(): #goblin defeat, tree with door
    player.add_gold(5)
    clear_screen()
    para_4_text = """The goblin falls at your feet. Searching its body, you find a small pouch of
gold coins. (5 coins are added to your inventory) Continuing forward, you come to a large
twisted tree with a door carved into its trunk. 

Do you enter the tree? (press 1 {para_3})

Or do you continue down the path (press 2 {para 20}
"""
    print(para_4_text)
    choice_para_4 = input("Make a choice and press Enter: ")
    if choice_para_4 == "1":
        paragraph_3() #enter the tree
    elif choice_para_4 == "2":
        paragraph_20()
    else:
        paragraph_4()

def paragraph_20(): #continue down the path, leaving tree behind
    clear_screen()
    print("paragraph 20")
    
def paragraph_23():
    para_23_text = """You decide to ignore the noise and quickly and quietly pass it by.Continuing forward, you come to a 
large twisted tree with a door carved into its trunk. 

Do you enter the tree? (press 1 {para_3})

Or do you continue down the path (press 2 {para 20}
"""
    print(para_23_text)
    choice_para_23 = input("Make a choice and press Enter: ")
    if choice_para_23 == "1":
        paragraph_3() #enter the tree
    elif choice_para_23 == "2":
        paragraph_20() #continue down the path
    else:
        paragraph_23()   

############### MAIN PROGRAM ##################

###start_game()##
#ignoring this for now as we will be testing from para_20()
#
paragraph_20()        
