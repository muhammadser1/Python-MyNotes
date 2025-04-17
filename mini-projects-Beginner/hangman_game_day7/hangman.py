import random


def choose_word():
    words = [
        "grave", "provision", "mountain", "fan", "horizon", "fund", "familiar",
        "building", "landowner", "soap", "secure", "cell", "wrist", "set", "penny",
        "rally", "exception", "budget", "extension", "overcharge"
    ]
    return random.choice(words)


def display_progress(res):
    print("\nGuess the word: ", " ".join(res))


def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            return guess


def update_result(word, guess, res):
    correct = False
    for i, char in enumerate(word):
        if char == guess:
            res[i] = guess
            correct = True
    return correct


def play_hangman():
    word = choose_word()
    lives = 10
    res = ["_" for _ in word]
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"Hint: The word has {len(word)} letters.")

    while lives:
        display_progress(res)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if update_result(word, guess, res):
            print("Correct!")
        else:
            lives -= 1
            print(f"Wrong! Lives left: {lives}")

        if "_" not in res:
            print("\nYou win! The word was:", word)
            break
    else:
        print("\nGame over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
