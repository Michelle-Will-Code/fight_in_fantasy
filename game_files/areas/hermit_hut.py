## HERMIT HUT ##

## Contains all the forks/choice between different areas of the forest. This module acts as the link between different 'Dungeons'

## Imported Modules ##

from game_files.game_components.utilities import *
from game_files.game_components.combat import *
from game_files.areas.endings import *
from game_files.game_components.enemies import *
from game_files.game_components.player import *



## Paragraphs ##


               

           

        
def paragraph_25(): #avoid plants
    clear_screen()
    para_25_text = """You wisely avoid the glowing plants and continue around the edge of the field. 
On the other side, you find a small hut. 

Do you enter the hut? (press 1 {para 29}) 

Or continue down the path (press 2 {para 45})?
"""
    print(para_25_text)
    choice_para_25 = input("Make a choice and press Enter: ")
    if choice_para_25 == "1":
        paragraph_29()
    elif choice_para_25 == "2":
        paragraph_45()
    else:
        paragraph_25()
        
def paragraph_26(): # plant attack - unlucky
    para_26_text = """You manage to break free from the mutant plant's grasp.
    
Mutant Plant: Skill 5, Stamina 12
"""
    print(para_26_text)
    encounter_enemy(mutant_plant)
    if player.stamina > 0:
        paragraph_28() # mutant plant defeated
    else:
        game_over() #player death
    

    
def paragraph_27(): #plant attack - unlucky
    skill_points = 3
    player.decrease_skill(skill_points)
    para_27_text = """You are unable to break free from the vines. You must now fight the plant while
encumbered (Lose 3 skill points for this battle)

Mutant Plant: Skill 5, Stamina 12
"""
    print(para_27_text)
    encounter_enemy(mutant_plant)
    if player.stamina >0:
        player.increase_skill(skill_points)
        paragraph_28()
    else:
        game_over()
        
def paragraph_28():
    pass

        
def paragraph_29():
    clear_screen()
    para_29_text = """Inside the hut, you find an old hermit who offers to heal your wounds. (Restore 
4 Stamina points. You take the time to check your inventory:

"""
    para_29_text_2 = """
The hermit offers his home to you to rest a while before continuing your journey.

Do you rest? (press 1 {para 31})

Or continue on your way? (press 2 {para 30})
"""
    print(para_29_text)
    print(f"Inventory: {player.inventory.show_inventory()}")
    print(f"Health Potions: {player.health_potions}")
    print(f"Gold: {player.gold}")
    
    print(para_29_text_2)
    choice_para_29 = input("Make a choice and press Enter: ")
    if choice_para_29 == "1":
        paragraph_31()
    elif choice_para_29 == "2":
        paragraph_30()
    else:
        paragraph_29()
        
def paragraph_30():
    print("Continue on your way")

def paragraph_31():
    print("Rest")

def paragraph_45():
    pass #temporary placement - new area after the hermit encounter section
        
def paragraph_47():
    clear_screen()
    para_47_text = """As you approach the glowing plants, they suddenly come to life, wrapping their
vines around you!
"""
    print(para_47_text)
    result = roll_dice()
    if result < player.luck:
        paragraph_26()
    else: 
        paragraph_27()



