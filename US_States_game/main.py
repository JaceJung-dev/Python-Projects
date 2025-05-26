import os
import pandas as pd
import turtle

BASEDIR = os.path.dirname(__file__)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{BASEDIR}/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(f"{BASEDIR}/50_states.csv")
all_states = data["state"].to_list()
guessed_list = []

while len(guessed_list) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_list)}/{len(all_states)} States Correct",
        prompt="What's another State's name?",
    ).title()

    if answer_state == "Exit":
        all_states_set = set(all_states)
        guessed_states_set = set(guessed_list)
        missing_states_set = all_states_set - guessed_states_set
        new_data = pd.DataFrame(missing_states_set)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
