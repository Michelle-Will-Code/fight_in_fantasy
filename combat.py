## Combat Functions ##

## Imported Modules ##

import msvcrt
import random
from utilities import *
from player import *

## Damage Calculation ##

def calculate_damage(attacker_skill, defender_skill): # damage calculation for combat
    base_damage = 4
    damage = base_damage + (attacker_skill // 2) - (defender_skill // 2)
    return max(1, damage)

## Combat ##

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
        print(f"Your current stats are: \n\n Skill: {player.skill}  Stamina: {player.stamina} Luck: {player.luck}\n\n")
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
        
