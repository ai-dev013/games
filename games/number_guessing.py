"""Number Guessing Game: guess the secret number within a limited number of tries."""

import random
import sys


DEFAULT_LOW = 1
DEFAULT_HIGH = 100
DEFAULT_MAX_TRIES = 7


def generate_secret(low=DEFAULT_LOW, high=DEFAULT_HIGH, rng=None):
    """Return a random integer in [low, high] using *rng* (or the global random)."""
    if rng is None:
        return random.randint(low, high)
    return rng.randint(low, high)


def evaluate_guess(secret, guess):
    """Return 'correct', 'too_low', or 'too_high'."""
    if guess == secret:
        return "correct"
    if guess < secret:
        return "too_low"
    return "too_high"


def get_guess(low, high):
    """Prompt the user for an integer in [low, high] and return it."""
    while True:
        raw = input(f"Enter your guess ({low}-{high}): ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if value < low or value > high:
            print(f"  Your guess must be between {low} and {high}.")
            continue
        return value


def play_game(low=DEFAULT_LOW, high=DEFAULT_HIGH, max_tries=DEFAULT_MAX_TRIES, rng=None):
    """Play one round of the number guessing game.

    Returns the number of guesses taken (negative value means the player
    did not guess correctly within *max_tries*).
    """
    secret = generate_secret(low, high, rng)
    print(f"\nNumber Guessing Game")
    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {max_tries} tries.\n")

    for attempt in range(1, max_tries + 1):
        print(f"Attempt {attempt}/{max_tries}")
        guess = get_guess(low, high)
        result = evaluate_guess(secret, guess)

        if result == "correct":
            print(f"  Correct! You guessed it in {attempt} attempt(s).")
            return attempt
        elif result == "too_low":
            print("  Too low!")
        else:
            print("  Too high!")

    print(f"  Out of tries! The secret number was {secret}.")
    return -max_tries


def main():
    """Entry point: play until the user quits."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            sys.exit(0)


if __name__ == "__main__":
    main()
