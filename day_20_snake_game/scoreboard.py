from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!", move=False, align=ALIGNMENT, font=("courier", 20, "normal"))
        self.goto(0, -40)
        self.write(f"Final score: {self.score}", move=False, align=ALIGNMENT, font=("courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
