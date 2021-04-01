#!/usr/bin/env python3
import sys
import os


"""" SHOULD YOU EAT A DONUT FLOWCHART """
# dictionary that contains the questions, answers, and paths
donut_flowchart = {
    "question": ["Do you have a donut? "],
    "answers": {
        "yes": "Eat that donut!",
        "no": "Get a donut"
    }
}


# welcome screen function for user to
def welcome_screen():
    print("\n************************")
    print("Should you have a donut?")
    print("************************\n\nAnswer the questions to see if you should have a donut. :)")
    start_questions()


# start questions function will kick off flowchart logic
def start_questions():
    user_input = input("\n" + donut_flowchart["question"][0]).lower()
    if user_input == "yes":
        print("\n" + donut_flowchart["answers"][user_input])
    elif user_input == "no":
        print("\n" + donut_flowchart["answers"][user_input] + "... then " + donut_flowchart["answers"]["yes"])
    elif user_input == "q":
        exit_app()
    else:
        print("\nInvalid Selection. Please enter yes or no.")
        print("Press Q to exit the application")
        start_questions()
    play_again()


def play_again():
    user_input = input("\nWould you like to know if you should eat another donut? ").lower()
    if user_input == "yes":
        clearScreen()
        welcome_screen()
    elif user_input == "no":
        exit_app()
    else:
        print("\nInvalid Selection. Please enter yes or no.")
        play_again()


def clearScreen():
    os.system('cls')


# helper function to exit the application
def exit_app():
    sys.exit("\nThanks for playing!")


def main():
    welcome_screen()


main()




