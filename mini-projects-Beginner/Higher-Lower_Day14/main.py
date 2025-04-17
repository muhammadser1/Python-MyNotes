import random

from follower_count import data


def display_data(index):
    person = data[index]
    return f"{person['name']}, {person['description']}, from {person['country']}."


def winner(guess, a, b):
    if data[a]['follower_count'] > data[b]['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


def play():
    score = 0
    first = random.randint(0, len(data) - 1)

    while True:

        while True:
            second = random.randint(0, len(data) - 1)
            if first != second:
                break

        print(f"Compare A: {display_data(first)}")
        print("VS")
        print(f"Against B: {display_data(second)}")

        while True:
            guess = input("Who has more followers? Type 'a' or 'b': ").lower()
            if guess in ['a', 'b']:
                break
            print("Invalid input. Please type 'a' or 'b'.")

        # Check winner
        if winner(guess, first, second):
            score += 1
            print(f"\nYou're right! Current score: {score}.\n")
            first = second
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            break


play()
