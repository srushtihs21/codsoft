# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 21:38:56 2026

@author: shrey
"""
import random

print("----- ROCK PAPER SCISSORS GAME -----")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()
    
    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")

    else:
        print("You Lose!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing!")
        break

