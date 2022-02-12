from turtle import  Turtle,Screen
class Score(Turtle):

    def __init__(self,pos,scor):
        super().__init__()
        Screen().tracer(0)
        if pos == "right":
            self.goto(250, 250)
        elif pos == "left":
            self.goto(-250,250)
        self.hideturtle()
        self.penup()
        self.score = scor
        self.color("white")
        self.write(f"Score: {self.score}",False)
        Screen().update()
    def splus(self,position):
        self.clear()
        self.__init__(position,self.score + 1)
        Screen().update()

