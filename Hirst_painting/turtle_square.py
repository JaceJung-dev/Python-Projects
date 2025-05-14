# Drawing a Square
import turtle as t

timmy = t.Turtle()

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = t.Screen()
screen.exitonclick()
