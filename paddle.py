from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        if position == "right".lower():
            self.create(350)
        else:
            self.create(-350)

    def create(self,position):
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(x=position, y=0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        y= self.ycor() +20
        self.goto(self.xcor(),y)

    def down(self):
        y= self.ycor() - 20
        self.goto(self.xcor(),y)


