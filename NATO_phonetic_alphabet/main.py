import os
import pandas as pd

BASEDIR = os.path.dirname(__file__)

df = pd.read_csv(f"{BASEDIR}/nato_phonetic_alphabet.csv")

phonetic_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_word = input("Type a word: ").upper()
converted_word = [phonetic_alphabet_dict[char] for char in user_word]
print(converted_word)
