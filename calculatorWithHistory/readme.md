# Calculator With History

A simple command-line calculator in Python that supports basic arithmetic and persistent history.

## Features

- Supports operations: `+`, `-`, `*`, `/`
- Input format: `number operator number` (e.g. `8 + 9`)
- View history with `history` (shows most recent first)
- Clear history with `clear`
- Exit with `exit`
- Saves successful calculations to `history.txt`
- Handles invalid input, unsupported operators, and divide-by-zero errors

## How to Run

```bash
cd "calculatorWithHistory"
python3 main.py
```

## Usage

1. Run the app.
2. Enter calculations:
   - `5 + 3`
   - `10 / 2`
   - `7 * 8`
3. Use commands:
   - `history` — show saved calculations in reverse order
   - `clear` — clear saved history
   - `exit` — quit program

## Data Persistence

Successful calculations are appended to `history.txt` as:

```
8 + 9 = 17
```

## Notes

- If your input format is invalid, the app shows:
  - `Invalid input. Use format: number operator number (e.g 8 + 9)`
- For unsupported operators, it shows:
  - `Invalid operator. use only + - * /`
- For division by zero, it shows:
  - `Cannot divide by 0`
