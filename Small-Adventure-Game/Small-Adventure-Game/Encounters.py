# Encounters.py

import random

# Zombie, Skeleton, robber, bear
Danger_Levels = {
    1: ["Lvl. 1 Zombie", "Lvl. 1 Skeleton", "Robber"],
    2: ["Lvl. 2 Zombie", "Lvl. 2 Skeleton", "Robber"],
    3: ["Lvl. 3 Zombie", "Lvl. 3 Skeleton", "Robber", "Bear"]
}

Damage = {
    "Zombie": 5,
    "Skeleton": 7,
    "Robber": 13,
    "Bear": 25
}

class Encounter:
    def __init__(self, danger, player):
        self.mob = random.choice(Danger_Levels[danger])
        self.danger = danger
        self.player = player
        for i in range(len(Damage.keys())):
            pass
        print(f"You encountered a {self.mob}")
        self.turn()
    
    def turn(self):
        print("What would you like to do?")
        print(f"1. Attack ({self.player.weapon}: {self.player.weapon_damage} Damage)")
        print("2. Use an item")
        print("3. Run away")
        turn_choice = int(input(""))
        if turn_choice == 1:
            self.attack()
        
        elif turn_choice == 2:
            pass #use item
    
        elif turn_choice == 3:
            if self.danger < 3 and bool(random.randint(0, 1)):
                print("You ran away successfully")
                return
            else:
                print("You couldn't run away")
        
        
        self.mob_attack()

            
    def attack(self):
        pass

    def mob_attack(self):
        pass