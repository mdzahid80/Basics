from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.updatescrbrd()

    def updatescrbrd(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=("Courier" ,80, "normal"))
        self.goto(100,200)
        self.write(self.rscore,align="center",font=("Courier" ,80, "normal"))

    def lpoint(self):
        self.lscore+=1
        self.updatescrbrd()
        
    def rpoint(self):
        self.rscore+=1
        self.updatescrbrd()