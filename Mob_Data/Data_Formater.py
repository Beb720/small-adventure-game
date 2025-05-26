import json

def old_append():
    with open("mobs.json","r") as f:
        Danger_Levels = json.load(f)
    print(Danger_Levels)
    D = []
    print("Write data in this order:")
    print("danger_level | mob_name | damage | crit_damage | crit_chances")
    k = input(" \n")
    D.append(k)

    Danger_Levels[D[0]][D[1]] = {"damage": D[2], "crit_damage": D[3], "crit_chances": (D[4], D[5])}
    with open("mobs.json", "w") as f:
        json.dump(Danger_Levels, f, indent=4)

def convert_to_readable():
    with open("mobs.json", "r") as f:
        Danger_Levels = json.load(f)

Danger_Levels = {
    1: {
            "Lvl. 1 Zombie": {"name": "Lvl. 1 Zombie", "damage": 5, "crit_damage": 12, "crit_chances": (75, 25)},
            "Lvl. 1 Skeleton":{"name": "Lvl. 1 Skeleton", "damage": 7, "crit_damage": 11, "crit_chances": (90, 10)},
            "Robber": {"name": "Robber", "damage": 14, "crit_damage": 19, "crit_chances": (70, 30)}
        },
    
    2: {
            "Lvl. 2 Zombie":  {"name": "Lvl. 2 Zombie", "damage": 10, "crit_damage": 17, "crit_chances": (75, 25)},
            "Lvl. 2 Skeleton": {"name": "Lvl. 2 Skeleton", "damage": 12, "crit_damage": 16, "crit_chances": (90, 10)},
            "Robber": {"name": "Robber", "damage": 20, "crit_damage": 25, "crit_chances": (70, 30)}
        },

    3: {
            "Lvl. 3 Zombie": {"name": "Lvl. 3 Zombie", "damage": 15, "crit_damage": 22, "crit_chances": (75, 25)},
            "Lvl. 3 Skeleton": {"name": "Lvl. 3 Skeleton", "damage": 17, "crit_damage": 21, "crit_chances": (90, 10)},
            "Robber": {"name": "Robber", "damage": 30, "crit_damage": 42, "crit_chances": (70, 30)},
            "Bear": {"name": "Bear", "damage":40, "crit_damage": 63, "crit_chances": (50, 50)}
    }
}

with open("json_Files/mobs.json", "w") as f:
        json.dump(Danger_Levels, f, indent=4)
    

