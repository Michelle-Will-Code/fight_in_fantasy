## Endings ##

## Imported Modules ##

from game_files.game_components.utilities import *

## Player Death ##

def game_over(): # Stamina at 0
    clear_screen()
    death = """You succumb to your injuries. Your quest is over.
"""
    print(death)
    
def game_over_paralysis(): # Paralysed
    clear_screen()
    paralysis = """The venom of the creature paralyses you. You are powerless as it drags
you to its lair to feast.
"""
    print(paralysis)

def game_over_amulet_death(): # Cursed Amulet
    clear_screen()
    amulet_death = """Your attempts to remove the amulet fail, leaving you bleeding out on 
the ground. Your vision grows clouded, then dark. You listen to your heart beat slowly fading. 
Your adventure is over.
"""
    print(amulet_death)
    
def game_over_butchered():
    clear_screen()
    butchered = """Your struggling only serves to make your bonds tighter. As you hear footsteps, 
you panic and increase your struggling. The hermit enters the room and smiles at you. You are unable
to stop him as he drags you towards the butchers block. Your adventure ends here.
"""
    print(butchered)

def game_over_winner():
    pass   
