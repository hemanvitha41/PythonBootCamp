from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

range_y = [0, 60, -60, 120, -120, 180, -180, 240, -240]

for i in range(9):
    line = Turtle()
    line.penup()
    line.shape("square")
    line.color("white")
    line.shapesize(stretch_wid=2, stretch_len=0.1)
    line.goto(0, range_y[i])
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle()
l_paddle = Paddle()
r_paddle.goto(350, 0)
l_paddle.goto(-350, 0)
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_ball()
        score_board.left_score()

    # Detect if left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_ball()
        score_board.right_score()

screen.exitonclick()