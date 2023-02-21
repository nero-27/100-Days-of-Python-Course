from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (350, 30), (350, 60)]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        # self.segments = []
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position)
        # self.segments.append(segment)

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)



