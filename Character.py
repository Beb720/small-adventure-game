# Character.py

import json

with open("json_Files/weapons.json", "r") as f:
    Weapon_List = json.load(f)

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.status_effects = []
        self.items = []
        self.weapon = Weapon_List["Fist"]
    
    def use_item(self):
        if bool(len[self.items]):
            for i in range(len[self.items]):
                print(self.items(i))
            print("What item would you like to use?")
            #Edit item data
        else:
            print("You don't have any items")
            return True

    def damage(self, damage):
        self.health -= damage

    def heal(self):
        pass #add later

Player("Bennett")