from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("courier", 25, "normal"))
