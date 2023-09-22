from turtle import Screen
from pong.paddle import Paddle
from pong.ball import Ball
from pong.scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Jovahnn's Game of Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collison with the wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()

    #Detect collison with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    #Detect when Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
