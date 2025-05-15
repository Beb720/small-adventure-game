# Locations.py
"""
# Function map with all locations is at the bottom of the code

Loation Map:

Home | Windy Path | Forest | Short Path | Village
    
    # Dark Forrest is below Forest

"""

Location_List = {
    "home": ["home", False, 0, ["windy_path"]],
    "windy_path": ["windy_path", True, 1, ["home", "forest"]],
    "forest": ["forest", True, 2, ["windy_path", "short_path", "dark_forest"]],
    "short_path": ["short_path", True, 1, ["forest", "village"]],
    "village": ["village", False, 0, ["short_path"]],
    "dark_forest": ["dark_forest", True, 3, ["forest"]]
}
    

class Location:
    def __init__(self):
        self.location = "home"
        self.spawning = False
        self.danger = 0
        self.adjacent_locations = ["windy_path"]

    def change(self, new_location): #changes location
        if new_location in self.adjacent_locations:
            self.location = Location_List[new_location][0]
            self.spawning = Location_List[new_location][1]
            self.danger = Location_List[new_location][2]
            self.adjacent_locations = Location_List[new_location][3]
        else:
            return "Sorry, you can't travel there."


"""     
location = Location()
print(location.location)
print(location.spawning)
location.change("windy_path")
print(location.location)
print(location.spawning)
"""