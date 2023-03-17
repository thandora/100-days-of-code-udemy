import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dict from dataframe where key-value pair are the letters-code.
nato_alphabet = {row["letter"]: row["code"] for (i, row) in data.iterrows()}

user_input = input("Enter a word: ")
# Create a list of the phonetic code words from a word that the user inputs.
nato_name = [nato_alphabet[letter.upper()] for letter in user_input]

print(nato_name)
