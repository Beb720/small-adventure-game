# Encounters.py

import Character
import random
import json
"""
Mob_Data = {
    "1": {
            "Lvl. 1 Zombie": {"damage": 5, "crit_damage": 12, "crit_chances": (75, 25)},
            "Lvl. 1 Skeleton":{"damage": 7, "crit_damage": 11, "crit_chances": (90, 10)},
            "Robber": {"damage": 14, "crit_damage": 19, "crit_chances": (70, 30)}
        },
    
    "2": {
            "Lvl. 2 Zombie":  {"damage": 10, "crit_damage": 17, "crit_chances": (75, 25)},
            "Lvl. 2 Skeleton": {"damage": 12, "crit_damage": 16, "crit_chances": (90, 10)},
            "Robber": {"damage": 20, "crit_damage": 25, "crit_chances": (70, 30)}
        },

    "3": {
            "Lvl. 3 Zombie": {"damage": 15, "crit_damage": 22, "crit_chances": (75, 25)},
            "Lvl. 3 Skeleton": {"damage": 17, "crit_damage": 21, "crit_chances": (90, 10)},
            "Robber": {"damage": 30, "crit_damage": 42, "crit_chances": (70, 30)},
            "Bear": {"damage":40, "crit_damage": 63, "crit_chances": (50, 50)}
    }
}
"""
with open("json_Files/mobs.json", "r") as f:
            Mob_Data = json.load(f)

class Encounter:
    def __init__(self, danger, player):
        self.Mob_Data = Mob_Data
    
        self.player = player
        self.danger = danger
        random_choice = random.choice(list(self.Mob_Data[str(danger)].keys()))
        self.mob = self.Mob_Data[str(danger)][random_choice]
        print(f"You encountered a {self.mob["name"]}!")
        self.battle_loop()

    
    def battle_loop(self):
        while self.player_turn() != False:
            if self.mob["health"] <= 0:
                print(f"You defeated {self.mob["name"]}")
                #add drops here
                break
            
            self.mob_turn()

            if self.player.health <= 0:
                print("You died")
                print("GAME OVER!")
                input()
                break
        
        return self.player


    
    def player_turn(self):
        print(f"{self.player.name}'s Health: {self.player.health}")
        print(f"{self.mob["name"]}'s Health: {self.mob["health"]}")
        print()
        print("What would you like to do?")
        print(f"1. Attack ({self.player.weapon["name"]}: {self.player.weapon["damage"]})")
        print("2. Use an item")
        print("3. Run away")
        
        turn_choice = int(input())
        if turn_choice == 1:
            self.player_attack()

        elif turn_choice == 2:
            if self.player.use_item():
                self.player_turn()

        elif turn_choice == 3:
            self.run_away()

        elif turn_choice == 66:
            return False

        else:
            print("That's not a valid option")
            self.player_turn()
        
    
    def run_away(self):
        print("You attempted to run away.")
        if self.danger < 3 and bool(random.choice((0, 1))):
            print("You got away safley.")
            return False

        else:
            print("You couldn't get away")
        


    def player_attack(self):
        if bool(random.choices((0, 1), weights=self.player.weapon["crit_chances"])):
            self.mob["health"] -= self.player.weapon["crit_damage"]

        else:
            self.mob["health"] -= self.player.weapon["damage"]


    def mob_turn(self):
        if bool(random.choices((0, 1), weights=self.mob["crit_chances"])):
            self.player.health -= self.mob["crit_damage"]

        else:
            self.player.health -= self.mob["damage"]