## INVENTORY ##

#This module contains everything pertaining to the players inventory

class Inventory:
    def __init__(self):
        self.items = ["Rope", "Flint"]
        
    def add_item(self, item):#add item to inventory
        self.items.append(item)
    
    def remove_item(self, item):#removes an item
        if item in self.items:
            self.items.remove(item)
        else:
            print("")
           
    def clear(self): #removes inventory contents
        self.items = []
    
    def show_inventory(self): #display invenotry
        if self.items:
            return ', '.join(self.items)
        else:
            return "Your inventory is empty"
        
    def has_item_check(self, item): #check items
        return item in self.items
    
    def get_items(self):
        return self.items.copy()
    
##inventory items

#Rope - starting item for now
#Flint - to light a fire
#Sleep potion - put something to sleep guard etc
#Holy Elixir - use on cursed items and creatures - amulet, ghoul, etc
#Ring of light - light up the cave
#Meat cleaver  - keep if sword is lost. if have instead of sword can turn tide of some battles 