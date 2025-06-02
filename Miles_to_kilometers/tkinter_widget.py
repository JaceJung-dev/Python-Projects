from tkinter import *

# Creating a new window and config.
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Label
label = Label(text="Original text")
label.config(text="Modified text")
label.pack()


# Button
## Define the action to be executed when the button is clicked.
def action():
    print("Do Something")


button = Button(text="click me", command=action)
button.pack()

# Entry
entry = Entry(width=20)
## Add some text to begin with.
entry.insert(END, string="Some text to begin with.")
entry.pack()
## Get text in entry
entry_value = entry.get()
print(entry_value)

# Text
text = Text(height=5, width=30)
text.pack()
## Put cursor in textbox.
text.focus()
## Add some text to begin with.
text.insert(END, "Multi-line text entry.")
# Retrieve all text from the beginning (line 1, character 0) to the end of the textbox
text_value = text.get("1.0", END)
print(text_value)


# Spinbox
def spinbox_used():
    # get the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check button
def checkbutton_used():
    # Print 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checkbox. 0 = ed
radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Get current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
