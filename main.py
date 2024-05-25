from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


l_scoreboard = Scoreboard((-100, 200))
r_scoreboard = Scoreboard((100, 200))



screen.listen()

screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)




game_is_on = True
while game_is_on:
    l_scoreboard.l_current_score()
    r_scoreboard.r_current_score()
    time.sleep(0.1)
    ball.move_1()
    screen.update()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect when right paddle misses
    if ball.xcor() >= 380:
        ball.reset_position()
        l_scoreboard.l_score +=1


    #Detect when left paddle misses
    if ball.xcor() <= -380:
        ball.reset_position()
        r_scoreboard.r_score +=1

    if l_scoreboard.l_score == 7 or r_scoreboard.r_score == 7:
        l_scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
