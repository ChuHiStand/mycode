# 1. Create a new script!
# 2. Include a shebang line.
#!/usr/bin/env python3

# 3. Make your file executable with a ./

# 4. Save a user's input to the variable char_name from the following question:
# Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)
# char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz) ")


# Save a user's input to the variable char_stat from the following question:
#  What statistic do you want to know about? (real name, powers, archenemy)
# char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ")

# Use the char_name and char_stat values to pull the appropriate value from the dictionary below.
heroes= {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
        }


# 7. Create a print function that combines that information into this output:
# <char_name>'s <char_stat> is: <value>
# BONUS 1: When returning the hero's name, have it capitalized appropriately (e.g. Flash, not flash)
# SUPER BONUS 2: Make the user's input error proof!
# MEGA SUPER BONUS 3: Allow the user to try again without exiting the script!

while True:
    char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz) ")
    if char_name in heroes.keys():
        char_name.lower()
        break
        print("Please enter the character name you see on the screen")
while True:
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ")
    if char_stat in heroes[char_name].keys():
        char_name.lower()
        break
        print("Please enter the character stat you see on the screen")

print(f"{char_name}'s {char_stat} is: {heroes[char_name][char_stat]}")
