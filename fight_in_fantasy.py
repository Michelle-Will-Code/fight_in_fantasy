######### imported libraries
import random
import msvcrt

#############SCREEN ADJUSTMENTS#################

def clear_screen():
    print('\033[2J\033[H', end ='')

############ REQUIREMENTS FOR PLAYER ###############

inventory = ["rope", "flint"]
health_potions = 2
purse = 5

class Player:
    def __init__(self, skill, stamina, luck):
        self.skill = skill
        self.stamina = stamina
        self.luck = luck
        
    def attack(self):
        #attack logic here
        pass
        
    def defend(self):
        #defend logic here
        pass
    
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

encounters = [goblin, sprite, mutant_plant, ogre,skeleton]

############## COMBAT FUNCTIONS ###################

def roll_dice():
    return random.randint(1,6)

def calculate_damage(attacker_skill, defender_skill):
    base_damage = 4
    damage = base_damage + (attacker_skill // 2) - (defender_skill // 2)
    return max(1, damage)

def combat(player, enemy):
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

def encounter_enemy(enemy):
    result = combat(player, enemy)
    if result:
        print(" ")
    else:
        print(f"You have fallen in battle. The quest is lost.")
        exit(0)
        
################ START GAME AND GAME OVER ################
#        
def start_game():
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
        print("Something went wrong, please try again...\n\n")
        start_game()
    
def game_over():
    print("You succumb to your injuries. Your quest is over.")
    
def game_over_special():
    print("The venom of the creature paralyses you. You are powerless as the creature drags you to its lair to feast.")

def game_over_winner():
    pass

############### PARAGRAPHS ###################

def paragraph_1(): #dense trees and a noise
    clear_screen()
    para_1_text = """The forest is dense, with tall trees blocking out most of the sunlight. You
follow a narrow path when you hear rustling in the bushes.

Do you investigate the noise? (type 1 {para 2})

Or do you continue along the path? (type 2 {para UNWRITTEN})

"""

    print(para_1_text)
    choice_para_1 = input("Make a choice and press Enter: ")
    if choice_para_1 == "1":
        paragraph_2()
    elif choice_para_1 == "2":
        pass #unwritten
    else:
        print("Something went wrong, please try again...\n\n")
        paragraph_1()

def paragraph_2(): #goblin encounter
    clear_screen()
    para_2_text = """You cautiously approach the source of the noise. Suddenly a goblin leaps
out at you!

Goblin: Skill 5, Stamina 10
"""
    print(para_2_text)
    encounter_enemy(goblin)
    if player.stamina > 0:
        paragraph_4()
    else:
        game_over()
        
def paragraph_3(): #spiral staircase in tree
    clear_screen()
    para_3_text = """Inside the tree, you find a spiral staircase leading down into darkness. 
    
Do you descend the stairs (press 1 {para 5}) 

Or leave the tree and continue along the path (press 2 {para UNWRITTEN})? 
"""
    print(para_3_text)
    choice_para_3 = input("Make a choice and press Enter: ")
    if choice_para_3 == "1":
        paragraph_5()
    elif choice_para_3 == "2":
        pass #UNWRITTEN
    else:
        print("Something went wrong, please try again...\n\n")
        paragraph_3()
        
def paragraph_4(): #goblin defeat, tree with door
    global purse
    gold = 5
    purse += gold
    clear_screen()
    para_4_text = """The goblin falls at your feet. Searching its body, you find a small pouch of
gold coins. (5 coins are added to your inventory) Continuing forward, you come to a large
twisted tree with a door carved into its trunk. 

Do you enter the tree? (press 1 {para_3})

Or do you continue down the path (press 2 {para UNWRITTEN}
"""
    print(para_4_text)
    choice_para_4 = input("Make a choice and press Enter: ")
    if choice_para_4 == "1":
        paragraph_3()
    elif choice_para_4 == "2":
        pass #UNWRIITEN
    else:
        print("Something went wrong, please try again...\n\n")
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
        paragraph_6()
    else:
        game_over()
    
def paragraph_6(): #ogre defeated, take passage or return up stairs
    clear_screen()
    para_6_text = """With the ogre defeated, you find a hidden passage behind a large boulder. 
    
Do you enter the passage? (press 1 {para 7}) 

Or return up the staircase? (press 2 UNWRITTEN)
"""
    print(para_6_text)
    choice_para_6 = input("Make your choice and press Enter: ")
    if choice_para_6 == "1":
        paragraph_7()
    elif choice_para_6 == "2":
        pass #unwritten
    else:
        print("Something went wrong, try again")
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
        paragraph_8()
    else:
        game_over()
    
def paragraph_8(): #take gold, look at items
    global purse
    clear_screen()
    para_8_text = """ With the guardian skeleton defeated, you take time to pick through the treasure.
It looks like the remains of a goblin's treasure hoard. Most of it is worn and tarnished with age and 
of little value or too large to take with you, however you are able to pocket some gold coins. You do
however find three items small enough that may be of value in your adventure.

    1. A small silver vial
    2. A strange amulet with a dull yellow stone
    3. A ring that emits a glow
    
Do you take the vial with you? (press 1 {para 9})

Or leave it? (press 2 {para 10})
"""
    print(para_8_text)
    gold = 20
    purse += gold
    choice_para_8 = input("Make a choice and press Enter: ")
    if choice_para_8 == "1":
        paragraph_9()
    elif choice_para_8()== "2":
        paragraph_10()
    else:
        ("Something went wrong. Please try again.")
        paragraph_8()
        
def paragraph_9(): #examine and pocket the vial
    print("Got vial")
    
def paragraph_10(): #examine and pocket the amulet
    print("Got amulet")

############### MAIN PROGRAM ##################

start_game()
