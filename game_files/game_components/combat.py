## COMBAT FUNCTIONS ##

# This module contains all the functions pertaining to combat

## Imported Modules ##

import msvcrt
import random
from game_files.game_components.utilities import *
from game_files.game_components.player import *
from game_files.areas.endings import game_over

## Damage Calculation ##

def calculate_damage(attacker_skill, defender_skill): # damage calculation for combat
    base_damage = 2
    damage = base_damage + (attacker_skill // 2) - (defender_skill // 2)
    return max(1, damage)

## Combat ##

def combat(player, enemy): # simulates the traditional turn based dice rolls for combat
    global purse
    print("\nPrepare to fight!\n")
    print("Press any key to continue...")
    msvcrt.getch()
    clear_screen()
    print("Battle results: \n")
    
    #combat counters
    player_hits = 0
    player_deflects = 0
    player_total_damage = 0
    enemy_hits = 0
    enemy_deflects = 0
    enemy_total_damage = 0
    
    while player.stamina >0 and enemy.stamina >0:
        #Player attack
        player_attack_roll = roll_dice() + player.skill + random.randint(-1,1)
        enemy_defense_roll = roll_dice() + enemy.skill + random.randint(-1,1)
        
        if player_attack_roll > enemy_defense_roll:
            damage = calculate_damage(player.skill, enemy.skill)
            enemy.take_damage(damage)
            player_hits += 1
            player_total_damage += damage
        else:
            player_deflects += 1
        
        #check if enemy defeated
        if enemy.stamina <=0:
            break
        
        #enemy attack
        enemy_attack_roll = roll_dice() + enemy.skill + random.randint(-1,1)
        player_defense_roll = roll_dice() + player.skill + random.randint(-1,1)
        
        if enemy_attack_roll > player_defense_roll:
            damage = calculate_damage(enemy.skill, player.skill)
            player.take_damage(damage)
            enemy_hits += 1
            enemy_total_damage += damage
        else:
            enemy_deflects += 1
            
    #battle results
    print(f"You hit the {enemy.name} {player_hits} times and dealt a total of {player_total_damage} damage.")
    print(f"You deflected {enemy_deflects} of the {enemy.name}'s attacks.")
    print(f"The {enemy.name} hit you {enemy_hits} times and dealt a total of {enemy_total_damage} damage.")
    print(f"The {enemy.name} deflected {player_deflects} of your attacks. \n")
     
    #check if player defeated
    if player.stamina <= 0:
        print("\nYou have been defeated...")
        print("\nPress any key to continue...")
        msvcrt.getch()
        return False
        #Could have a def function here for game over
    else:
        print(f"\n\n{enemy.name} is defeated!\n")
        print(player.show_stats())
        print("\nPress any key to continue... ")
        msvcrt.getch()
        return True

def encounter_enemy(enemy): # deals with enemy generation
    result = combat(player, enemy)
    if result:
        print(" ")
    else:
        print(f"You have fallen in battle. The quest is lost.")
        game_over()
        
