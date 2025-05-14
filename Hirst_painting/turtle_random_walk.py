# Random walk
import turtle as t
import random

color_list = [
    "yellow",
    "gold",
    "orange",
    "red",
    "maroon",
    "violet",
    "magenta",
    "purple",
    "navy",
    "blue",
    "skyblue",
    "cyan",
    "turquoise",
    "lightgreen",
    "green",
    "darkgreen",
    "chocolate",
    "brown",
    "black",
    "gray",
]

directions = [0, 90, 180, 270]

timmy = t.Turtle()
timmy.speed("fastest")
timmy.pensize(12)


def random_walk(n):
    for _ in range(n):
        timmy.color(random.choice(color_list))
        timmy.forward(20)
        timmy.setheading(random.choice(directions))


random_walk(200)


screen = t.Screen()
screen.exitonclick()
