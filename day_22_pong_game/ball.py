from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.circle(10)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!!", move=False, align=ALIGNMENT, font=("courier", 20, "normal"))

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()


