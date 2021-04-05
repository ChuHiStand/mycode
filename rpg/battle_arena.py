#!/usr/bin/env python3

import os
import sys

from character_class import random_challenger_selector
from character_class import display_classes
from character_class import display_class_info
from character_class import playable_character_list
from character_class import start_battle

"""Marco Bragado || Battle Arena """

# will start welcome screen
def start_game():
    print("\nWelcome to the battle arena. Please select what you would like to to do:")
    player_action = input("\n[1] Enter The Arena!\n[2] Enter the Item Shop\nSelection: ")
    if player_action == "1":
        class_selection()
    elif player_action == "2":
        print("Feature not implemented yet")
        start_game()
        # enter_item_shop()
    else:
        print("Invalid selection. Please enter [1] or [2]")
        start_game()


# function that prompts the user to select a player class to play
def class_selection():
    clear_screen()
    print("\nPlease choose a class you would like to play\n")
    display_classes()
    player_class_selection = input("\nPlease type out the class: ").lower()
    while True:
        if player_class_selection in playable_character_list():
            display_class_info(player_class_selection)
            user_input = input("\nDid you want to continue with this class?\n[1] YES, I'm ready to fight!\n[2] No, "
                               "I want to check "
                               "out the other classes!\nSelection: ")
            if user_input == "1":
                start_arena(random_challenger_selector(), player_class_selection)
                break
            elif user_input == "2":
                class_selection()
            else:
                print("Invalid Selection please select [1] or [2]")
        else:
            print("Invalid selection")
            class_selection()


# function to start arena scenario
def start_arena(random_challenger, player_class):
    print("\nThe ARENA MATCH HAS STARTED!")
    print(f"You are facing a {random_challenger}!\n")
    print("What would you like to do?\n[1] Attack\n[2] View Inventory")
    user_selection = input("Selection: ")
    if user_selection == "1":
        play_again = start_battle(random_challenger, player_class)
        if play_again == "1":
            start_game()
        elif play_again == "2":
            exit_app()
    elif user_selection == "2":
        # display_inventory()
        print("Feature not implemented yet.")
        start_game()

## Inventory to be implemented in the future
# def display_inventory():
#     gold_amount = 0
#     items = []
#     print("======Inventory=====")
#     print(f"Gold : {gold_amount}")
#     print(f"Items: {items}")
#     print("====================")
#

## Item Shop to be implemented in the future
# def enter_item_shop():
#     item_selection = input("Please select an item you would like to buy\n[1] Health Potion[+5HP] - 10 gold")


# clears the screen

# helper function to clear the screen
def clear_screen():
    os.system('cls')


# helper function to exit the application
def exit_app():
    sys.exit("\nThanks for playing!")

# will start the application
def main():
    start_game()


main()
