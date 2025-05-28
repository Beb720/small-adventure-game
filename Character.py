# Character.py

import json

class Player:
    def __init__(self, name):
        with open("json_Files/weapons.json", "r") as f:
            self.Weapon_List = json.load(f)
    
        self.name = name
        self.health = 100
        self.status_effects = []
        self.items = []
        self.weapon = self.Weapon_List["Fist"]
    
    def use_item(self):
        if bool(len(self.items)):
            for i in range(len(self.items)):
                print(f"{i}. {self.items[i]}")
                
            print("What item would you like to use?")
            item_choice = int(input(""))
            print(f"You used {self.items[item_choice]}. NOT FINISHED!")
            #Edit item data
        
        else:
            print("You don't have any items")
            return True

    def damage(self, damage):
        self.health -= damage

    def heal(self):
        pass #add later

Player("Bennett")