import turtle as t
import random

# tim = t.Turtle()
#
#
# def forward():
#     tim.forward(20)
#
#
# def backward():
#     tim.backward(20)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen = t.Screen()
# screen.listen()
# screen.onkey(forward, 'w')
# screen.onkey(backward, 's')
# screen.onkey(turn_left, 'a')
# screen.onkey(turn_right, 'd')
# screen.onkey(clear, 'c')
# screen.exitonclick()

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter your color: ")
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = []

pos = -3
for i in range(len(colors)):
    tim = t.Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=pos*30)
    pos += 1
    turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


if winner == user_bet:
    print(f"You won the bet.")
else:
    print(f"You lost the bet.")
print(f"{winner} won the race.")



screen.exitonclick()


