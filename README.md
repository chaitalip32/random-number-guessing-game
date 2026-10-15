# Random Number Guessing Game

A simple command-line number guessing game built with Python. The computer selects a random number, and the player tries to guess it within a limited number of attempts.

## Features

- Generates a random number between 1 and 100.
- Gives the player 7 valid attempts to guess the number.
- Provides hints when a guess is too low or too high.
- Validates non-numeric input and guesses outside the allowed range.
- Reports whether the player wins or runs out of attempts.
- Includes automated tests using Python's built-in `unittest` framework.

## Requirements

- Python 3.8 or later.
- No external Python packages are required because the project uses Python's standard library.

## Getting Started

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/random-number-guessing-game.git
cd random-number-guessing-game
```

Alternatively, download the repository and open its folder in VS Code.

### 2. Run the game

```bash
python game.py
```

On Windows, you can also use:

```bash
py game.py
```

Follow the on-screen prompts to enter your guesses.

## How to Play

1. The computer chooses a random number between 1 and 100.
2. Enter a whole number when prompted.
3. The game tells you whether your guess is too low or too high.
4. Invalid input and numbers outside the allowed range are rejected without consuming an attempt.
5. Guess the number within 7 valid attempts to win.

## Run the Tests

From the project's root directory, run:

```bash
python -m unittest discover -s tests -v
```

On Windows, you can also use:

```bash
py -m unittest discover -s tests -v
```

The tests cover guess-checking logic, winning and losing outcomes, and invalid input handling.

## Project Structure

```text
random-number-guessing-game/
├── game.py
├── tests/
│   └── test_game.py
├── README.md
└── .gitignore
```

## Concepts Practiced

- Variables and constants
- Functions and return values
- Conditional statements and loops
- Input validation and exception handling
- Random number generation
- Automated unit testing and mocking
- Git and GitHub version control

## Possible Future Improvements

- Add difficulty levels.
- Allow players to start another round without restarting the program.
- Track the number of games won.
- Add a graphical user interface.

## Author

**Chaitali Pednekar**

- GitHub: [chaitalip32](https://github.com/chaitalip32)

---

If you find a bug or have a suggestion, feel free to open an issue or submit a pull request.
