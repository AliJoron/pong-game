from turtle import Turtle
import time
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create()
        self.xmove = 10
        self.ymove =  10
        self.move_speed = 0.1

    def create(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x, y)
    def bounce(self):
        self.ymove *= -1
    def bouncep(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    def resball(self):
        time.sleep(0.5)
        self.move_speed = 0.1
        self.goto(0,0)
        self.bouncep()
