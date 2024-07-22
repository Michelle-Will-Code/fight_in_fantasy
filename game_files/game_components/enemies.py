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
    
goblin = Enemy(name="Goblin", skill=6, stamina=10, damage=5)
sprite = Enemy(name="Sprite", skill=8, stamina=15, damage=7)
mutant_plant = Enemy(name="Mutant Plant", skill=4, stamina=10, damage=6)
ogre = Enemy(name="Ogre", skill=6, stamina=12, damage =8)
skeleton = Enemy(name="Skeleton", skill=7, stamina=10, damage=8)
ghoul = Enemy(name="Ghoul", skill=5, stamina=12, damage=9) #unused so far
hermit = Enemy(name="Hermit", skill=5, stamina=12, damage = 6)
giant_spider = Enemy(name="Giant Spider", skill=5, stamina=8, damage =5)

# Encounters List ##

encounters = [goblin, sprite, mutant_plant, ogre, skeleton, ghoul, hermit]
