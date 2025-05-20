import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen

RIGHT_STARTING_POS = (350, 0)
LEFT_STARTING_POS = (-350, 0)

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(RIGHT_STARTING_POS)
l_paddle = Paddle(LEFT_STARTING_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with ceiling or floor.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right hand side paddle.
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_y()
        ball.bounce_x()

    # Detect right hand side paddle misses ball.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left hand side paddle misses ball.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
