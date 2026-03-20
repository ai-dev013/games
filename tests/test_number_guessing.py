"""Tests for the Number Guessing game."""

import random
import pytest
from games.number_guessing import (
    generate_secret,
    evaluate_guess,
    play_game,
    DEFAULT_LOW,
    DEFAULT_HIGH,
    DEFAULT_MAX_TRIES,
)


class TestGenerateSecret:
    def test_within_range(self):
        rng = random.Random(42)
        for _ in range(100):
            secret = generate_secret(1, 10, rng)
            assert 1 <= secret <= 10

    def test_uses_rng(self):
        rng = random.Random(0)
        s1 = generate_secret(1, 100, rng)
        rng = random.Random(0)
        s2 = generate_secret(1, 100, rng)
        assert s1 == s2


class TestEvaluateGuess:
    def test_correct(self):
        assert evaluate_guess(42, 42) == "correct"

    def test_too_low(self):
        assert evaluate_guess(50, 30) == "too_low"

    def test_too_high(self):
        assert evaluate_guess(30, 50) == "too_high"


class TestPlayGame:
    def test_win_on_first_try(self, monkeypatch):
        rng = random.Random()
        rng.randint = lambda a, b: 42
        inputs = iter(["42"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_game(low=1, high=100, max_tries=7, rng=rng)
        assert result == 1

    def test_fail_to_guess(self, monkeypatch):
        rng = random.Random()
        rng.randint = lambda a, b: 99
        inputs = iter(["1", "2", "3"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_game(low=1, high=100, max_tries=3, rng=rng)
        assert result < 0
