from turtle import Turtle
start_pos=(0,-280)
move_dist=10

class player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.rst()
        self.setheading(90)
        self.color("cyan")
        self.speed("fastest")
        

    def move(self):
        self.forward(move_dist)

    def rst(self):
        self.goto(start_pos)