#!/usr/bin/env python3
import random


def guess_the_number():
    user_input = int(input("Welcome to the guess the number game. What would you like to guess up to?\nEnter number: "))
    random_number = random.randint(1, user_input)
    user_guess = 0

    while user_guess != random_number:
        user_guess = int(input(f'\nGuess a number between 1 and {user_input}: '))
        if user_guess < random_number:
            print(f'\nThe number {user_guess} is lower than the correct answer. Please pick again')
        elif user_guess > random_number:
            print(f'\nThe number {user_guess} is higher than the correct answer. Please pick again')

    print(f'\nThe number {random_number} is correct. Thank you for playing!')


guess_the_number()
