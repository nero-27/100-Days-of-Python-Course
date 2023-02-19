import colorgram
import turtle as t
import random

color_list = [(236, 235, 240), (236, 231, 234), (222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169), (162, 168, 75), (117, 122, 148), (185, 188, 206), (88, 141, 158)]

tim = t.Turtle()
screen = t.Screen()
tim.speed(7)
t.colormode(255)
tim.hideturtle()
rows = 10
spaces = 50
tim.penup()
tim.goto(0-screen.window_width() // 4, 0-screen.window_height() // 4)

for i in range(1, rows+1):
    for _ in range(rows):
        # draw a dot
        tim.pendown()
        tim.dot(25, random.choice(color_list))
        # move 50 spaces to right
        tim.penup()
        tim.forward(spaces)


    # move 10*50 spaces left
    tim.left(180)
    tim.forward(spaces*rows)
    tim.right(90)
    tim.forward(spaces)
    tim.right(90)



