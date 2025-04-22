
import os

with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()

with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

for name in names:
    letter = starting_letter.replace('[name]', name)
    os.makedirs("Output/ReadyToSend", exist_ok=True)

    url = f"Output/ReadyToSend/letter_for_{name}.txt"
    with open(url, mode='w') as file:
        file.write(letter)
