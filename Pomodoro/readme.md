# Pomodoro GUI Application

## What I learn
- How to work with the Canvas widget and add images in Tkinter
- How to implement a countdown mechanism in Python and Tkinter
- How to create dynamic typing effects in a Tkinter application

## Code Example in Action
### Count down

```python
import time

def count_down(count):
    while count >= 0:
        print(count)
        count -= 1
        time.sleep(1)
    
count_down(5)
```

- The code above does not execute immediately in GUI or event-driven environments.

```python
from tkinter import *

def count_down(count):
    label.config(text=str(count))
    
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        label.config(text="Time's up!")

# Create the main window
window = Tk()

# Create and place a label
label = Label(window, font=("Courier", 40))
label.pack()

# Start countdown
count_down(5)

window.mainloop()
```
- `after()` schedules function calls without freezing the interface.
- Countdown updates the label every second without blocking the main loop.

### Dynamic typing
Dynamic typing is a feature of some programming languages where you don’t need to declare a variable’s type explicitly.

- The type of a variable is inferred from the assigned value.
- A variable can change its type during program execution.
- It leads to more flexible and concise code, but also requires careful handling to avoid runtime errors.

```python
x = 10       # x is an integer
x = "hello"  # now x is a string
```