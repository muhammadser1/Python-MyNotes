# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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
