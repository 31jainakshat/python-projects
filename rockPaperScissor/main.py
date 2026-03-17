#!/usr/bin/env python3

import random

# 0 -> Rock, 1 -> Paper, 2 -> Scissor

options = ["rock", "paper", "scissor"]

user_wins = 0
computer_wins = 0

while True:
    user_input = input("\nType Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked:", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("\nYou won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("\nYou won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("\nYou won!")
        user_wins += 1
    else:
        print("\nYou lost!")
        computer_wins += 1

print("\nYou won:", user_wins, "times")
print("\nThe computer won:", computer_wins, "times")
print("\nGood bye!")