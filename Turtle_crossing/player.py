from turtle import Turtle

STARTING_DIRECTION = 90
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(STARTING_DIRECTION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        if self.ycor() > 280:
            return True
        else:
            return False
