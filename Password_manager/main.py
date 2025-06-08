import json
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
            new_data = {
                website: {
                    "username": username,
                    "password": password,
                }
            }

            try:
                with open(f"{BASEDIR}/data.json", mode="r") as file:
                    # Reading old data
                    save_data = json.load(file)
            except FileNotFoundError:
                with open(f"{BASEDIR}/data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data.
                save_data.update(new_data)

                with open(f"{BASEDIR}/data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(save_data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website = website_entry.get()

    try:
        with open(f"{BASEDIR}/data.json", mode="r") as file:
            save_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in save_data:
            username = save_data[website]["username"]
            password = save_data[website]["password"]

            messagebox.showinfo(
                title="Error", message=f"Username: {username} \n\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for the {website} exist."
            )


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
search_button = Button(
    text="Search", command=search_data, highlightthickness=0, borderwidth=0, width=13
)
search_button.grid(row=1, column=2)

generate_pw_button = Button(
    text="Generate Password",
    command=generate_pw,
    highlightthickness=0,
    borderwidth=0,
    width=13,
)
generate_pw_button.grid(row=3, column=2)

add_button = Button(
    text="Add", command=save, width=36, highlightthickness=0, borderwidth=0
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
