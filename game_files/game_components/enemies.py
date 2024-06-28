## ENEMIES ##

# This module contains everything concerning enemies in the game

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

## Enemy Stats ##
    
goblin = Enemy(name="Goblin", skill=5, stamina=10, damage=5)
sprite = Enemy(name="Sprite", skill=10, stamina=15, damage=7)
mutant_plant = Enemy(name="Mutant Plant", skill=3, stamina=12, damage=6)
ogre = Enemy(name="Ogre", skill=7, stamina=14, damage =10)
skeleton = Enemy(name="Skeleton", skill=6, stamina=10, damage=8)
ghoul = Enemy(name="Ghoul", skill=5, stamina=12, damage=9)

# Encounters List ##

encounters = [goblin, sprite, mutant_plant, ogre,skeleton,ghoul]
