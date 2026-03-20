"""Tests for the Tic-Tac-Toe game."""

import pytest
from games.tictactoe import (
    make_board,
    check_winner,
    display_board,
    EMPTY,
)


def _board(*moves):
    """Build a board by applying (player, position) tuples in order."""
    board = make_board()
    for player, pos in moves:
        board[pos] = player
    return board


class TestMakeBoard:
    def test_length(self):
        assert len(make_board()) == 9

    def test_all_empty(self):
        board = make_board()
        assert all(cell == EMPTY for cell in board)


class TestCheckWinner:
    def test_no_winner_at_start(self):
        assert check_winner(make_board()) is None

    def test_x_wins_row(self):
        board = _board(("X", 0), ("X", 1), ("X", 2))
        assert check_winner(board) == "X"

    def test_o_wins_column(self):
        board = _board(("O", 0), ("O", 3), ("O", 6))
        assert check_winner(board) == "O"

    def test_x_wins_diagonal(self):
        board = _board(("X", 0), ("X", 4), ("X", 8))
        assert check_winner(board) == "X"

    def test_x_wins_anti_diagonal(self):
        board = _board(("X", 2), ("X", 4), ("X", 6))
        assert check_winner(board) == "X"

    def test_draw(self):
        # X O X
        # X X O
        # O X O
        board = ["X", "O", "X",
                 "X", "X", "O",
                 "O", "X", "O"]
        assert check_winner(board) == "draw"

    def test_game_in_progress(self):
        board = _board(("X", 0), ("O", 1))
        assert check_winner(board) is None


class TestDisplayBoard:
    def test_display_does_not_raise(self, capsys):
        board = make_board()
        display_board(board)
        captured = capsys.readouterr()
        assert "|" in captured.out
