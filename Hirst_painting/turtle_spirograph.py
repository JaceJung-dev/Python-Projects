# Spirograph
import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy = t.Turtle()
timmy.speed("fastest")


def draw_spirograph(turtle, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph(timmy, 5)

screen = t.Screen()
screen.exitonclick()
