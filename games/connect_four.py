"""Connect Four: two-player, command-line, 6×7 token-drop game."""

import sys

ROWS = 6
COLS = 7
EMPTY = "."
TOKENS = ("X", "O")


def make_board():
    """Return a fresh ROWS×COLS board as a list of lists."""
    return [[EMPTY] * COLS for _ in range(ROWS)]


def display_board(board):
    """Print the board with column numbers to stdout."""
    col_numbers = " ".join(str(c + 1) for c in range(COLS))
    print(f" {col_numbers}")
    for row in board:
        print("|" + " ".join(row) + "|")


def drop_token(board, col, token):
    """Drop *token* into *col* (0-indexed).

    Returns the row index where the token landed, or -1 if the column is full.
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = token
            return row
    return -1


def check_winner(board):
    """Return the winning token symbol, 'draw', or None if the game continues."""
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            token = board[r][c]
            if token != EMPTY and all(board[r][c + k] == token for k in range(4)):
                return token

    # Check vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            token = board[r][c]
            if token != EMPTY and all(board[r + k][c] == token for k in range(4)):
                return token

    # Check diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            token = board[r][c]
            if token != EMPTY and all(board[r + k][c + k] == token for k in range(4)):
                return token

    # Check diagonal (down-left)
    for r in range(ROWS - 3):
        for c in range(3, COLS):
            token = board[r][c]
            if token != EMPTY and all(board[r + k][c - k] == token for k in range(4)):
                return token

    # Draw: no empty cells remain
    if all(board[r][c] != EMPTY for r in range(ROWS) for c in range(COLS)):
        return "draw"

    return None


def get_column(board, player):
    """Prompt *player* for a valid column (1-COLS) and return it as 0-indexed."""
    while True:
        raw = input(f"Player {player}, choose column (1-{COLS}): ").strip()
        if not raw.isdigit():
            print(f"  Please enter a number between 1 and {COLS}.")
            continue
        col = int(raw) - 1
        if col < 0 or col >= COLS:
            print(f"  Column must be between 1 and {COLS}.")
            continue
        if drop_token([row[:] for row in board], col, "?") == -1:
            print("  That column is full. Choose another.")
            continue
        return col


def play_game():
    """Run a single game of Connect Four and return the result ('X', 'O', or 'draw')."""
    board = make_board()
    print("\nConnect Four")
    print(f"Drop your token into a column to get 4 in a row!\n")

    for turn in range(ROWS * COLS):
        player = TOKENS[turn % 2]
        display_board(board)
        print()
        col = get_column(board, player)
        drop_token(board, col, player)
        result = check_winner(board)
        if result is not None:
            display_board(board)
            if result == "draw":
                print("\nIt's a draw!")
            else:
                print(f"\nPlayer {result} wins!")
            return result

    return "draw"  # unreachable but satisfies type checkers


def main():
    """Entry point: play until the users quit."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            sys.exit(0)


if __name__ == "__main__":
    main()
