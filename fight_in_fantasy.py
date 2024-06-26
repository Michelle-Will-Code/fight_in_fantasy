######### imported libraries
import random
import msvcrt

#############SCREEN ADJUSTMENTS#################

def clear_screen():
    print('\033[2J\033[H', end ='')

############ REQUIREMENTS FOR PLAYER ###############

inventory = ["Rope", "Flint"]
health_potions = 2 #restore 5 stamina
purse = 5 #gold

class Player:
    def __init__(self, skill, stamina, luck):
        self.skill = skill
        self.stamina = stamina
        self.luck = luck
    
    def modify_luck(self, amount):
        self.luck += amount
        if self.luck <0:
            self.luck =10
            
    def take_damage(self, damage):
        self.stamina -= damage
        if self.stamina <1:
            self.stamina = 0
    
player = Player(skill=8, stamina=20, luck=6)

############# REQUIREMENTS FOR ENEMIES #################

class Enemy:
    def __init__(self, name, skill, stamina, damage):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.damage = damage
    
    def attack(self):
        return self.damage
        
    def take_damage(self, damage):
        self.stamina -= damage
        if self.stamina <0:
            self.stamina = 0
            
    def is_defeated(self):
        return self.stamina <= 0
        
    def __str__(self):
        return f"{self.name} (Skill: {self.skill}. Stamina: {self.stamina}, Damage: {self.damage})"

goblin = Enemy(name="Goblin", skill=5, stamina=10, damage=5)
sprite = Enemy(name="Sprite", skill=10, stamina=15, damage=7)
mutant_plant = Enemy(name="Mutant Plant", skill=3, stamina=12, damage=6)
ogre = Enemy(name="Ogre", skill=7, stamina=14, damage =10)
skeleton = Enemy(name="skeleton", skill=6, stamina=10, damage=8)
ghoul = Enemy(name="Ghoul", skill=5, stamina=12, damage=9)

encounters = [goblin, sprite, mutant_plant, ogre,skeleton,ghoul]

############## DICE SIMULATIONS ###################

def roll_dice(): #required to simulate a 6 sided dice for combat and luck rolls
    return random.randint(1,6)

def roll_12_sided_dice():
    return random.randint(1,12)

############# COMBAT FUNCTIONS ###################

def calculate_damage(attacker_skill, defender_skill): # damage calculation for combat
    base_damage = 4
    damage = base_damage + (attacker_skill // 2) - (defender_skill // 2)
    return max(1, damage)

def combat(player, enemy): # simulates the traditional turn based dice rolls for combat
    global purse
    print("\nPrepare to fight!")
    while player.stamina >0 and enemy.stamina >0:
        #Player attack
        player_attack_roll = roll_dice() + player.skill + random.randint(-1,1)
        enemy_defense_roll = roll_dice() + enemy.skill + random.randint(-1,1)
        
        if player_attack_roll > enemy_defense_roll:
            damage = calculate_damage(player.skill, enemy.skill)
            enemy.take_damage(damage)
            print(f"You hit the {enemy.name} and dealt {damage} damage.")
        else:
            print(f"The {enemy.name} deflected your hit")
        
        #check if enemy defeated
        if enemy.stamina <=0:
            break
        
        #enemy attack
        enemy_attack_roll = roll_dice() + enemy.skill + random.randint(-1,1)
        player_defense_roll = roll_dice() + player.skill + random.randint(-1,1)
        
        if enemy_attack_roll > player_defense_roll:
            damage = calculate_damage(enemy.skill, player.skill)
            player.take_damage(damage)
            print(f"The {enemy.name} hits you and causes {damage} damage.")
        else:
            print(f"You deflect the {enemy.name}'s attack.")
     
    #check if player defeated
    if player.stamina <= 0:
        print("\nYou have been defeated.")
        return False
        #Could have a def function here for game over
    else:
        print(f"\n\n{enemy.name} is defeated!\n")
        print(f"Your current stats are: \n\n Skill: {player.skill}  Stamina: {player.stamina} Luck: {player.luck}\n\n Gold = {purse}\n")
        print("\nPress any key to continue... ")
        msvcrt.getch()
        return True

def encounter_enemy(enemy): # deals with enemy generation
    result = combat(player, enemy)
    if result:
        print(" ")
    else:
        print(f"You have fallen in battle. The quest is lost.")
        exit(0)
        
################ START GAME AND GAME OVER ################
#        
def start_game(): #start of the game
    clear_screen()
    global purse
    global health_potions
    global inventory

    start = f"""The Forest of Morrowfield Adventure Game!
    
STARTING STATS         INVENTORY
Skill: {player.skill}               Gold: {purse}
Stamina: {player.stamina}            Health Potions: {health_potions}
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
    
def game_over(): #Player Death
    clear_screen()
    print("You succumb to your injuries. Your quest is over.")
    
def game_over_special(): #Player Death based on paralysing enemies
    clear_screen()
    print("The venom of the creature paralyses you. You are powerless as the creature drags you to its lair to feast.")

def game_over_winner():#Completed the game
    pass

def game_over_amulet_death():
    clear_screen()
    amulet_death = """Your attempts to remove the amulet fail, leaving you bleeding out on the ground. Your vision grows 
clouded, then dark. You listen as your heart beat slowly fades. Your adventure is over.
"""
    print(amulet_death)

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
        
def paragraph_3(): #spiral staircase in tree
    clear_screen()
    para_3_text = """Inside the tree, you find a spiral staircase leading down into darkness. 
    
Do you descend the stairs (press 1 {para 5}) 

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
    global purse
    gold = 5
    purse += gold #update gold
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

Or return up the staircase? (press 2 {para_23})
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
    global purse
    gold = 20
    purse += gold #update gold
    clear_screen()
    para_8_text = """ With the guardian skeleton defeated, you take time to pick through the treasure.
It looks like the remains of a goblin's treasure hoard. Most of it is worn and tarnished with age and 
of little value or too large to take with you, however you are able to pocket some gold coins. You do
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
    global inventory
    inventory.append("Holy Elixir") #add Holy Elixir to inventory
    clear_screen()
    para_9_text = """You decide to take the silver vial with you. As you examine it more closely, you 
realize it is filled with holy elixir, a potent substance against evil creatures and curses. (Holy Elixir 
added to inventory)

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
    para_10_text = """Intrigued by the strange amulet you put it round your neck for safekeeping. As soon as
you do, you feel suddenly weak and fall to the ground as the amulet burns hot against your chest, fusing 
against your flesh. The amulet is cursed and is draining your life force.

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
    global inventory
    inventory.append("Ring of Light")
    clear_screen()
    para_11_text = """You pocket the ring and then retrace your steps, finding yourself back outside the tree once
more. You continue down the path, leaving the tree behind. 
"""
    print(para_11_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()
    
def paragraph_12(): #use Holy Elixir to remove amulet
    global inventory
    clear_screen()
    para_12_text = """In your weakened state you struggle to open the vial of Holy Elixir but through sheer 
determination you unstop the bottle and pour it over the amulet. There is a hissing sound and the amulet 
falls off your chest. You throw it away from you as it turns to dust. You've lost some stamina but are otherwise
fine.
"""
    para_12_text_1 = """In your weakened state you struggle to open the vial of Holy Elixir but through sheer 
determination you unstop the bottle and pour it over the amulet. There is a hissing sound and the amulet 
falls off your chest but you were already weak from your previous battles. You feel yourself fading.
"""
    if "Holy Elixir" in inventory:
        inventory.remove("Holy Elixir")
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
    para_13_text = """You have no means to fight off this curse except sheer determination. Struggling against the weakness, 
you try slicing the amulet off with your dagger.
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
    para_14_text = """Panting with pain, you managed to slice the amulet from your skin and throw it away, leaving yourself 
bleeding, but alive.
"""
    para_14_text_1 = """After taking some time to recover and deal with your injury, you look at the last item you found, a ring. 
This time you examine your find more closely and find etchings along the inside that name this the Ring of Light,a useful item for
lighting up dark areas.

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
    para_16_text = """You dont like the look of the amulet, sensing something dark about it. The leave it alone and
take a look at the ring.

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
    para_17_text = """You take a few minutes to calm down after your frightening experience, thinking that you need to
be more careful in future. After taking some time to recover, you look at the last item you found, a ring. 
This time you examine your find more closely and find etchings along the inside that name this the Ring of Light,a 
useful item for lighting up dark areas.

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
    para_18_text = """Your experience with the amulet has put you off taking any kind of jewellery with you. You leave 
the ring behind. 
You retrace your steps and find yourself outside the tree once more. You continue down the path, leaving the tree behind.
"""
    print(para_18_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()

def paragraph_19(): #take ring and reveal its purpose
    clear_screen()
    para_19_text = """Upon closer examination of the ring, you find etchings along the inside that name this the Ring of 
Light,a useful item for lighting up dark areas.
After pocketing the ring, you retrace your steps and find yourself back outside the tree once more. You continue down the 
path, leaving the tree behind.
"""
    print(para_19_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()   

def paragraph_20(): #continue down the path, leaving tree behind
    clear_screen()
    print("paragraph 20")
    
def paragraph_21():
    clear_screen()
    para_21_text = """You decide to leave the ring behind. You retrace your steps and find yourself back outside the tree 
once more. You continue down the path, leaving the tree behind.
"""
    print(para_21_text)
    print("Press any key to continue ...")
    msvcrt.getch()
    paragraph_20()
    
def paragraph_22():
    print("You don't have a Holy Elixir. Press any key to continue...")
    msvcrt.getch()
    paragraph_13()
    
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

def paragraph_24():
    para_24_text = """You retrace your steps and find yourself back outside the tree once more.
You continue down the path, leaving the tree behind."""
    print(para_24_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_20()
    

############### MAIN PROGRAM ##################

start_game()
