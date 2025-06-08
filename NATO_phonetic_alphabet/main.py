import os
import pandas as pd

BASEDIR = os.path.dirname(__file__)

df = pd.read_csv(f"{BASEDIR}/nato_phonetic_alphabet.csv")

phonetic_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_word = input("Type a word: ").upper()
    try:
        converted_word = [phonetic_alphabet_dict[char] for char in user_word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(converted_word)


generate_phonetic()
