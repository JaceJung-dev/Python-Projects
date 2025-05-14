import turtle as t
import random
from color_data import color_list

t.colormode(255)
timmy = t.Turtle()

timmy.speed("fastest")

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(325)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()
