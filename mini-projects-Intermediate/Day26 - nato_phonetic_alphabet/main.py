import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row['letter']:row['code'] for  (index, row) in data.iterrows() }

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("write a word:").upper()
phonetic_list = [new_dict[char] for char in user_input]
print(phonetic_list)