from turtle import Turtle
import random

class Food(Turtle):#initialisation of food at some random position
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5,0.3)
        self.penup()
        self.color("red")
        self.renew()

    def renew(self):#after collision get food object at new position
        self.xcoor=random.randint(-275,275)
        self.ycoor=random.randint(-275,275)
        self.goto(self.xcoor,self.ycoor)
    

