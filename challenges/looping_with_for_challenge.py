#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# Function 1
# Write a for loop that returns all the animals from the NE Farm!
print("\nFUNCTION 1")
for animal in farms[0]["agriculture"]:
    print(animal)


# Function 2
# Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.
print("\nFUNCTION 2")
user_input = input("What farm's agriculture would you like to get info from? ")
for each_farm in farms:
    if user_input in each_farm["name"]:
        print(each_farm["agriculture"])


# Function 3
# Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.
print("\nFUNCTION 3")
user_input = input("What farm's animals would you like to get info from? ")
ignore = ["carrots", "celery"]
for each_farm in farms:
    if user_input in each_farm["name"]:
        for animal in each_farm:
            if animal not in ignore:
                print(each_farm["agriculture"])
