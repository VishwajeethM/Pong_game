from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

score = Scoreboard()
screen = Screen()

l_pad = Paddle((-380, 0))
r_pad = Paddle((380, 0))
ball = Ball()

screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong game")

screen.listen()

screen.onkey(l_pad.move_up, "w")
screen.onkey(l_pad.move_down, "s")

screen.onkey(r_pad.move_up, "Up")
screen.onkey(r_pad.move_down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move(dx=ball.x, dy=ball.y)

    # Detect collision with wall(above and below)
    if ball.hit_wall():
        ball.y *= -1

    # Ball out of bounds

    # R_ball misses
    if ball.xcor() > 395:
        ball.reset_position()
        ball.x *= -1
        score.l_score += 1
        score.show_score()

    # L_ball misses
    if ball.xcor() < -395:
        ball.reset_position()
        ball.x *= -1
        score.r_score += 1
        score.show_score()

    # Ball hits paddle
    if ball.distance(r_pad) < 50 and ball.xcor() > 355 or ball.distance(l_pad) < 50 and ball.xcor() < -355:
        ball.x *= -1
        ball.move_speed *= 0.9

screen.exitonclick()
