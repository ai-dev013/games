"""Tests for the Connect Four game."""

import pytest
from games.connect_four import (
    ROWS,
    COLS,
    EMPTY,
    TOKENS,
    make_board,
    display_board,
    drop_token,
    check_winner,
    play_game,
)


class TestMakeBoard:
    def test_dimensions(self):
        board = make_board()
        assert len(board) == ROWS
        assert all(len(row) == COLS for row in board)

    def test_all_empty(self):
        board = make_board()
        assert all(cell == EMPTY for row in board for cell in row)


class TestDropToken:
    def test_token_lands_at_bottom(self):
        board = make_board()
        row = drop_token(board, 0, "X")
        assert row == ROWS - 1
        assert board[ROWS - 1][0] == "X"

    def test_token_stacks(self):
        board = make_board()
        drop_token(board, 3, "X")
        row = drop_token(board, 3, "O")
        assert row == ROWS - 2
        assert board[ROWS - 2][3] == "O"

    def test_full_column_returns_minus_one(self):
        board = make_board()
        for _ in range(ROWS):
            drop_token(board, 0, "X")
        assert drop_token(board, 0, "O") == -1


class TestCheckWinner:
    def test_no_winner_at_start(self):
        assert check_winner(make_board()) is None

    def _place_row(self, board, row, start_col, token, length=4):
        for i in range(length):
            board[row][start_col + i] = token

    def test_horizontal_win(self):
        board = make_board()
        self._place_row(board, ROWS - 1, 0, "X")
        assert check_winner(board) == "X"

    def test_vertical_win(self):
        board = make_board()
        for r in range(4):
            board[r][0] = "O"
        assert check_winner(board) == "O"

    def test_diagonal_down_right_win(self):
        board = make_board()
        for k in range(4):
            board[k][k] = "X"
        assert check_winner(board) == "X"

    def test_diagonal_down_left_win(self):
        board = make_board()
        for k in range(4):
            board[k][3 - k] = "O"
        assert check_winner(board) == "O"

    def test_draw(self):
        # Known draw layout: even rows → XXXOXXX, odd rows → OOOXOOO.
        # No run of 4 identical tokens exists in any direction.
        board = make_board()
        for r in range(ROWS):
            if r % 2 == 0:
                board[r] = ["X", "X", "X", "O", "X", "X", "X"]
            else:
                board[r] = ["O", "O", "O", "X", "O", "O", "O"]
        assert check_winner(board) == "draw"

    def test_game_in_progress(self):
        board = make_board()
        drop_token(board, 0, "X")
        drop_token(board, 1, "O")
        assert check_winner(board) is None


class TestDisplayBoard:
    def test_display_does_not_raise(self, capsys):
        board = make_board()
        display_board(board)
        captured = capsys.readouterr()
        assert "|" in captured.out

    def test_display_shows_column_numbers(self, capsys):
        board = make_board()
        display_board(board)
        captured = capsys.readouterr()
        assert "1" in captured.out
        assert str(COLS) in captured.out


class TestPlayGame:
    def test_player_x_wins(self, monkeypatch):
        # X drops into col 0 four times; O drops into col 1 three times
        # Sequence: X→col0, O→col1, X→col0, O→col1, X→col0, O→col1, X→col0 → X wins vertically
        inputs = iter(["1", "2"] * 3 + ["1"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_game()
        assert result == "X"

    def test_player_o_wins(self, monkeypatch):
        # O wins vertically in col 2; X spreads across cols 1,3,4,5 to avoid early win.
        # Sequence: X→1, O→2, X→3, O→2, X→4, O→2, X→5, O→2 → O gets 4 in col 2.
        inputs = iter(["1", "2", "3", "2", "4", "2", "5", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_game()
        assert result == "O"
