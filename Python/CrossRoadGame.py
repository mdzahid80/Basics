import time
from turtle import Screen
from crsrd_player import player
from crsrd_score import Score
from crsrd_car import cars

scrn=Screen()
scrn.setup(width=600, height=600)
scrn.tracer(0)
scrn.bgcolor("black")

plyr=player()
scor=Score()
car=cars()
scrn.listen()
scrn.onkey(key="Up",fun=plyr.move)


game_on=True
while game_on:
    time.sleep(car.carspd)
    scrn.update()
    car.create_car()
    car.move_cars()
    
    for car_actv in car.all_cars:
        if plyr.distance(car_actv) < 20:
            game_on=scor.game_over()

    if plyr.ycor()>=300:
         scor.update()
         plyr.rst()
         car.spd()

scrn.exitonclick()