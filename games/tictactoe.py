"""Tic-Tac-Toe: two-player, command-line, 3x3 grid."""

import sys

EMPTY = " "
PLAYERS = ("X", "O")


def make_board():
    """Return a fresh 3x3 board represented as a list of 9 strings."""
    return [EMPTY] * 9


def display_board(board):
    """Print the board to stdout."""
    rows = [board[i * 3 : i * 3 + 3] for i in range(3)]
    separator = "-----------"
    lines = []
    for i, row in enumerate(rows):
        lines.append(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            lines.append(separator)
    print("\n".join(lines))


def check_winner(board):
    """Return the winning player symbol, 'draw', or None if the game continues."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in wins:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "draw"
    return None


def get_move(board, player):
    """Prompt *player* for a valid position (1-9) and return it as 0-indexed."""
    while True:
        raw = input(f"Player {player}, enter position (1-9): ").strip()
        if not raw.isdigit():
            print("  Please enter a number between 1 and 9.")
            continue
        pos = int(raw) - 1
        if pos < 0 or pos > 8:
            print("  Position must be between 1 and 9.")
            continue
        if board[pos] != EMPTY:
            print("  That position is already taken.")
            continue
        return pos


def play_game():
    """Run a single game of Tic-Tac-Toe and return the result ('X', 'O', or 'draw')."""
    board = make_board()
    print("\nTic-Tac-Toe")
    print("Positions are numbered 1-9 left-to-right, top-to-bottom.\n")

    for turn in range(9):
        player = PLAYERS[turn % 2]
        display_board(board)
        print()
        pos = get_move(board, player)
        board[pos] = player
        result = check_winner(board)
        if result is not None:
            display_board(board)
            if result == "draw":
                print("\nIt's a draw!")
            else:
                print(f"\nPlayer {result} wins!")
            return result

    return "draw"


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
