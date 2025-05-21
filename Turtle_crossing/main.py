import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing.
    if player.is_at_finishline():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
