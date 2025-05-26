# Encounters.py

import random

# Zombie, Skeleton, robber, bear
Danger_Levels = {
    1: ("Lvl. 1 Zombie", "Lvl. 1 Skeleton", "Robber"),
    2: ("Lvl. 2 Zombie", "Lvl. 2 Skeleton", "Robber"),
    3: ("Lvl. 3 Zombie", "Lvl. 3 Skeleton", "Robber", "Bear")
}

Danger_Levels2 = {
    1: (
            #(Mob name, damage, crit damage, crit chances)
            ("Lvl. 1 Zombie", 5, 12, (75, 25)),
            ("Lvl. 1 Skeleton", 7, 11, (90, 10)),
            ("Robber", 14, 19, (70, 30))
        ),
    2: (
            ("Lvl. 2 Zombie", 10, 17, (75, 25)),
            ("Lvl. 2 Skeleton", 12, 16, (90, 10)),
            ("Robber", 20, 25, (70, 30))
        ),

    3: (
            ("Lvl. 3 Zombie", 15, 22, (75, 25)),
            ("Lvl. 3 Skeleton", 17, 21, (90, 10)),
            ("Robber", 30, 42, (70, 30)),
            ("Bear", 40, 63, (50, 50))
        )
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

        else: 
            self.turn()
        
        self.mob_attack()

            
    def attack(self):
        print(f"You attacked the {self.mob}")
        if bool(random.choices((0, 1), weights = self.player.crit_chances)):
            print(f"CRITICAL HIT! Your did {self.player.weapon_damage + self.player.crit_damage}")
        print("You did ")

    def mob_attack(self):
        pass