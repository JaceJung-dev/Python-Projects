# Drawing diagrams
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

timmy = t.Turtle()


def draw_diagram(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


def draw_multiple_diagrams(n):
    for n_side in range(3, n + 1):
        timmy.color(random.choice(color_list))
        draw_diagram(n_side)


draw_multiple_diagrams(10)

screen = t.Screen()
screen.exitonclick()
