import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
score = Scoreboard()
car_manager = CarManager()
screen.listen()

screen.onkeypress(tim.move_up, "Up")

game_is_on = True
i = 0
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # detect collision with car
    for car in car_manager.all_cars:
        if tim.distance(car) < 20:
            score.game_over()
            game_is_on = False

    # detect player reaching other side
    if tim.is_at_finish_line():
        score.increase_score()
        tim.reset_position()
        car_manager.speed_up()



screen.exitonclick()
