import json

Location_Data = {
    "home": {"name": "Home", "spawning": False, "danger": 0, "adjacent_locations": ["windy path"]},
    "windy path": {"name": "Windy Path", "spawning": True, "danger": 1, "adjacent_locations": ["home", "forest"]},
    "forest": {"name": "Forest", "spawning": True, "danger":2, "adjacent_locations": ["windy path", "short path", "dark forest"]},
    "short path": {"name": "Short Path", "spawning": True, "danger":1, "adjacent_locations": ["forest", "village"]},
    "village": {"name": "Village", "spawning": False, "danger":0, "adjacent_locations": ["short path"]},
    "dark forest": {"name": "Dark Forest", "spawning": True, "danger":3, "adjacent_locations": ["forest"]}
}





Mob_Data = {
    "1": {
            "Lvl. 1 Zombie":
                {"name": "Lvl. 1 Zombie", "damage": 5, "health": 25,"crit_damage": 12, "crit_chances": [75, 25]},
        
            "Lvl. 1 Skeleton":
                {"name": "Lvl. 1 Skeleton", "damage": 7, "health": 25, "crit_damage": 11, "crit_chances": [90, 10]},
        
            "Robber":
                {"name": "Robber", "damage": 14, "health": 40,"crit_damage": 19, "crit_chances": [70, 30]}},
    
    "2": {
            "Lvl. 2 Zombie":
                {"name": "Lvl. 2 Zombie", "damage": 10, "health": 55, "crit_damage": 17, "crit_chances": [75, 25]},
        
            "Lvl. 2 Skeleton":
                {"name": "Lvl. 2 Skeleton", "damage": 12, "health": 50, "crit_damage": 16, "crit_chances": [90, 10]},
        
            "Robber":
                {"name": "Robber", "damage": 20, "health": 75, "crit_damage": 25, "crit_chances": [70, 30]}},

    "3": {
            "Lvl. 3 Zombie":
                {"name": "Lvl. 3 Zombie", "damage": 15, "health": 95, "crit_damage": 22, "crit_chances": [75, 25]},
        
            "Lvl. 3 Skeleton":
                {"name": "Lvl. 3 Skeleton", "damage": 17, "health": 90, "crit_damage": 21, "crit_chances": [90, 10]},
        
            "Robber":
                {"name": "Robber", "damage": 30, "health": 100, "crit_damage": 42, "crit_chances": [70, 30]},
        
            "Bear": #Add spawn requirments, along with robber
                {"name": "Bear", "damage":40, "health": 200, "crit_damage": 63, "crit_chances": [50, 50]}}
}





Weapon_Data = {
    "Fist":
        {"name": "Fist", "damage": 10, "crit_damage": 12, "crit_chances": [25, 75]},
    
    "Wooden Bat":
        {"name": "Wooden Bat", "damage": 12, "crit_damage": 15, "crit_chances": [50, 50]},
    
    "Wood Sword":
        {"name": "Wood Sword", "damage": 15, "crit_damage": 16, "crit_chances": [80, 20]},
    
    "Brone Sword":
        {"name": "Bronze Sword", "damage": 20, "crit_damage": 25, "crit_chances": [75, 25]}
}





Item_Data = {
    "healing": ["apple", 5, "bread", 10, "bandages", 20],
    "other_items": ["gold", "zombie_remains"]
}




print("What would you like to update?")
print("1. Mob_Data")
print("2. Weapon_Data")
print("3. Location_Data")
print("4. Item_Data")
i = int(input(" \n"))

if i == 1:
    with open("json_Files/mobs.json", "w") as f:
        json.dump(Mob_Data, f, indent=4)

elif i == 2:
    with open("json_Files/weapons.json", "w") as f:
        json.dump(Weapon_Data, f, indent=4)

elif i == 3:
    with open("json_Files/locations.json", "w") as f:
        json.dump(Location_Data, f, indent=4)

elif i == 4:
    with open("json_Files/items.json", "w") as f:
        json.dump(Item_Data, f, indent=4)

else:
    print("INCORECT ENTRY")

print("done")