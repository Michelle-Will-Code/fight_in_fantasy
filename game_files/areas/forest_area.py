## FOREST DUNGEON ##

## Contains all the forks/choice between different areas of the forest. This module acts as the link between different 'Dungeons'

## Imported Modules ##

from game_files.game_components.utilities import *
from game_files.game_components.combat import *
from game_files.areas.endings import *
from game_files.game_components.enemies import *
from game_files.areas.tree_dungeon_area import *


## Paragraphs ##

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
