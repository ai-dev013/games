# Games

A collection of classic command-line games written in Python.

## Games Available

| Game | Description |
|------|-------------|
| [Tic-Tac-Toe](games/tictactoe.py) | Two-player classic 3×3 grid game |
| [Number Guessing](games/number_guessing.py) | Guess the secret number within a limited number of tries |
| [Rock Paper Scissors](games/rock_paper_scissors.py) | Play against the computer in best-of-N rounds |
| [Connect Four](games/connect_four.py) | Two-player token-drop game on a 6×7 grid — get 4 in a row to win |

## Requirements

- Python 3.8 or later
- No third-party packages required

## How to Run

```bash
# Tic-Tac-Toe (two players on the same machine)
python games/tictactoe.py

# Number Guessing Game
python games/number_guessing.py

# Rock Paper Scissors
python games/rock_paper_scissors.py

# Connect Four (two players on the same machine)
python games/connect_four.py
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Project Structure

```
games/
├── README.md
├── games/
│   ├── __init__.py
│   ├── tictactoe.py
│   ├── number_guessing.py
│   ├── rock_paper_scissors.py
│   └── connect_four.py
└── tests/
    ├── __init__.py
    ├── test_tictactoe.py
    ├── test_number_guessing.py
    ├── test_rock_paper_scissors.py
    └── test_connect_four.py
```
