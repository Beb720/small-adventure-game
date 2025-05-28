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


location.change("windy path")
location.change("forest")

while player.health > 0:

    print("What would you like to do?")
    print("1. Hunt mobs")
    print("2. Travel")
    print("3. Organize Sack")
    action = int(input(""))
    print()

    if action == 1:
        if location.info["spawning"]:
            Encounters.Encounter(location.info["danger"], player)

        else:
            print("Sorry, mobs don't spawn here.")

    elif action == 2:
        print(f"Current Location: {location.info["name"]}")
        print("Adjacent Locations (Places you can travel):")

        for i in range(1, len(location.info["adjacent_locations"]) + 1):
            print(f"{i}. {location.info["adjacent_locations"][i - 1]}")

        location_choice = int(input("Where would you like to go?\n")) - 1
        location.change(location.info["adjacent_locations"][location_choice])