## CHASM AREA ##

## Imported Modules ##

import msvcrt
from game_files.game_components.combat import encounter_enemy
from game_files.game_components.utilities import *
from game_files.areas.temple_area import paragraph_100
from game_files.game_components.player import *
from game_files.areas.endings import *
from game_files.game_components.enemies import *

## Paragraphs ##

def paragraph_80():
    clear_screen()
    para_80_text = """You awaken in the chasm, your body aching from the fall. You 
have lost 6 Stamina points and your right arm is broken, forcing you to fight with 
your left arm, resulting in a loss of 2 Skill points. The yellow fog around you is 
poisonous, and you can feel its effects sapping your strength. You must find a way 
out of this chasm quickly.

Do you take a health potion before you begin to make your way out? (press 1 {take potions and go to para 82})

Or move through the chasm looking for an exit? (press 2 {go straight to para 82})
"""
    para_80_text_1 = """ You drink one health potion, regaining 5 stamina. Feeling a 
little better, you start to move on to try and find your way out of the chasm before the
poisonous fog claims you.
"""
    para_80_text_2 = """You search through your pack but you have no health potions left.
Cursing your luck, you start to move on to try and find your way our of the chasm before the
poisonous fog claims you.
"""
    
    print(para_80_text)
    choice_para_80 = input("Make a choice and press Enter: ")
    if choice_para_80 == "1":
        clear_screen()
        if player.use_health_potion():
            print(para_80_text_1)
            print("Press any key to continue: ")
            msvcrt.getch()
            paragraph_82()
        else:
            print(para_80_text_2)
            print("Press any key to continue: ")
            msvcrt.getch()
            paragraph_82()
    elif choice_para_80 == "2":
        paragraph_82()

def paragraph_81():
    print("Climbed down")
    
def paragraph_82(): #move through chasm
    para_82_text = """You move through the chasm, the thick yellow fog making it difficult to see. 
The gnarled trees and pools of putrid water create an eerie atmosphere. Suddenly, you hear the sloshing
of water behind you. You turn to investigate.
"""
    print(para_82_text)
    print("Press any key to continue: ")
    luck_test = roll_dice()
    if luck_test <= player.luck:
        paragraph_83()
    else:
        paragraph_84()

def paragraph_83(): #lucky escape from swamp creature
    para_83_text = """You quickly dodge to the side as a swamp creature lunges at you from a pool of 
putrid water. The creature snarls and retreats back into the pool, but you know it will attack again if 
you linger. You decide to move on quickly.
"""
    print(para_83_text)
    print("Press any key to continue: ")
    msvcrt.getch()
    paragraph_85()

def paragraph_84(): #grabbed by swamp creature
    stamina_loss = 3
    stamina_loss_1 = 6
    para_84_text = """A swamp creature lunges at you from a pool of putrid water, catching you by surprise. 
It tries to pull you into the pool.
"""
    para_84_text_1 = """You manage to break free from the swamp creature's grasp, losing 3 Stamina points 
in the struggle. You quickly move away from the pool, wary of another attack.
"""
    para_84_text_2 = """The swamp creature pulls you into the pool, and you struggle to breathe as the putrid 
water fills your lungs. With your strength fading, you manage to break free, but you have lost 6 Stamina points 
and are now severely weakened.
"""
    print(para_84_text)
    print("Press any key to continue: ")
    msvcrt.getch()
    skill_test = roll_dice()
    if skill_test <= player.skill:
        player.take_damage(stamina_loss)
        if player.stamina > 0:
            print(para_84_text_1)
            print("Press any key to continue: ")
            msvcrt.getch()
            paragraph_85()
        else:
            game_over_drowned()
    else:
        player.take_damage(stamina_loss_1)
        if player.stamina > 0:
            print(para_84_text_2)
            print("Press any key to continue: ")
            msvcrt.getch()
            paragraph_85()
        else:
            game_over_drowned()
           
def paragraph_85():
    clear_screen()
    stamina_loss = 2
    para_85_text = """You continue to make your way through the chasm. It is difficult to see your way
and you are wary of any further attacks. You stay to the right and scan the cliff face in hope of finding
any way back up. After a few minutes you come across a section of cliff that has broken away, leaving scattered
rocks. You cant see far up due to the fog but it may be possible to try using the jagged outcroppings as a means 
to climb out.

Do you attempt to climb up the rock face? (press 1)

Or look for another way up? (press 2)
"""
    print(para_85_text)
    choice_para_85 = input("Make a choice and press Enter: ")
    if choice_para_85 == "1":
        paragraph_86()
    elif choice_para_85 == "2":
        player.take_damage(stamina_loss)
        paragraph_87()
    else:
        paragraph_85()
        
def paragraph_86(): #attempt to climb
    pass

def paragraph_87(): #look for another way up
    para_87_text = """You decide it's too risky to try and make the climb and continue on your way.
The fog continues to burn your lungs and you cough violently, spitting up blood (lose 2 stamina points). 
You need to get out of here soon.
"""
    print(para_87_text)
    if player.stamina <=0:
        print("Press any key to continue: ")
        msvcrt.getch()
        game_over_fog()
    else:
        print("Press any key to continue: ")
        msvcrt.getch()
        paragraph_88()
        
def paragraph_88():#find cave
    clear_screen()
    stamina_loss = 2
    para_88_text = """As you continue along you see an opening in the cliff face. As you approach, you see 
that it is a split in the rock that has formed a path leading upwards. The path looks well worn and there
are the shredded remains of spider webs so there is a chance of encountering creatures here. You will need 
to be wary if you take this path.

Do you climb up the path? (press 1)

Or continue along and try and find another way up? (press 2)
"""
    print(para_88_text)
    choice_para_88 = input("Make a choice and press Enter: ")
    if choice_para_88 == "1":
        paragraph_89()
    elif choice_para_88 == "2":
        player.take_damage(stamina_loss)
        paragraph_90()
    else:
        paragraph_88()
        
def paragraph_89(): #climb the path
    clear_screen()
    stamina_gain = 4
    para_89_text = """You climb the path staying alert for any signs of danger, but the path is quiet for 
now. The path growns steeper and you being to tire. You see a smooth rocky outcropping that would be 
suitable to sit and rest for a while.
    
Do you sit and rest for a while? (press 1 {para 91})
    
Or continue on your way? (press 2 {para 92})
"""
    print(para_89_text)
    choice_para_89 = input("Make a choice and press Enter: ")
    if choice_para_89 == "1":
        player.heal_damage(stamina_gain)
        paragraph_91()
    elif choice_para_89 == "2":
        paragraph_92()
    else:
        paragraph_89()

def paragraph_90(): #find another way up
    para_90_text = """You decide to leave the path for now and search for a safer alternative.
"""

def paragraph_91(): #sit and rest on the rock
    clear_screen()
    para_91_text = f"""You decide to sit down and take some time to rest (4 stamina points restored). While
resting you decide to check over your injuries and the contents of your pack.

STARTING STATS         INVENTORY
Skill: {player.skill}               Gold: {player.gold}
Stamina: {player.stamina}            Health Potions: {player.health_potions}
Luck: {player.luck}                Bag: {player.inventory.show_inventory()}

You consider whether to use a health potion before you continue on your way.

Do you drink a potion? (press 1 -para 93)

Or continue on your way? (press 2 - para 94)
"""
    print(para_91_text)
    choice_para_91 = input("Make a choice and press Enter: ")
    if choice_para_91 == "1":
        paragraph_93()
    elif choice_para_91 == "2":
        paragraph_92()
    else:
        paragraph_91()
    

def paragraph_92(): #continue on your way up the path
    pass

def paragraph_93(): #drink health potion
    clear_screen()

    para_93_text = """You drink a health potion (restore 5 stamina) and feel much better. As you pack
away your things and get ready to leave, you hear a noise above you.

"""
    para_93_text_1 = """You dont have any health potions left. As your pack away your things and get 
ready to leave, you hear a noise above you.

"""
    para_93_text_2 = """You leap out of the way just in time before a giant spider jumps from above. It
hisses at you. Prepare to fight.
"""
    para_93_text_3 = """You try to dive out of the way as a giant spider leaps at you from above, but you
end up trapped under it as it sinks its fangs into your shoulder. You struggle to get free but quickly 
succumb to the paralysing bite. You feel the spider’s thick, sticky webbing wrapping around your body as 
your vision begins to blur.
"""
    luck_test = roll_dice()
    if player.use_health_potion():
        print(para_93_text)
    else:
        print(para_93_text_1)

    if luck_test <= player.luck:
        print(para_93_text_2)
        print("Press any key to continue: ")
        msvcrt.getch()
        paragraph_95()
    else:
        print(para_93_text_3)
        print("Press any key to continue: ")
        msvcrt.getch()
        paragraph_96()


def paragraph_95(): #fight spider
    clear_screen()
    para_95_text = """You kill the spider and then look around carefully for any other spiders in the area
before moving on.
"""
    encounter_enemy(giant_spider)
    if player.stamina >0:
        print(para_95_text)
        print("Press any key to continue: ")
        paragraph_92()
    else:
        game_over()


def paragraph_96(): #paralysed and in spider larder
    para_96_text = """You regain partial awareness as you feel the rough stone beneath you. You are unsure
how long you have been out for. The spider's webbing encasing you obscures your vision but it appears to be 
dark. You find you have some movement now and you struggle in the silk. You have been lucky so far in that 
the spider has not come to eat its newly caught meal, but time may well be running out.
"""
    skill_test = roll_dice()
    if skill_test <= player.skill:
        print("Press any key to continue:")
        msvcrt.getch()
        paragraph_97()
    else:
        print("Press any key to continue: ")
        msvcrt.getch()
        game_over_spider()

def paragraph_97():#escape from webbing
    para_97_text = """With great effort, you manage to get free of the sticky webbing. You find yourself in 