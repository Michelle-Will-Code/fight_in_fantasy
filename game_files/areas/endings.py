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
to stop him as he drags you towards the butchers block. 

Your adventure ends here.
"""
    print(butchered)
    
def game_over_possession():
    clear_screen()
    possessed = """You utterly fail to fight off the possession. Your mind is now trapped in a body you can no 
longer control. The spirit cackles gleefully as the vines fall away from it. It takes your body outside
the cave. You feel the malevolence of this spirit as it sends it foul magic out into the forest.

Your adventure ends here.
"""
    print(possessed)
    
def game_over_fall():
    clear_screen()
    fall = """You hit several branches on the way down. When your broken body finally hits the putrid floor of 
the forest you can no longer move. You hear movement and a curious growl but you dont stay conscious long enough
to find out what it is.

Your adventure ends here.
"""
    print(fall)

def game_over_drowned():
    clear_screen()
    drowned = """The swamp creature pulls you into the pool, and you struggle to breathe as the putrid 
water fills your lungs. Your strength fails as you struggle to break free. Unconsciousness comes quickly.

Your adventure is over.
"""
    print(drowned)

def game_over_fog():
    clear_screen()
    fog = """The choking fog becomes too much for you in your weakened state. You collapse as it slowly
suffocates you.
    
Your adventure ends here.
"""
    print(fog)

def game_over_spider():
    clear_screen()
    spider = """While you are struggling to get free, you hear the skittering sound of the spiders feet. You
are grabbed as the spider bites into you several times, injecting more of its venom into your body. You lose
consciousness again for the last time.

Your adventure ends here.
"""
    print(spider)

def game_over_winner():
    pass   
