"""Rock Paper Scissors: play against the computer in best-of-N rounds."""

import random
import sys

CHOICES = ("rock", "paper", "scissors")
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_computer_choice(rng=None):
    """Return a random choice for the computer."""
    if rng is None:
        return random.choice(CHOICES)
    return rng.choice(CHOICES)


def determine_round_result(player, computer):
    """Return 'player', 'computer', or 'tie' for a single round."""
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "player"
    return "computer"


def get_player_choice():
    """Prompt the user and return their validated choice."""
    options = ", ".join(CHOICES)
    while True:
        raw = input(f"Your choice ({options}): ").strip().lower()
        if raw in CHOICES:
            return raw
        print(f"  Invalid choice. Please enter one of: {options}")


def play_game(rounds=3, rng=None):
    """Play a best-of-*rounds* series.

    Returns 'player' if the player wins the series, 'computer' otherwise.
    """
    wins_needed = rounds // 2 + 1
    player_wins = 0
    computer_wins = 0
    round_num = 0

    print(f"\nRock Paper Scissors  (best of {rounds})\n")

    while player_wins < wins_needed and computer_wins < wins_needed:
        round_num += 1
        print(f"--- Round {round_num} ---")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice(rng)
        print(f"  Computer chose: {computer_choice}")

        result = determine_round_result(player_choice, computer_choice)
        if result == "player":
            player_wins += 1
            print("  You win this round!")
        elif result == "computer":
            computer_wins += 1
            print("  Computer wins this round!")
        else:
            print("  It's a tie!")

        print(f"  Score — You: {player_wins}  Computer: {computer_wins}\n")

    if player_wins > computer_wins:
        print("You win the series!")
        return "player"
    else:
        print("Computer wins the series!")
        return "computer"


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
