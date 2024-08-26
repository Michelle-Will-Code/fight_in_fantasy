## STATUS EFFECT ##

## This module contains eveything pertaining to status effects

class Status_Effect:
    def __init__(self):
        self.status = []
        
    def add_item(self, status):#add a status effect
        self.status.append(status)
    
    def remove_item(self, status):#remove a status effect
        if status in self.status:
            self.status.remove(status)
        else:
            print("")
           
    def clear(self): #removes all status effects
        self.status = []
    
    def show_inventory(self): #display status effects
        if self.status:
            return ', '.join(self.status)
        else:
            return "You are free of status effects."
        
    def has_status_check(self, status): #check status effects
        return status in self.status
    
##inventory items

#Rope - starting item for now
#Flint - to light a fire
#Sleep potion - put something to sleep guard etc
#Holy Elixir - use on cursed items and creatures - amulet, ghoul, etc
#Ring of light - light up the cave
#Meat cleaver  - keep if sword is lost. if have instead of sword can turn tide of some battles 
