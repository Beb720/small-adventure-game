# main.py

import random
import Locations
import Character
import Encounters
"""
def tick_loop():
    while True:
        if charecter_location
"""
player = Character.Player("Bennett")
location = Locations.Location() # initalizes Location class

while True:

    print("What would you like to do?")
    print("1. Hunt mobs")
    print("2. Travel")
    print("3. Organize Sack")
    action = int(input(""))

    if action == 1:
        if location.spawning:
            Encounters.Encounter(location.danger, player)

        else:
            print("Sorry, mobs don't spawn here.")