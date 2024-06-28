## INVENTORY ##

#This module contains everything pertaining to the players inventory

class Inventory:
    def __init__(self):
        self.items = ["Rope", "Flint"]
        
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("")
    
    def show_inventory(self):
        if self.items:
            return ', '.join(self.items)
        else:
            return "Your inventory is empty"
        
    def has_item_check(self, item):
        return item in self.items