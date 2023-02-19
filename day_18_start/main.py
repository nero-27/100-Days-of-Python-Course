import turtle
import turtle as t
import random


# def draw_turtle(s, a):
#     tim = Turtle()
#     tim.shape("arrow")
#     tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     for i in range(s):
#         tim.right(a)
#         tim.forward(100)
#
#
# total = 360
# side = 3
#
# screen = Screen()
# screen.colormode(255)
#
# while side < 8:
#     angle = total // side
#     draw_turtle(side, angle)
#     side += 1
#
#
# screen.exitonclick()

# ------------------------------------------------------------

# angles = [0, 90, 180, 270, 360]
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors
#
#
# tim = t.Turtle()
# t.colormode(255)
# tim.speed(8)
# tim.shape("turtle")
# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(angles))
#     tim.width(4)
#     tim.forward(15)
#
# screen = t.Screen()
# screen.exitonclick()

# ------------------------------------------------------


radius = 100
t.colormode(255)
tim = t.Turtle()
tim.speed(20)

angle = 5
n = 360 // angle
while True:
    tim.circle(radius)
    tim.color(random_color())
    tim.tilt(angle)
    tim.right(angle)
    n -= 1
    if n == 0:
        break



