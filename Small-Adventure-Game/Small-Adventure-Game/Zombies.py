# Zombies.py
import random

mobs = ["zombie1", "zombie2", "zombie3"]
def attempt_spawn(player, danger):
    for i in range(danger):
        if bool(random.randint(0, 1)):
            zombie = Zombie(i)
            battle = Battle(player, zombie)
            break
            
class Battle:
    def __init__(self, player, zombie):
        self.player = player
        self.zombie = zombie
        print(f"You encountered a Level {self.zombie.level} Zombie.")
        print("Battle it (0), or run away(1)?")
        i = bool(input())
        if i:
            if self.zombie.level != 3 and bool(random.randint(0, 1)):
                print("You got away succecfully!")
                return

        print("You couldn't get away from the zombie.")

    def turn(self):
        print("What would you like to do?")
        print(f"1. Attack ({self.player.weapon}: {self.player.weapon_damage} Damage)")
        print("2. Use an item")
        print("3. Run away")
        i = int(input())
        if i == 1:
            pass
        
                
            
            

class Zombie:
    def __init__(self, level):
        self.health = 25 * level
        self.strength = 5 * level
        self.level = level