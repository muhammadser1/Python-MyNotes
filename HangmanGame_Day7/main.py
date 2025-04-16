import random

words = [
    "grave", "provision", "mountain", "fan", "horizon", "fund", "familiar",
    "building", "landowner", "soap", "secure", "cell", "wrist", "set", "penny",
    "rally", "exception", "budget", "extension", "overcharge"
]

word = random.choice(words)
lives = 10
res = ["_" for _ in range(len(word))]

print("Welcome to Hangman!")
print(f"Hint: The word has {len(word)} letters.")

while lives:
    print("\nGuess the word:  ", " ".join(res))
    guess = input("Guess a letter: ").lower()

    if guess in res:
        print("You've already guessed that letter.")
        continue

    flag = False
    for i, char in enumerate(word):
        if char == guess:
            res[i] = guess
            flag = True

    if flag:
        print("Correct!")
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")

    if "_" not in res:
        print("\nYou win! The word was:", word)
        break
else:
    print("\nGame over! The word was:", word)
