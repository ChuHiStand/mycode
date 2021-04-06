#!user/bin/env python3

# imports always go at the top of your code
import requests
import pprint
"""Pokemon API Challenge"""
# The Pokemon API can be found here! https://pokeapi.co/

# THE CHALLENGE
# Use your script to print out the following:

# Change the Pokemon in the URL to a Pokemon of your choice! BONUS- add input to collect what Pokemon to look up!

# Print the URL to "front_default", which is a link to an image of your Pokemon! BONUS- download the image (one tool you could use is the wget module... or write to file with "wb"!)!

# Return a count of how many "game_indices" the selected Pokemon has been in!

# Print out the "name"s of ALL the selected Pokemon's "moves".

def main():
    pokemon_search = input("Please type a pokemon you would like to get more info on!\nSelection: ").lower()
    current_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_search}").json()
    print(f"Picture: {current_pokemon['sprites']['front_default']}")
    print(f"# of Games {pokemon_search} has been in: {len(current_pokemon['game_indices'])}")
    print(f"{pokemon_search}'s moves:")
    for moves in current_pokemon["moves"]:
        print(moves['move']['name'])


main()

