# Locations.py
"""
# Function map with all locations is at the bottom of the code

Loation Map:

Home | Windy Path | Forest | Short Path | Village
    
    # Dark Forrest is below Forest

"""

Location_List = {
    "home": [False, 0, "home", ["windy_path"]]
}
    

class Location:
    def __init__(self):
        self.home()

    def change(self, new_location): #changes location
        if new_location in self.adjacent_locations:
            function_to_execute = function_map[new_location]
            function_to_execute(self)
        else:
            return "Sorry, you can't travel there."

    def home(self):
        self.spawning = False
        self.danger = 0
        self.location = "home"
        self.adjacent_locations = ["windy_path"]

    def windy_path(self):
        self.spawning = True
        self.danger = 1
        self.location = "windy_path"
        self.adjacent_locations = ["home", "forest"]
    
    def forest(self):
        self.spawning = True
        self.danger = 2
        self.location = "forest"
        self.adjacent_locations = ["windy_path", "short_path", "dark_forest"]

    def short_path(self):
        self.spawning = True
        self.danger = 1
        self.location = "short_path"
        self.adjacent_locations = ["forest", "village"]

    def village(self):
        self.spawning = False
        self.danger = 0
        self.location = "village"
        self.adjacent_locations = ["short_path"]

    def dark_forest(self):
        self.spawning = True
        self.danger = 3
        self.location = "dark_forest"
        self.adjacent_locations = ["forest"]

# Function map
function_map = {
    "home": Location.home,
    "windy_path": Location.windy_path,
    "forest": Location.forest,
    "short_path": Location.short_path,
    "village": Location.village,
    "dark_forest": Location.dark_forest
}