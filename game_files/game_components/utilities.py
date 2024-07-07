## Utilities ##

## Imported Modules ##

import random
import os

## Dice Simulations ##

def roll_dice(): #required to simulate a 6 sided dice for combat and luck rolls
    return random.randint(1,6)

def roll_12_sided_dice():
    return random.randint(1,12)

## Clear Screen ##

def clear_screen():
    print('\033[2J\033[H', end ='')