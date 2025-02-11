from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=3)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 40)

    def move_down(self):
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 40)
