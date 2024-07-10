## TREE DUNGEON AREA ##

# This module contains paragraphs 1 to 24 
# INCLUDES: goblin attack, all tree dungeon area, leaving the area, investigate plants

## Imported Modules ## 
import msvcrt
from game_files.game_components.utilities import *
from game_files.areas.endings import *
from game_files.game_components.combat import *
from game_files.game_components.enemies import *
from game_files.areas.hermit_hut import *

## Paragraphs ### 

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
        
def paragraph_3(): #spiral staircase in tree
    clear_screen()
    para_3_text = """Inside the tree, you find a spiral staircase leading down into darkness. 
    
Do you descend the stairs? (press 1 {para 5}) 

Or leave the tree and continue along the path (press 2 {para 20})? 
"""
    print(para_3_text)
    choice_para_3 = input("Make a choice and press Enter: ")
    if choice_para_3 == "1":
        paragraph_5() #descend stairs
    elif choice_para_3 == "2":
        paragraph_20()
    else:
        paragraph_3()
        
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
        
def paragraph_5():
    clear_screen()
    para_5_text = """The staircase descends into a dimly lit cavern. The air is damp and cold. As you 
reach the bottom, you see an ogre blocking your path. 

Ogre: Skill 7, Stamina 14
"""
    print(para_5_text)
    encounter_enemy(ogre)
    if player.stamina > 0:
        paragraph_6() #ogre defeated
    else:
        game_over() #player death
    
def paragraph_6(): #ogre defeated, take passage or return up stairs
    clear_screen()
    para_6_text = """With the ogre defeated, you find a hidden passage behind a large boulder. 
    
Do you enter the passage? (press 1 {para 7}) 

Or return up the stairs? (press 2 {para_24})
"""
    print(para_6_text)
    choice_para_6 = input("Make your choice and press Enter: ")
    if choice_para_6 == "1":
        paragraph_7() #enter passage
    elif choice_para_6 == "2":
        paragraph_24()
    else:
        paragraph_6()
        
def paragraph_7(): #skeleton encounter
    clear_screen()
    para_7_text = """The hidden passage leads you to a secret chamber filled with treasure! However, 
a guardian skeleton stands in your way.

Skeleton: Skill 6, Stamina 6
"""
    print(para_7_text)
    encounter_enemy(skeleton)
    if player.stamina > 0:
        paragraph_8() #skeleton defeated
    else:
        game_over() #player death

def paragraph_8(): #take gold, look at items
    player.add_gold(20)
    clear_screen()
    para_8_text = """ With the guardian skeleton defeated, you take time to pick through the treasure.
It looks like the remains of a goblin's treasure hoard. Most of it is worn and tarnished with age and 
of little value or too large to take with you, however you are able to pocket 20 gold coins. You do
however find three items small enough that may be of value in your adventure.

    1. A small silver vial
    2. An amulet with a sickly yellow stone
    3. A ring that emits a glow
    
You pick up the vial.
    
Do you take the vial with you? (press 1 {para 9})

Or leave it? (press 2 {para 15})
"""
    print(para_8_text)
    choice_para_8 = input("Make a choice and press Enter: ")
    if choice_para_8 == "1":
        paragraph_9() #take the vial
    elif choice_para_8 == "2":
        paragraph_15() #leave the vial
    else:
        paragraph_8()
        
def paragraph_9(): #examine and pocket the vial. choose amulet or not
    player.inventory.add_item("Holy Elixir") #add Holy Elixir to inventory
    clear_screen()
    para_9_text = """You decide to take the silver vial with you. As you examine it more closely, you 
realize it is filled with holy elixir, a potent substance against evil creatures and curses. (Holy 
Elixir added to inventory)

You look at the amulet next.

Will you take it with you? (press 1 {para 10})

Or will you leave it? (press 2 {para 16})
"""
    print(para_9_text)
    choice_para_9 = input("Make a choice and Press Enter: ")
    if choice_para_9 == "1":
        paragraph_10() #take amulet
    elif choice_para_9 == "2":
        paragraph_16() #leave amulet
    else:
        paragraph_9()
    
def paragraph_10(): #examine and pocket the amulet
    clear_screen()
    para_10_text = """Intrigued by the strange amulet you put it round your neck for safekeeping. As 
soon as you do, you feel suddenly weak and fall to the ground as the amulet burns hot against your 
chest, fusing against your flesh. The amulet is cursed and is draining your life force.

Do you have a Holy Elixir? (Press 1 {para 12})

Or not? (Press 2 {para 13})
""" 
    print(para_10_text)
    choice_para_10 = input("Make a choice and press Enter: ")
    if choice_para_10 == "1":
        paragraph_12() #have holy elixir
    elif choice_para_10 == "2":
        paragraph_13() # dont have holy elixir
    
def paragraph_11(): #examine and pocket the #Ring of Light
    player.inventory.add_item("Ring of Light")
    clear_screen()
    para_11_text = """You pocket the ring and then retrace your steps, finding yourself back outside 
the tree once more. You continue down the path, leaving the tree behind. 
"""
    print(para_11_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()
    
def paragraph_12(): #use Holy Elixir to remove amulet
    clear_screen()
    para_12_text = """In your weakened state you struggle to open the vial of Holy Elixir but through 
sheer determination you unstop the bottle and pour it over the amulet. There is a hissing sound and the 
amulet falls off your chest. You throw it away from you as it turns to dust. You've lost some stamina 
but are otherwise fine.
"""
    para_12_text_1 = """In your weakened state you struggle to open the vial of Holy Elixir but through 
sheer determination you unstop the bottle and pour it over the amulet. There is a hissing sound and the 
amulet falls off your chest but you were already weak from your previous battles. You feel yourself fading.
"""
    if player.inventory.has_item_check("Holy Elixir"):
        player.inventory.remove_item("Holy Elixir")
        damage = 4
        player.take_damage(damage)
        if player.stamina <= 0:
            print(para_12_text_1)
            print("Press any key to continue...")
            msvcrt.getch()
            game_over()
        else:
            print(para_12_text)
            print(f"Your current stats are: \n\n Skill: {player.skill}  Stamina: {player.stamina} Luck: {player.luck}\n\n")
            print("\n Press any key to continue. \n\n")
            msvcrt.getch()
            paragraph_17() #recover from ordeal
    else:
        paragraph_22() # dont have holy elixir

def paragraph_13(): #No holy elixir - calculate survival
    clear_screen()
    para_13_text = """You have no means to fight off this curse except sheer determination. Struggling 
against the weakness, you try slicing the amulet off with your dagger.
"""
    print(para_13_text)
    print("Press any key to continue...")
    msvcrt.getch()
    damage = roll_12_sided_dice()
    player.take_damage(damage)
    if player.stamina <= 0:
        game_over_amulet_death()
    else:
        paragraph_14()

def paragraph_14(): #recover from amulet ordeal (no Holy Elixir)
    clear_screen()
    para_14_text = """Panting with pain, you managed to slice the amulet from your skin and throw it away, 
leaving yourself bleeding, but alive.
"""
    para_14_text_1 = """After taking some time to recover and deal with your injury, you look at the last 
item you found, a ring. This time you examine your find more closely and find etchings along the inside that 
name this the Ring of Light,a useful item for lighting up dark areas.

Do you take the ring? (press 1 {para 11})

Or do you leave it? (press 2 {para 18})
"""
    print(para_14_text)
    print(f"Your current stats are: \n\n Skill: {player.skill}  Stamina: {player.stamina} Luck: {player.luck}\n\n")
    print(para_14_text_1)
    choice_para_14 = input("Make a choice and press Enter: ")
    if choice_para_14 == "1":
        paragraph_11()
    elif choice_para_14 == "2":
        paragraph_18()
    else:
        paragraph_14()
    
    
def paragraph_15(): # leave vial, decide on amulet
    clear_screen()
    para_15_text = """You decide you dont need the vial and take a look at the amulet.

Will you take the amulet with you? (press 1 {para 10})

Or will you leave it? (press 2 {para 16})
"""
    print(para_15_text)
    choice_para_15 = input("Make choice and press Enter: ")
    if choice_para_15 == "1":
        paragraph_10()
    elif choice_para_15 == "2":
        paragraph_16()
    else:
        paragraph_15()
        
def paragraph_16(): #leave amulet
    clear_screen()
    para_16_text = """You dont like the look of the amulet, sensing something dark about it. The leave it alone
and take a look at the ring.

Do you take the ring? (press 1 {para 19})

Or leave it (press 1 {para 21})
"""
    print(para_16_text)
    choice_para_16 = input("Make choice and press Enter: ")
    if choice_para_16 == "1":
        paragraph_19()
    elif choice_para_16 == "2":
        paragraph_21()
    else:
        paragraph_16()

def paragraph_17(): #recover from ordeal (used Holy Elixir)
    clear_screen()
    para_17_text = """You take a few minutes to calm down after your frightening experience, thinking that you 
need to be more careful in future. After taking some time to recover, you look at the last item you found, a 
ring. This time you examine your find more closely and find etchings along the inside that name this the Ring 
of Light,a useful item for lighting up dark areas.

Do you take the ring? (press 1 {para 11})

Or do you leave it? (press 2 {para 18})
"""
    print(para_17_text)
    choice_para_17 = input("Make choice and press Enter: ")
    if choice_para_17 == "1":
        paragraph_11()
    elif choice_para_17 == "2":
        paragraph_18()
    else:
        paragraph_17()  
    
def paragraph_18(): #leave the Ring of Light
    clear_screen()
    para_18_text = """Your experience with the amulet has put you off taking any kind of jewellery with you. 
You leave the ring behind. 
You retrace your steps and find yourself outside the tree once more. You continue down the path, leaving the 
tree behind.
"""
    print(para_18_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()

def paragraph_19(): #take ring and reveal its purpose
    player.inventory.add_item("Ring of Light")
    clear_screen()
    para_19_text = """Upon closer examination of the ring, you find etchings along the inside that name this 
the Ring of Light,a useful item for lighting up dark areas. After pocketing the ring, you retrace your steps 
and find yourself back outside the tree once more. You continue down the path, leaving the tree behind.
"""
    print(para_19_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()  
    
def paragraph_20(): #continue down the path, leaving tree behind
    clear_screen()
    para_20_text = """You continue along the path until you reach a large, open field. In the center 
of the field, you see a patch of strange, glowing plants. 

Do you investigate the plants? (press 1 {para 47}) 

Or skirt around the edge of the field? (press 2 {para 25)
"""
    print(para_20_text)
    choice_para_20 = input("Make a choice and press Enter: ")
    if choice_para_20 == "1":
        paragraph_47()
    elif choice_para_20 == "2":
        paragraph_25()
    else:
        paragraph_20()    
    
def paragraph_21():
    clear_screen()
    para_21_text = """You decide to leave the ring behind. You retrace your steps and find yourself back outside
the tree once more. You continue down the path, leaving the tree behind.
"""
    print(para_21_text)
    print("Press any key to continue ...")
    msvcrt.getch()
    paragraph_20()
    
def paragraph_22():
    clear_screen()
    print("You don't have a Holy Elixir. Press any key to continue...")
    msvcrt.getch()
    paragraph_13()
    
def paragraph_23(): #ignore noise and continue
    clear_screen()
    para_23_text = """You decide to ignore the noise and quickly and quietly pass it by.Continuing 
forward, you come to a large twisted tree with a door carved into its trunk. 

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
    
def paragraph_24():
    clear_screen()
    para_24_text = """You retrace your steps and find yourself back outside the tree once more.
You continue down the path, leaving the tree behind."""
    print(para_24_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()
    
