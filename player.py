## Player ##

class Player:
    def __init__(self, skill, stamina, luck):
        self.skill = skill
        self.stamina = stamina
        self.luck = luck
        self.gold = 5
        self.health_potions = 2 # each potion heals 5 stamina
    
    def modify_luck(self, amount):
        self.luck += amount
        if self.luck <0:
            self.luck =10
            
    def take_damage(self, damage):
        self.stamina -= damage
        if self.stamina <1:
            self.stamina = 0
            
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

## Player Stats ##
#    
player = Player(skill=8, stamina=20, luck=6)
