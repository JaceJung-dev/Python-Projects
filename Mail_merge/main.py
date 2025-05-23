import os

BASEDIR = os.path.dirname(__file__)
PLACEHOLDER = "[name]"

with open(f"{BASEDIR}/Input/Names/Invited_names.txt", mode="r") as name_file:
    name_list = name_file.readlines()

with open(f"{BASEDIR}/Input/Letters/letter_template.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(
            f"{BASEDIR}/Output/ReadyToSend/letter_to_{name}.txt", mode="w"
        ) as completed_letter:
            completed_letter.write(new_letter)
