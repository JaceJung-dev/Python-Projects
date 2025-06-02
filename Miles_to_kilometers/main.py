from tkinter import *


def convert_miles_to_kilo():
    miles = float(miles_input.get())
    km = miles * 1.609344
    converted_value_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

converted_value_label = Label(text="0")
converted_value_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=convert_miles_to_kilo)
button.grid(column=1, row=2)

window.mainloop()
