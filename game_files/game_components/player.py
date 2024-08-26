## PLAYER ##

# This module contains everything concerning the player. Future considerations will be use of dice functions to determine starting stats

from game_files.game_components.inventory import *
from game_files.game_components.status_effects import *

class Player:
    def __init__(self, skill, stamina, max_stamina, luck):
        self.skill = skill
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.luck = luck
        self.gold = 5
        self.health_potions = 2 # each potion heals 5 stamina
        self.inventory = Inventory()
        self.status_effects = Status_Effects()
        
    def show_stats(self):
        return f"Your current stats are: \n\n Skill: {player.skill}  Stamina: {player.stamina} Luck: {player.luck}\n\n"
    
    def modify_luck(self, amount):
        self.luck += amount
        if self.luck <0:
            self.luck =4
      
    def take_damage(self, damage):
        self.stamina -= damage
        if self.stamina <1:
            self.stamina = 0
           
    def heal_damage(self, amount):
        self.stamina +=amount
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
            
    def increase_skill(self, amount):
        self.skill +=amount
        
    def decrease_skill(self, amount):
        self.skill -= amount
        if self.skill <0:
            self.skill = 0
            
    def add_gold(self, amount):
        self.gold += amount
    
    def subtract_gold(self, amount):
        self.gold -= amount
        if self.gold <0:
            self.gold = 0
            
    def add_health_potions(self, amount):
        self.health_potions += amount
        
    def subtract_health_potions(self, amount):
        self.health_potions -= amount
        if self.health_potions < 0:
            self.health_potions = 0
            
    def use_health_potion(self,amount):
        if self.health_potions >0:
            self.heal_damage(5)
            self.subtract_health_potions(1)
            return True
        else:
            return False

        
   

## Player Stats ##
   
player = Player(skill=8, stamina=18, max_stamina=18, luck=4)
#standard skill 8 stamina 18 max stamina 20 luck 4
#skill and luck do not need max
#potentially luck points could be reduced every time luck is tested. introduce luck potion to increase luck again


