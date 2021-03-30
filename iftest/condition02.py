#!/usr/bin/env python3

# collects input from user
hostname = input("What value should we set for hostname? ")

# check if the user input is the same as mtg
if hostname.lower() == "mtg":
    # if so print out that it was found and matches config
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
elif hostname == "":
    print("You didn't type anything in, silly")

# will print out at the end of the script
print("Exiting the script")
