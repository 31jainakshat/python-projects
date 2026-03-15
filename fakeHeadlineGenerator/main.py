#!/usr/bin/env python3

import random

subjects = [
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A group of Monkeys",
    "Prime minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local train",
    "a plote of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL match",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n" + headline)

    user_input = input("Do you want more news ? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using fake news generator !")