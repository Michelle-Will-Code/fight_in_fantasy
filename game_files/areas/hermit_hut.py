## HERMIT HUT ##

## Contains all the forks/choice between different areas of the forest. This module acts as the link between different 'Dungeons'

## Imported Modules ##

from game_files.game_components.utilities import *
from game_files.game_components.combat import *
from game_files.areas.endings import *
from game_files.game_components.enemies import *
from game_files.game_components.player import *

## Global variables ## 
save_inventory = []
save_potions = 0
save_gold = 0

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
        
def paragraph_26(): # plant attack - lucky
    clear_screen()
    para_26_text = """You manage to break free from the mutant plant's grasp.
    
Mutant Plant: Skill 4, Stamina 10
"""
    print(para_26_text)
    encounter_enemy(mutant_plant)
    if player.stamina > 0:
        paragraph_28() # mutant plant defeated
    else:
        game_over() #player death
    

    
def paragraph_27(): #plant attack - unlucky
    clear_screen()
    skill_points = 2
    player.decrease_skill(skill_points)
    para_27_text = """You are unable to break free from the vines. You must now fight the plant while
encumbered (Lose 2 skill points for this battle)

Mutant Plant: Skill 4, Stamina 10
"""
    print(para_27_text)
    encounter_enemy(mutant_plant)
    if player.stamina >0:
        player.increase_skill(skill_points)
        paragraph_28()
    else:
        game_over()
        
def paragraph_28():
    print("defeated plant")

        
def paragraph_29(): #enter hut
    clear_screen()
    healing = 4
    para_29_text = """Inside the hut, you find an old hermit who offers to heal your wounds. (Restore 
4 Stamina points. You take the time to check your inventory:

"""
    para_29_text_2 = """
The hermit offers his home to you to rest a while before continuing your journey.

Do you rest? (press 1 {para 31})

Or continue on your way? (press 2 {para 30})
"""
    print(para_29_text)
    player.heal_damage(healing)
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
        
def paragraph_30(): #continue on your way (leave hermit hut)
    print("Continue on your way")

def paragraph_31(): #rest in hut
    clear_screen()
    para_31_text = """The hermit offers you a warm drink and you gladly accept. After, you begin to 
feel unusually drowsy. As you struggle to keep your eyes open, you realize that you've been drugged. 
"""
    print(para_31_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_32()
    
def paragraph_32(): #wake up in larder
    global save_inventory
    global save_gold
    global save_potions
    clear_screen()
    lose_skill = 4
    player.decrease_skill(lose_skill)
    save_inventory = player.inventory.get_items() #save inventory contents to variable
    save_gold = player.gold
    player.gold = 0
    save_potions = player.health_potions
    player.health_potions = 0
    player.inventory.clear() #clears inventory
    para_32_text = """You wake up groggily, your head throbbing from the hermit's blow. As your vision 
clears, you realize you are bound and lying on a cold stone floor. All your possessions are gone 
including your sword (lose 4 skill points) The room smells of decay, and you see a butchers block and 
various cuts of meat hanging from hooks around the room. Horrified, you begin to realise that you are 
in some sort of larder.

Do you test your luck and try to break your bonds? (press 1 {para 35 for lucky roll, 46 for unlucky})

Or look around the room for something to help you? (press 2 {para 36})
"""
    print(para_32_text)
    ###TEST SECTION. REMOVE WHEN CONFIRMED WORKING ###
    print(f"TESTING Player gold {player.gold}, player potions {player.health_potions}, inventory {player.inventory.show_inventory()}")
    ###END OF TEST SECTION ###
    choice_para_32 = input("Make a choice and press Enter: ")
    if choice_para_32 == "1":
        result = roll_dice()
        if result <= player.luck:
            paragraph_35()
        else:
            paragraph_46()
    elif choice_para_32 == "2":
        paragraph_36()
    else:
        paragraph_32()
        
def paragraph_35(): #test bonds and get free
    clear_screen()
    skill_increase = 2
    player.increase_skill(skill_increase)
    para_35_text = """With determination, you manage to loosen the ropes binding you. Free at last, you 
look around the larder for a weapon and find a sharp cleaver. (add 2 skill points) You carefully exit 
the larder onto a dirt tunnel which leads up. You keep alert any sight or sound of the hermit.
As you reach the tunnel exit, you come to another door. You can hear the hermit gleefully singing to 
himself in a strange tongue.

Do you open the door carefully? 37

Or kick it open and prepare to fight? 38
"""
    print(para_35_text)
    choice_para_35 = input("Make a choice and press Enter:")
    if choice_para_35 == "1":
        paragraph_37()
    elif choice_para_35 == "2":
        paragraph_38()
    else:
        paragraph_35()

def paragraph_36():
    pass  

def paragraph_37():
    pass

def paragraph_38(): #kick door open fight hermit
    clear_screen()
    para_38_text = """The hermit jumps as you kick the door open, but recovers quickly, leaping at 
you, brandishing a sharp knife. 

Hermit: Skill 5, Stamina 14
"""
    encounter_enemy(hermit)
    if player.stamina >0:
        paragraph_43()
    else:
        game_over()

def paragraph_43(): #hermit dead, get possessions back, leave hut
    global save_inventory
    global save_gold
    global save_potions
    for item in save_inventory:
        player.inventory.add_item(item)
    player.gold += save_gold
    player.health_potions += save_potions
    skill_increase = 2
    player.increase_skill(skill_increase)
    clear_screen()
    para_43_text = """With the hermit dead, you discard the cleaver and take the time to locate your 
possessions before leaving the hut.
"""
    print(para_43_text)
    ##TESTIG CODE ###
    print(f"Testing restoration works: gold {player.gold} potions {player.health_potions} inventory {player.inventory.show_inventory()}")
    ##end of test code
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_45()


def paragraph_45():
    pass #temporary placement - new area after the hermit encounter section

def paragraph_46():
    pass
        
def paragraph_47(): #approach plants
    clear_screen()
    para_47_text = """As you approach the glowing plants, they suddenly come to life, wrapping their
vines around you!

"""
    print(para_47_text)
    print("Press any key to continue...")
    msvcrt.getch()
    result = roll_dice()
    if result <= player.luck:
        paragraph_26()
    else: 
        paragraph_27()



