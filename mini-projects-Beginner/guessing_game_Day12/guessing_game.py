import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_difficulty():
    """Prompts the user for difficulty and returns number of attempts."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return EASY_LEVEL_ATTEMPTS if difficulty == "easy" else HARD_LEVEL_ATTEMPTS


def check_guess(guess, target):
    """Returns feedback string based on the guess."""
    if guess < target:
        return "Too Low!"
    elif guess > target:
        return "Too High!"
    else:
        return "Correct"


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    target_number = random.randint(1, 100)
    attempts = set_difficulty()

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        result = check_guess(guess, target_number)

        if result == "Correct":
            print(f"You got it! The answer was {target_number}.")
            return
        else:
            print(result)
            attempts -= 1

    print(f"\nYou've run out of guesses. The correct number was {target_number}. Better luck next time!")


play_game()
