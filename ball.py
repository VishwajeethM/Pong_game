from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.x = 10
        self.y = 10
        self.move(self.x, self.y)
        self.move_speed = 0.1

    def hit_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
        else:
            return False

    def move(self, dx, dy):
        self.goto(self.xcor() + dx, self.ycor() + dy)

    def reset_position(self):
        # self.color("white")
        self.goto(0, 0)
        # self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))
        # return True
