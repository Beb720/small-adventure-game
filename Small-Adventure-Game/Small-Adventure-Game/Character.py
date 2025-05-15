# Character.py

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.status_effects = []
        self.items = []
        self.weapon = "fist"
        self.weapon_damage = 10

    def damage(self, damage):
        self.health -= damage

    def heal(self):
        pass #add later
