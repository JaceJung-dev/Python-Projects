import os
import pyperclip
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

BASEDIR = os.path.dirname(__file__)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_number + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail/Username: {username}\nPassword: {password}\n Is it ok to save?",
        )

        if is_ok:
            data = f"{website} | {username} | {password}\n"
            with open(f"{BASEDIR}/data.txt", mode="a") as file:
                file.write(data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=f"{BASEDIR}/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "example@example.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_pw_button = Button(
    text="Generate Password", command=generate_pw, highlightthickness=0, borderwidth=0
)
generate_pw_button.grid(row=3, column=2)

add_button = Button(
    text="Add", command=save, width=36, highlightthickness=0, borderwidth=0
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
