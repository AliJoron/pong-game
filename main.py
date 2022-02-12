from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
rscore = Score("right",0)
lscore = Score("left",0)
screen.bgcolor("black")
screen.setup(width=800 ,height=600)
screen.title("Pong")
screen.tracer(0)
rpaddle = Paddle("right")
lpaddle = Paddle("left")
ball = Ball()
screen.listen()
screen.onkey(rpaddle.up,"Up")
screen.onkey(rpaddle.down,"Down")
screen.onkey(lpaddle.up,"w")
screen.onkey(lpaddle.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed )
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    if ball.distance(rpaddle) < 50 and ball.xcor() > 330 or ball.distance(lpaddle) < 60 and ball.xcor() < -330:
        ball.bouncep()

    if ball.xcor() > 380:
        ball.resball()
        lscore.splus("left")

    if ball.xcor() < -380:
        ball.resball()
        rscore.splus("right")

screen.exitonclick()