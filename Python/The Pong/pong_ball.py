from turtle import Turtle

class ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("black")
        self.penup()
        self.xmove=10
        self.ymove=10

    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx,newy)

    def xbounce(self):
        self.xmove= self.xmove*(-1)
    def ybounce(self):
       self.ymove*=-1
    
    def resetL(self):
        self.goto(0,0)
        self.xbounce()

    def resetR(self):
        self.goto(0,0)
        self.xbounce()


        
    
