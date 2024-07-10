## HERMIT HUT ##

## Contains all forks from investigation of plants and hermit hut area
## Paragraphs 25 - 47

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
        paragraph_29() #enter hut
    elif choice_para_25 == "2":
        paragraph_45() #continue down path
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
    player.decrease_skill(skill_points) # lose skill points due to encumberment
    para_27_text = """You are unable to break free from the vines. You must now fight the plant while
encumbered (Lose 2 skill points for this battle)

Mutant Plant: Skill 4, Stamina 10
"""
    print(para_27_text)
    encounter_enemy(mutant_plant)
    if player.stamina >0:
        player.increase_skill(skill_points)
        paragraph_28() #plant defeated
    else:
        game_over() #player death
        
def paragraph_28(): #plant dead, find hut
    clear_screen()
    para_28_text = """Stumbling away from the dead vines, you continue on your way. You see a small building 
on the edge of the field. As you get close, you realise it is a small hut.

Enter the hut (press 1 {para 29})

Continue on your way (press 2 {para 30})
"""
    print(para_28_text)
    choice_para_28 = input("Make a choice and press Enter: ")
    if choice_para_28 == "1":
        paragraph_29() #enter hut
    elif choice_para_28 == "2":
        paragraph_30() #continue on way
    else:
        paragraph_28()
        
def paragraph_29(): #enter hut
    clear_screen()
    healing = 4
    player.heal_damage(healing)
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
        paragraph_31() #rest
    elif choice_para_29 == "2":
        paragraph_30() #leave hut
    else:
        paragraph_29()
        
def paragraph_30(): #continue on your way (leave hermit hut)
    clear_screen()
    para_30_text = """You politely decline his offer and prepare to leave. As you turn to go, however,
you sense movement behind you. The hermit attacks you, trying to knock you out with a heavy blow to 
the head. 
Do you manage to avoid the attack?
Press any key to continue...
 """
    print(para_30_text)
    msvcrt.getch()
    luck_test = roll_dice()
    if luck_test <= player.luck:
        paragraph_33() #lucky
    else:
        global save_inventory
        global save_gold
        global save_potions
        lose_skill = 4
        player.decrease_skill(lose_skill)
        save_inventory = player.inventory.get_items() #save inventory contents to variable
        save_gold = player.gold
        player.gold = 0
        save_potions = player.health_potions
        player.health_potions = 0
        player.inventory.clear() #clears inventory
        paragraph_32() #unlucky

def paragraph_31(): #rest in hut
    clear_screen()
    global save_inventory
    global save_gold
    global save_potions
    lose_skill = 4
    player.decrease_skill(lose_skill)
    save_inventory = player.inventory.get_items() #save inventory contents to variable
    save_gold = player.gold
    player.gold = 0
    save_potions = player.health_potions
    player.health_potions = 0
    player.inventory.clear() #clears inventory
    para_31_text = """The hermit offers you a warm drink and you gladly accept. After, you begin to 
feel unusually drowsy. As you struggle to keep your eyes open, you realize that you've been drugged. 
"""
    print(para_31_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_32()
    
def paragraph_32(): #wake up in larder
    clear_screen()
    para_32_text = """You wake up groggily, your head throbbing from the hermit's blow. As your vision 
clears, you realize you are bound and lying on a cold stone floor. All your possessions are gone 
including your sword (lose 4 skill points) The room smells of decay, and you see a butchers block and 
various cuts of meat hanging from hooks around the room. Horrified, you begin to realise that you are 
in some sort of larder.

Do you test your luck and try to break your bonds? (press 1 {para 35 for lucky roll, 46 for unlucky})

Or look around the room for something to help you? (press 2 {para 36})
"""
    print(para_32_text)
    choice_para_32 = input("Make a choice and press Enter: ")
    if choice_para_32 == "1":
        luck_test = roll_dice()
        if luck_test <= player.luck:
            skill_regain = 2
            player.increase_skill(skill_regain)
            paragraph_35() # lucky
        else:
            game_over_butchered() #unlucky
    elif choice_para_32 == "2":
        skill_regain = 2
        player.increase_skill(skill_regain)
        paragraph_36() #look for something to help you
    else:
        paragraph_32()
        
def paragraph_33(): # lucky - dodge hermit attack
    clear_screen()
    para_33_text = """You manage to dodge the hermit's attack just in time, causing him to stumble. 
Seizing the opportunity, you swiftly retaliate. 

Fight the hermit:

Hermit: Skill 5, Stamina 12
"""
    print(para_33_text)
    encounter_enemy(hermit)
    if player.stamina >0:
        paragraph_34() #hermit defeated
    else:
        game_over() #player death

def paragraph_34():
    clear_screen()
    gold = 5
    player.add_gold(5)
    item = "Sleep Potion"
    player.inventory.add_item(item)
    para_34_text = """After a fierce struggle, you manage to overpower and kill the hermit. Searching 
his cabin for anything of use, you find 5 gold coins and a vial of sleep potion. You take them with you 
and leave the hermit's cabin. You continue on your way.
"""
    print(para_34_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_45()
    
        
def paragraph_35(): #test bonds and get free
    clear_screen()
    para_35_text = """With determination, you manage to loosen the ropes binding you. Free at last, you 
look around the larder for a weapon and find a sharp cleaver. (2 skill points regained) You carefully exit 
the larder onto a dirt tunnel which leads up. You keep alert any sight or sound of the hermit.
As you reach the tunnel exit, you come to another door. You can hear the hermit gleefully singing to 
himself in a strange tongue.

Do you open the door carefully? press 1 {para 37})

Or kick it open and prepare to fight? (press 2 {para 38})
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
    clear_screen()
    para_36_text = """Looking around you see a sharp piece of bone within reach. Shuffling towards it, 
you manage to use it to cut yourself free. You look around the larder for a weapon and find a sharp 
cleaver. (regain 2 skill points). You carefully exit the larder onto a dirt tunnel which leads up. You keep 
alert any sight or sound of the hermit. As you reach the tunnel exit, you come to another door. You can
hear the hermit gleefully singing to himself in a strange tongue.

Do you open the door carefully? (press 1 {para 37}

Or kick it open and prepare to fight? (press 2 {para 38}
"""
    print(para_36_text)
    print(f"TESTING skill should be 6 {player.skill}")
    choice_para_36 = input("Make a choice and press Enter: ")
    if choice_para_36 == "1":
        paragraph_37() #open door carefully
    elif choice_para_36 == "2":
        paragraph_38() #kick door open
    else:
        paragraph_36() 

def paragraph_37():
    clear_screen()
    para_37_text = """The door opens without a sound. You see the hermit stood over a cooking point. He is 
still singing gleefully to himself.

Do you sneak up on him and attack (press 1 {para 39})

Or quietly leave the hut (press 2 {para 40})
"""
    print(para_37_text)
    choice_para_37 = input("Make a choice and press Enter: ")
    if choice_para_37 == "1":
        paragraph_39() #sneak up and attack
    elif choice_para_37 == "2":
        paragraph_40() # leave the hut quietly
    else:
        paragraph_37()

def paragraph_38(): #kick door open fight hermit
    clear_screen()
    para_38_text = """The hermit jumps as you kick the door open, but recovers quickly, leaping at 
you, brandishing a sharp knife. 

Hermit: Skill 5, Stamina 12
"""
    encounter_enemy(hermit)
    if player.stamina >0:
        paragraph_43()
    else:
        game_over()
        
def paragraph_39():
    clear_screen()
    global save_inventory
    global save_gold
    global save_potions
    gold = 5
    potion = 1
    damage = 2
    player.take_damage(damage)
    para_39_text = """You hit the hermit heavily in the neck with the cleaver. He screams, knocking 
the cooking pot to the floor. It takes a second hit to kill him but not before he slashes you with 
the knife he was holding. (lose 2 stamina). In your weakened state, you were unable to stop the 
knife slashing you across the throat. You bleed out beside him.
"""
    para_39_text_1 = f"""You hit the hermit heavily in the neck with the cleaver. He screams, knocking 
the cooking pot to the floor. It takes a second hit to kill him but not before he slashes you with the 
knife he was holding. (lose 2 stamina).
Finally safe, you take your time to search through the hut, taking care to avoid the spilled cooking 
pot whose contents look suspiciously human. You find your sword sitting by the door. You discard the 
meat cleaver and take it in your hand again (Regain another 2 skill points) In a wooden chest you find 
the rest of your belongings as well as a Health Potion and 5 gold. 

You take stock of your injuries and consider whether you need a health potion.

Current Health: {player.stamina}
"""

    para_39_text_2 = """Do you drink a health potion? (press 1)

Or leave the hut and continue on your way? (press 2)

"""
    if player.stamina <=0:
        print(para_39_text)
        print("Press any key to continue...")
        msvcrt.getch()
        game_over() #player death
    else:
        print(para_39_text_1)
        print(para_39_text_2)
        for item in save_inventory:
            player.inventory.add_item(item)
        player.gold += save_gold + gold
        player.health_potions += save_potions + potion
        skill_increase = 2
        player.increase_skill(skill_increase)
        choice_para_39 = input("Make a choice and press Enter: ")
        if choice_para_39 == "1":
            paragraph_44()
        elif choice_para_39 == "2":
            paragraph_46()
        else:
            paragraph_39()      
        
def paragraph_40():
    clear_screen()
    para_40_text = """You quietly move to the other side of the room and open the door to the outside world, 
hoping the hermit does not notice you.
"""
    print(para_40_text)
    print("Press any key to continue...")
    msvcrt.getch()
    result = roll_dice()
    if result <= player.luck:
        paragraph_41() #lucky
    else: 
        paragraph_42() #unlucky
        
def paragraph_41():
    clear_screen()
    item = "Meat Cleaver"
    player.inventory.add_item(item)
    para_41_text = """You manage to leave the hut without the hermit noticing you. You bemoan the loss of your 
    sword and other possessions but at least you are alive and still have the Meat Cleaver as a makeshift
    weapon. (Meat Cleaver is added to your inventory)
"""
    print(para_41_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_45()

def paragraph_42(): #unlucky, hermit hears you
    clear_screen()
    para_42_text = """The hut door groans, making the hermit turn round. He immediately attacks you.
    
Hermit skill 6 stamina 18
"""
    print(para_42_text)
    encounter_enemy(hermit)
    if player.stamina > 0:
        paragraph_43()
    else:
        game_over()

def paragraph_43(): #hermit dead, get possessions back, leave hut
    clear_screen()
    global save_inventory
    global save_gold
    global save_potions
    for item in save_inventory:
        player.inventory.add_item(item)
    player.gold += save_gold
    player.health_potions += save_potions
    skill_increase = 2
    player.increase_skill(skill_increase)
    para_43_text = """With the hermit safely dead, you discard the cleaver and take the time to locate 
your possessions before leaving the hut.
"""
    print(para_43_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_45()
    
def paragraph_44():
    clear_screen()
    restore_health = 6
    remove_potion = 1
    para_44_text = """You decide to drink a health potion to restore your health (6 stamina restored).
Feeling much better, you leave the hut and your experience with the hermit behind you.
"""
    print(para_44_text)
    print(f"TESTING: stamina before: {player.stamina}")
    player.heal_damage(restore_health)
    player.subtract_health_potions(remove_potion)
    print(f"TESTING stamina after {player.stamina}")
    print("Press any key to continue...")
    print(f"testing potions {player.health_potions}")
    msvcrt.getch()
    paragraph_45()


def paragraph_45():
    pass #temporary placement - new area after the hermit encounter section

def paragraph_46():
    clear_screen()
    para_46_text = """You decide against drinking a Health Potion at this time. You leave the hut
and your experience with the hermit behind you.
"""
    print(para_46_text)
    print("Press any key to continue... ")
    msvcrt.getch()
    paragraph_45()
        
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



