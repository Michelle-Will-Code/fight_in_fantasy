## Endings ##

## Imported Modules ##

from game_files.game_components.utilities import *

## Player Death ##

def game_over(): # Stamina at 0
    clear_screen()
    print("You succumb to your injuries. Your quest is over.")
    
def game_over_special(): # Paralysed
    clear_screen()
    print("The venom of the creature paralyses you. You are powerless as the creature drags you to its lair to feast.")

def game_over_amulet_death(): # Cursed Amulet
    clear_screen()
    amulet_death = """Your attempts to remove the amulet fail, leaving you bleeding out on the ground. Your vision grows 
clouded, then dark. You listen as your heart beat slowly fades. Your adventure is over.
"""
    print(amulet_death)

def game_over_winner():
    pass    
