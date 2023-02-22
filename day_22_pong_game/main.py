from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("PING PONG GAME")
screen.bgcolor("black")
screen.setup(800, 600)

paddle = Turtle()
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()

screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

scoreboard = Scoreboard()

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right wall (r_paddle missed)
    if ball.xcor() > 380:
        ball.reset_position()
        screen.update()
        scoreboard.l_point()

    # detect collision with left wall (l_paddle missed)
    if ball.xcor() < -380:
        ball.reset_position()
        screen.update()
        scoreboard.r_point()

    # detect collision with r_paddle and l_paddle
    if (ball.distance(r_paddle) < 100 and ball.xcor() > 320) or (ball.distance(l_paddle) < 100 and ball.xcor() < -320):
        ball.bounce_x()


screen.exitonclick()

