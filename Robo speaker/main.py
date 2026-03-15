#!/usr/bin/env python3

import os

if __name__ == '__main__':
    os.system("say 'Welcome to automated voice tool'")
    while True:
        x = input("Please enter what you want me to speak: ")
        if x == "q":
            os.system("say 'bye bye'")
            break
        command = f"say {x}"
        os.system(command)