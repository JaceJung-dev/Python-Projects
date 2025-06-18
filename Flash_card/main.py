import os
import random
import pandas as pd
import tkinter as tk
from tkinter import PhotoImage

BASE_DIR = os.path.dirname(__file__)
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv(f"{BASE_DIR}/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(f"{BASE_DIR}/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(f"{BASE_DIR}/data/words_to_learn.csv", index=False)
    next_card()


# Window
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = tk.Canvas(width=800, height=526)
card_front_img = PhotoImage(file=f"{BASE_DIR}/images/card_front.png")
card_back_img = PhotoImage(file=f"{BASE_DIR}/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="Title", fill="black", font=("Helvetica", 40, "italic")
)
card_word = canvas.create_text(
    400, 263, text="word", fill="black", font=("Helvetica", 60, "bold")
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
unknown_img = PhotoImage(file=f"{BASE_DIR}/images/wrong.png")
unknown_button = tk.Button(
    image=unknown_img, command=next_card, highlightthickness=0, borderwidth=0
)
unknown_button.grid(row=1, column=0)

known_img = PhotoImage(file=f"{BASE_DIR}/images/right.png")
known_button = tk.Button(
    image=known_img, command=is_known, highlightthickness=0, borderwidth=0
)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
