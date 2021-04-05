import random
# dictionary storing the playable classes in the game
playable_classes = {
    "warrior": {
        "id": "1",
        "about": "Warriors are melee fighters highly trained in the art of weaponry. Melee combat is the warrior's "
                 "strongest skill. They are strong and quick on the battlefield.",
        "abilities": [{"Mortal Strike": 5}, {"Blade Storm": 9}],
        "hp": 25
    },
    "mage": {
        "id": 2,
        "about": "A caster that specializes in burst damage and area of effect spells.",
        "abilities": [{"Frost_Bolt": 2}, {"Fire Ball": 7}],
        "hp": 30
    },
    "hunter": {
        "id": "3",
        "about": "Hunters battle their foes at a distance or up close, commanding their pets to attack while they "
                 "nock their arrows.",
        "abilities": [{"Arcane Shot": 10}, {"Pet Attack": 8}],
        "hp": 19
    },
    "druid": {
        "id": "4",
        "about": "Druids harness the vast powers of nature to preserve balance and protect life. With experience, "
                 "druids can unleash nature’s raw energy against their enemies.",
        "abilities": [{"Moon Fire": 10}, {"Star Surge": 8}],
        "hp": 45
    }
}


# function to display classes to the user
def display_classes():
    for current_class in playable_classes:
        for class_atr in playable_classes[current_class]:
            if class_atr == "id":
                print(f"{current_class} ")


# function to display information about a specific class
def display_class_info(class_name):
    selected_class = playable_classes[class_name]
    class_lore = selected_class["about"]
    class_abilities = selected_class["abilities"]
    print("\n*********************************************")
    print(f"You have selected the {class_name} class!\n\n{class_lore}\n\nThe {class_name}'s abilities are :\n"
          f"{class_abilities}")
    print("*********************************************")


# function to generate a random opponent in the arena
def random_challenger_selector():
    random_challenger_list = []
    for each_class in playable_classes:
        random_challenger_list.append(each_class)
    challenger_selected = random_challenger_list[random.randint(0, len(random_challenger_list) - 1)]
    # print(random_challenger_list)
    # print(len(random_challenger_list))
    # print(challenger_selected)
    return challenger_selected


# function to select a random ability from a given opponent
def random_challenger_ability(random_challenger):
    abilities = playable_classes[random_challenger]["abilities"]
    random_ability = get_abilities(random_challenger, random.randint(0, len(abilities) - 1))
    # print(playable_classes[random_challenger]["abilities"][random.randint(0, random_ability) - 1])
    random_ability_damage = attack(random_ability)  # will return the number associated with the move
    print(f"The enemy {random_challenger} used {random_ability} dealing {random_ability_damage} damage ", end='')
    return random_ability_damage


# function to display the player's current class abilities
def display_abilities(player_class):
    class_abilities = playable_classes[player_class]["abilities"]
    for each_ability in class_abilities:
        class_abilities_index = playable_classes[player_class]["abilities"].index(each_ability)
        print(f"{class_abilities_index}: {each_ability}")


# helper function used in class_selection() ../battle_arena.py
def playable_character_list():
    random_challenger_list = []
    for each_class in playable_classes:
        random_challenger_list.append(each_class)
    return random_challenger_list

# helper function to return an ability at a specified index. // currently not being used
def use_ability(index_of_ability, player_class):
    abilities = playable_classes[player_class]["abilities"][index_of_ability]
    return f"{player_class} used {abilities}"

# function that starts the battle scenario between the player and a random opponent
def start_battle(random_challenger, player_class):
    enemy_hp = playable_classes[random_challenger]["hp"]
    player_hp = playable_classes[player_class]["hp"]
    print(f"\nEnemy HP: {enemy_hp}")
    print(f"Player HP: {player_hp}")
    ongoing_battle = True
    while ongoing_battle:
        display_abilities(player_class)
        player_ability_selection = input(f"\nSelection: ")
        if player_ability_selection == "0" or player_ability_selection == "1":
            selected_ability = get_abilities(player_class, int(player_ability_selection))
            ability_damage = attack(selected_ability)  # will return the number associated with the move
            enemy_hp -= ability_damage
            print(f"\nYou used {selected_ability} dealing {ability_damage} damage, leaving the {random_challenger} "
                  f"with {enemy_hp} HP!\n")
            challenger_ability_damage = random_challenger_ability(random_challenger)
            player_hp -= challenger_ability_damage
            print(f"leaving you with {player_hp} HP!\n")
        else:
            print("Invalid Selection. Please choose between [0] and [1]")
        if enemy_hp <= 0:
            print("Congrats you defeated your opponent!\n")
            play_again = input("Would you like to play again?\n[1] YES\n[2] NO\nSelection:")
            ongoing_battle = False
            if play_again == "1":
                return "1"
            elif play_again == "2":
                return "2"
        elif player_hp <= 0:
            print("You have been defeated :(\n")
            play_again = input("Would you like to play again?\n[1] YES\n[2] NO\nSelection: ")
            ongoing_battle = False
            if play_again == "1":
                return "1"
            elif play_again == "2":
                return "2"
        else:
            print("Invalid Selection. Please choose between [0] and [1]")

# returns the ability of a specific class at the abilities index
def get_abilities(player_class, index):
    result = []
    class_abilities = playable_classes[player_class]["abilities"]
    for each_ability in class_abilities:
        for ability in each_ability:
            result.append(ability)
    return result[index]


def attack(move_name):
    return {
        "Mortal Strike": 5,
        "Blade Storm": 9,
        "Frost_Bolt": 2,
        "Fire Ball": 7,
        "Arcane Shot": 10,
        "Pet Attack": 8,
        "Moon Fire": 10,
        "Star Surge": 8
    }[move_name]


# Individual Function Testing Below:

# display_classes()
# display_class_info("druid")
# random_challenger_selector()
# random_challenger_ability(random_challenger_selector())
# Player Abilities
# print(playable_classes["warrior"]["abilities"])
# display_abilities("warrior")
# print(playable_character_list())
# print(use_ability(0,"warrior"))
# display_abilities_and_hp("mage")
# start_battle(random_challenger_selector(), "druid")
# print(attack("Moon Fire"))
# print(get_abilities("mage", 0))
# print(attack("Frost_Bolt"))
# print(attack(get_abilities("mage", 0)))
# ability = playable_classes["druid"]["abilities"][0].keys()
