# Locations.py

import json

"""
# Function map with all locations is at the bottom of the code

Loation Map:

Home | Windy Path | Forest | Short Path | Village
    
    # Dark Forrest is below Forest

""" 

class Location:
    def __init__(self):
        with open("json_Files/locations.json", "r") as f:
            self.Location_Data = json.load(f)


        self.info = self.Location_Data["home"]

    def change(self, new_location): #changes location
        if new_location in self.info["adjacent_locations"]:
            self.info = self.Location_Data[new_location]
            print(f"\nYOU TRAVELED TO: {self.info["name"]}")
            print()

        else:
            return "Sorry, you can't travel there."