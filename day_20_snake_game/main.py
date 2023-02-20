from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snaky = Snake()
food = Food()
screen = Screen()
score = Scoreboard()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(8)
screen.bgcolor('black')
screen.title('Nokia Snake Game')

screen.onkey(snaky.up, "Up")
screen.onkey(snaky.down, "Down")
screen.onkey(snaky.left, "Left")
screen.onkey(snaky.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snaky.move()

    # detect collision with food
    if snaky.head.distance(food) < 15:
        score.increase_score()
        snaky.extend()
        food.refresh()

    # detect collision with wall
    if snaky.head.xcor() > 280 or snaky.head.xcor() < -280 or snaky.head.ycor() > 280 or snaky.head.ycor() < -280:
        is_game_on = False

    # detect collision with own tail
    for segment in snaky.segments[1:]:
        if snaky.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

score.game_over()



screen.exitonclick()