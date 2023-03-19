from turtle import Turtle
class paddle(Turtle):
    def __init__(self,x):
        super().__init__("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x,0)

    # def __init__(self,x):
    #     self.rt_paddle=Turtle("square")
    #     self.rt_paddle.hideturtle()
    #     self.rt_paddle.shapesize(1,5)
    #     self.rt_paddle.penup()
    #     self.rt_paddle.goto(x,0)
    #     self.rt_paddle.left(90)
    #     self.rt_paddle.showturtle()

    def fwd(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def bwd(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)