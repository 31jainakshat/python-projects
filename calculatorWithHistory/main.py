#!/usr/bin/env python3

HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found")
            else:
                for l in reversed(lines):
                    print(l.strip())
    except FileNotFoundError:
        print("No history found")

def clear_history():
    with open(HISTORY_FILE, 'w'):
        pass
    print("History cleared successfully!")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g 8 + 9)")
        return
    num1 = float(parts[0])
    operator = str(parts[1])
    num2 = float(parts[2])
    result = 0

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by 0")
            return
        result = num1/num2
    elif operator == "*":
        result = num1 * num2
    else:
        print("Invalid operator. use only + - * /")
        return
    
    if int(result) == result:
        result = int(result)
    print("Result: ", result)
    save_to_history(user_input, result)

def main():
    print("Simple calculator (type history, clear or exit) ")
    while True:
        user_input = input("Enter calculation ( + - * / ) or command (history, clear or exit): ")
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()
