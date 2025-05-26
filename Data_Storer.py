import json


data = {
    "Fist": {"name": "Fist", "damage": 10, "crit_damage": 12, "crit_chances": [25, 75]}
}
file = "json_Files/weapons.json"

with open(file, "w") as f:
    json.dump(data, f, indent=4)

