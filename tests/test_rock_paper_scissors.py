"""Tests for the Rock Paper Scissors game."""

import random
import pytest
from games.rock_paper_scissors import (
    CHOICES,
    BEATS,
    get_computer_choice,
    determine_round_result,
    play_game,
)


class TestGetComputerChoice:
    def test_valid_choice(self):
        rng = random.Random(7)
        choice = get_computer_choice(rng)
        assert choice in CHOICES

    def test_reproducible_with_seed(self):
        rng1 = random.Random(123)
        rng2 = random.Random(123)
        assert get_computer_choice(rng1) == get_computer_choice(rng2)


class TestDetermineRoundResult:
    @pytest.mark.parametrize("player,computer", [
        ("rock", "rock"),
        ("paper", "paper"),
        ("scissors", "scissors"),
    ])
    def test_tie(self, player, computer):
        assert determine_round_result(player, computer) == "tie"

    @pytest.mark.parametrize("player,computer", [
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    ])
    def test_player_wins(self, player, computer):
        assert determine_round_result(player, computer) == "player"

    @pytest.mark.parametrize("player,computer", [
        ("scissors", "rock"),
        ("rock", "paper"),
        ("paper", "scissors"),
    ])
    def test_computer_wins(self, player, computer):
        assert determine_round_result(player, computer) == "computer"


class TestPlayGame:
    def test_player_wins_series(self, monkeypatch):
        # Computer always picks rock; player always picks paper → player wins
        rng = random.Random()
        rng.choice = lambda seq: "rock"
        inputs = iter(["paper"] * 10)
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_game(rounds=3, rng=rng)
        assert result == "player"

    def test_computer_wins_series(self, monkeypatch):
        # Computer always picks scissors; player always picks rock → player wins
        # Wait — rock beats scissors, so let's flip:
        # Computer always picks paper; player always picks rock → computer wins
        rng = random.Random()
        rng.choice = lambda seq: "paper"
        inputs = iter(["rock"] * 10)
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_game(rounds=3, rng=rng)
        assert result == "computer"
