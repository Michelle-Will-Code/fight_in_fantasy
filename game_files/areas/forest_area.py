## FOREST AREA

# Imported modules

import msvcrt
from game_files.game_components.utilities import *
from game_files.game_components.combat import *
from game_files.areas.temple_area import paragraph_100
from game_files.areas.chasm_area import paragraph_80
from game_files.areas.chasm_area import paragraph_81
from game_files.areas.endings import *
from game_files.game_components.enemies import *

# Paragraphs

def paragraph_45(): #leaving the hermit hut behind
    clear_screen()
    para_45_text = """You venture deeper into the forest. The trees grow denser, their 
thick branches creating a canopy that blocks out most of the sunlight. The path becomes 
less defined, forcing you to navigate through the underbrush. You begin to hear the sound
of running water.

Do you follow the sound of the running water? (press 1 {para 48})

Or do you press on through the forest? (press 2 {para 49})
"""
    print(para_45_text)
    choice_para_45 = input("Make a choice and press Enter: ")
    if choice_para_45 == "1":
        paragraph_48()
    elif choice_para_45 == "2":
        paragraph_49()
    else:
        paragraph_45()

def paragraph_48(): #follow sound of water
    clear_screen()
    healing = 2
    healing2 = 3
    gold = 2
    item = "Map"
    para_48_text = """Following the sound of the running water, you come upon a small, tranquil 
pool fed by a gentle stream. The clear, cool water looks inviting, and you decide to rest and 
refresh yourself here.

Do you take a drink of the water? (press 1 {para 50})

Look around the pool (press 2 {para 51})

Or rest by the pool? (press 3 {para 52})
"""
    print(para_48_text)
    choice_para_48 = input("Make a choice and press Enter: ")
    if choice_para_48 == "1":
        player.heal_damage(healing)
        paragraph_50()
    elif choice_para_48 == "2":
        player.add_gold(gold)
        player.inventory.add_item(item)
        paragraph_51()
    elif choice_para_48 == "3":
        player.heal_damage(healing2)
        paragraph_52()
    else:
        paragraph_48()

def paragraph_49(): #press on through the forest
    clear_screen()
    para_49_text = """You continue to push through the dense forest. The path is difficult and 
you have to hack through thick vines and branches. Eventually, you find a more defined trail that 
seems to lead somewhere. You follow it until you reach a fork in the path.

Do you take the left path leading uphill? (press 1 {para 53})

Or the right path which seem to lead into a darker part of the forest? (press 2 {para 54})
"""
    print(para_49_text)
    choice_para_49 = input("Make a choice and press Enter: ")
    if choice_para_49 == "1":
        paragraph_53()
    elif choice_para_49 == "2":
        paragraph_54()
    else:
        paragraph_49()
    
def paragraph_50(): #drink pool water
    clear_screen()
    para_50_text = """You kneel by the pool and drink the cool, refreshing water. You feel 
rejuvenated and regain 2 Stamina points. While resting, you notice an entrance to a cave partially 
hidden by foliage.

Do you enter the Cave (press 1 {para_55})

Or continue on your journey (press 2 {para_56})
"""
    print(para_50_text)
    choice_para_50 = input("Make a choice and press Enter: ")
    if choice_para_50 == "1":
        paragraph_55()
    elif choice_para_50 == "2":
        paragraph_56()
    else:
        paragraph_50

def paragraph_51(): #look around the pool
    clear_screen()
    para_51_text = """You search the area around the pool and find an old leather bag half-buried under 
some leaves. Inside the bag, you find 2 gold coins and an old sketch that seems to be a hastily drawn
map outlining landmarks on the way to the temple you are seeking (add map to inventory). With renewed 
hope, you continue your journey. 
"""
    print(para_51_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_56()

def paragraph_52(): #take time to rest and recover
    clear_screen()
    para_52_text = """You take some time to rest by the pool, feeling the cool breeze and listening to 
the soothing sound of the water. This rest restores 3 Stamina points. As you prepare to leave, you spot 
what looks like the entrance to a cave hidden by dense foliage.

Do you investigate the cave (press 1 {para 55})

Or continue your journey (press 2 {para 56})
"""
    print(para_52_text)
    choice_para_52 = input("Make a choice and press Enter: ")
    if choice_para_52 == "1":
        paragraph_55()
    elif choice_para_52 == "2":
        paragraph_56()
    else:
        paragraph_52

def paragraph_53(): #left path uphill
    clear_screen()
    para_53_text = """You take the left path and begin to climb a gentle hill. The forest thins slightly, 
allowing more light to filter through. As you reach the top, you see what looks like the ruins of an old 
temple far in the distance.  The sight fills you with renewed determination. You carefully make your way 
along, moving closer to your goal.
"""
    print(para_53_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_57()

def paragraph_54(): #right path into dark part of forest
    clear_screen()
    para_54_text = """You continue deeper into the forest, the dense canopy above blocking out much of the 
light. The air grows cooler and the forest feels more foreboding. Suddenly, you encounter a group of goblins 
blocking your path.

Do you fight the goblins? (press 1 {para 64})

Or try to evade them? (press 2 {para 65})
"""
    print(para_54_text)
    choice_para_54 = input("Make a choice and press Enter: ")
    if choice_para_54 == "1":
        paragraph_64()
    elif choice_para_54 == "2":
        paragraph_65()
    else:
        paragraph_54()

def paragraph_55(): #enter cave
    clear_screen()
    para_55_text = """You carefully enter the cave, your footsteps echoing off the damp walls. The air 
inside is cool and musty, and you feel a slight draft from deeper within. As you venture further, you 
see a faint glimmer of light deep within.

Do you explore deeper? (press 1 {para 62})

Or leave the cave? (press 2 {para 63}
"""
    print(para_55_text)
    choice_para_55 = input("Make a choice and press Enter: ")
    if choice_para_55 == "1":
        paragraph_62()
    elif choice_para_55 == "2":
        paragraph_63()
    else:
        paragraph_55()

def paragraph_56(): #continue on your journey
    clear_screen()
    para_56_text = """Leaving the pool behind, you continue your journey through the dense forest. The 
path is difficult, but you push on, driven by the hope of reaching the ancient temple. You come to a 
fork in the path where you can head uphill or go into a dark area of the forest.

Do you take the left path up the hill? (press 1 {para 53})

Or take the right path into the darker area? (press 2 {para 54})
"""
    print(para_56_text)
    choice_para_56 = input("Make a choice and press Enter: ")
    if choice_para_56 == "1":
        paragraph_53()
    elif choice_para_56 == "2":
        paragraph_54()
    else:
        paragraph_56()

def paragraph_57(): #rickety bridge and chasm
    clear_screen()
    para_57_text = """As you continue along the path, you suddenly come upon a wide chasm. Looking down 
you can see the tops of gnarled trees and an odd yellow fog. A rickety old bridge spans the gap, swaying 
slightly in the breeze. The bridge looks dangerous, but it seems to be the only way forward.

Do you attempt to cross the bridge? (press 1 {para 58})

Or look for a way down? (press 2 {para 59})
"""
    print(para_57_text)
    choice_para_57 = input("Make a choice and press Enter: ")
    if choice_para_57 == "1":
        paragraph_58()
    elif choice_para_57 == "2":
        paragraph_59()
    
def paragraph_58(): # attempt to cross bridge
    clear_screen()
    para_58_text = """You step onto the rickety old bridge, testing each plank carefully. The bridge creaks 
and sways with every step, but you manage to keep your balance. Halfway across, a particularly rotten plank 
breaks under your weight.
"""
    print(para_58_text)
    print("Press any key to continue...")
    msvcrt.getch()
    luck_test = roll_dice()
    if luck_test <4:
        paragraph_60()
    else:
        paragraph_61()

def paragraph_59(): #find a way down
    clear_screen()
    para_59_text = """You decide the bridge is too risky and search for another way around the chasm. After
some time, you find a narrow path that seems to lead down into the chasm. It looks treacherous, but it might
be safer than the bridge.
"""
    print(para_59_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_81()

def paragraph_60(): #lucky on bridge
    clear_screen()
    para_60_text = """You manage to leap to the next plank as the rotten one breaks away, and you continue 
carefully to the other side. Safe at last, you take a moment to catch your breath before continuing your 
journey.
"""
    print(para_60_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_100()

def paragraph_61(): #unlucky on bridge
    clear_screen()
    stamina_loss = 6
    skill_loss = 2
    player.take_damage(stamina_loss)
    player.decrease_skill(skill_loss)
    para_61_text = """As the plank breaks under you, you lose your balance and fall. You try to grab onto
the bridge, but your fingers slip, and you plummet down ito the chasm. Your fall is broken by one of the 
gharled trees and you tumble into the yellow fog, landing in wet putrid mud before blacking out.
"""
    if player.stamina <= 0:
        game_over_fall()
    else:
        print(para_61_text)
        print("Press any key to continue...")
        msvcrt.getch()
        paragraph_80() #new section
    
def paragraph_62(): #explore cave further #check invetory for Ring of Light
    clear_screen()
    para_62_text = """The cave is far too dark to progress further without some light. If you have the Ring
of Light, you could use it here.

Do you use the Ring of Light? (press 1 {para 69})

Or do you not have this ring? (press 2 {para 70})
"""
    print(para_62_text)
    choice_para_62 = input("Make a choice and press Enter: ")
    if choice_para_62 == "1":
         if player.inventory.has_item_check("Ring of Light"):
            paragraph_69()
         else:
            paragraph_70()
    elif choice_para_62 == "2":
        paragraph_70()
    else:
        paragraph_62()

def paragraph_63(): #leave the cave
    clear_screen()
    para_63_text = """You decide to leave the cave, believing it not worth exploring. You continue your 
journey through the dense forest. The path is difficult, but you push on, finally coming to a fork in the 
path where you can head uphill or go into a dark area of the forest.

Do you take the left path up the hill? (press 1 {para 53})

Or take the right path into the darker area? (press 2 {para 54})
"""
    print(para_63_text)
    choice_para_63 = input("Make a choice and press Enter: ")
    if choice_para_63 == "1":
        paragraph_53()
    elif choice_para_63 == "2":
        paragraph_54()
    else:
        paragraph_63()
        
def paragraph_64(): #fight goblins
    clear_screen()
    para_64_text = """The goblins notice you as you step out and prepare for battle. You must fight them.
    
Goblin: Skill 5, Stamina 6

Goblin: Skill 5, Stamina 6
"""
    print(para_64_text)
    encounter_enemy(goblin)
    if player.stamina > 0:
        encounter_enemy(goblin)
        if player.stamina > 0:
            paragraph_66() # goblin defeated
        else:
            game_over() #player death
    else:
        game_over() #player death
    

def paragraph_65(): #try to evade goblins
    clear_screen()
    para_65_text = """You try to sneak past the goblins, moving slowly and quietly. Time to test your Skill.
"""
    print(para_65_text)
    print("Press any key to continue")
    msvcrt.getch()
    skill_check = roll_dice()
    if skill_check <= player.skill:
        paragraph_67()
    else:
        paragraph_68()  

def paragraph_66(): #goblins defeated
    para_66_text = """You successfully deal with the goblins and continue on your way, feeling a mixture of 
relief and determination. Eventually, you come upon a wide chasm with a rickety old bridge spanning the gap."""

def paragraph_67(): #evade successful
    pass

def paragraph_68(): #evade failed
    clear_screen()
    para_68_text = """You step on a twig which cracks under your weight. The goblins are alerted to your 
presence and rush to attack.
    
Goblin: Skill 5, Stamina 6

Goblin: Skill 5, Stamina 6
"""
    print(para_68_text)
    encounter_enemy(goblin)
    if player.stamina > 0:
        encounter_enemy(goblin)
        if player.stamina > 0:
            paragraph_66() # goblin defeated
        else:
            game_over() #player death
    else:
        game_over() #player death

def paragraph_69(): #have Ring of Light
    clear_screen()
    para_69_text = """You place the ring on your finger and it immeditely lights up your surroundings, enabling you
to continue your exploration. As you venture deeper, the glimmer of light becomes more pronounced. You turn a corner
into a large space. An altar of some sort stands in the centre with glimmering vines twisted around it. Sat on the 
altar in a stand is a clear glass orb. As you approach, the orb begins to shine.

Do you touch the orb? (press 1 {para 71})

Or leave it and return the way you came? (press 2 {para 72})
"""
    print(para_69_text)
    choice_para_69 = input("Make a choice and press Enter: ")
    if choice_para_69 == "1":
        paragraph_71()
    elif choice_para_69 == "2":
        paragraph_72()
    else:
        paragraph_69()

def paragraph_70(): #no Ring of Light
    clear_screen()
    para_70_text = """You have no means to explore the cave further and it would be too dangerous to go in
without any light. You leave the cave and return to the pool before continuing on your way.
"""
    print(para_70_text)
    msvcrt.getch()
    paragraph_49()
    
def paragraph_71(): #touch the orb
    clear_screen()
    para_71_text = """You cautiously touch the orb. It feels warm to the touch. Suddenly the vines twisting
around the altar come to life. They wrap themselves around you, forcing you into a kneeling position before
the altar. Sharp white light explodes from the orb, blinding you. You hear a strange etheral voice as you
fight against the vines. Eventually the light recedes and a dark spirit floats before you.
"I am finally released!" it declares.
It studies you as you continue to stuggle.
"You will make a fine host," it murmurs.
Against your will, the spirit invades your body. You fight the possession. You will need all your skill and 
stamina for this battle of wills.
"""
    para_71_text_2 = """You resist the invasion of the spirit, but it steps up its attack.
"""
    para_71_text_3 = """You continue to resist the possession. The spirit screams against your defiance. 
Without a body to inhabit, it retreats into the orb and the vines fall away from you.
"""
    para_71_text_4 = """You fail to resist the invasion of the spirit and it settles deeper into your body 
as it attempts to take over your mind.
"""
    print(para_71_text)
    print("Press any key to continue...")
    skill_test = roll_dice()
    stamina_test = roll_12_sided_dice()
    if skill_test <= player.skill: 
        print(para_71_text_2) #spirit fails to possess but tries again
        print("Press any key to continue...")
        msvcrt.getch()
        if stamina_test <= player.stamina: 
            print(para_71_text_3)#spirit fails to possess again. Complete possession prevented
            print("Press any key to continue...")
            paragraph_73() 
        else:
            paragraph_75()#fail
    else:
        print(para_71_text_4)#first failure to resist spirit, spirit continues to possess
        print("Press any key to continue...")
        msvcrt.getch()
        if stamina_test <= player.stamina:
            paragraph_75() #resist complete possession
        else:
            game_over_possession() #complete possession

def paragraph_72(): #don't touch orb, leave the cave
    clear_screen()
    para_72_text = """You sense something ominous about the orb. You slowly back away and return back the way you came.
Exiting the cave, you continue on your journey.
"""
    print(para_72_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_49()

def paragraph_73(): #completely resist the dark spirit
    clear_screen()
    para_73_text = """You retreat out of the cave as fast as you can, leaving the orb and its dark spirit behind. You
collapse by the pool, shaking after your experience. After taking a few minutes to calm yourself, you continue on your
journey.
"""
    print(para_73_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_49()

def paragraph_74():
    clear_screen()
    para_74_text = """You dont have this item.
"""
    print(para_74_text)
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_70()
    
def paragraph_75(): #dark spirit inhabits your body, but keep free will
    clear_screen()
    stamina = 20
    skill = 10
    player.heal_damage(stamina)
    player.increase_skill(skill)
    para_75_text = """The dark spirit inhabits your body but through sheer determination you have managed to keep your 
free will. The vines fall away from you and you stand up, shakily at first, but then power flows through you. The malevolent
force inside you has increased your strength and fully restored your stamina. You may be harder to kill now, but this is the 
spirit ensuring you wont die before it can take you over completely. You will need to be vigilant against any attempts at
control by the spirit until you can find a way to remove it from your body.

You leave the cave and continue on your way.
"""
    print(para_75_text)
    print(f"Your stats have changed:\n Skill: {player.skill} Stamina: {player.stamina}")
    player.add_status("Spirit Possession")