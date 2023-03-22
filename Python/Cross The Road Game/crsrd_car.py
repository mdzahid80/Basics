from turtle import Turtle
import time
import random

colr=["green","yellow","blue","orange","white","pink"]
movedist=5
moveinc=10

class cars():
    def __init__(self):
        self.all_cars=[]
        self.carspd=0.1

    def create_car(self):
        randnum=random.randint(1,6)
        if randnum==1:
            nwcar=Turtle("square")
            nwcar.penup()
            nwcar.shapesize(stretch_wid=1,stretch_len=2)
            nwcar.color(random.choice(colr))
            rnd_y=random.randint(-250,250)
            nwcar.goto(300,rnd_y)
            self.all_cars.append(nwcar)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(movedist)

    def spd(self):
        self.carspd*=0.9
        
        