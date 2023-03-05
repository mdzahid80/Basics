from turtle import Turtle,Screen
import time
from snakeclass import Snake
from snake_food import Food
from SnakeScore import Scoreb


scrn= Screen()
scrn.bgcolor("blue")
scrn.setup(600,600)
scrn.title("The Snake Game")
scrn.tracer(0)#to turn off turtle graphics


snake=Snake()#initialise snake
sfood=Food()#initialise food
score=Scoreb()#initialising Score


scrn.listen()#movement of snake according to keys
scrn.onkey(snake.up,"Up")
scrn.onkey(snake.down,"Down")
scrn.onkey(snake.right,"Right")
scrn.onkey(snake.left,"Left")



game_is_on = True
while game_is_on:#continuation of process to keep snake moving


    scrn.update()#to turn on turtle graphics
    snake.move()#move function from snake class to move snake forward
    time.sleep(0.08)#to give movement process some time gap else we will not get time to opoerate our turtle

    if snake.head.distance(sfood) < 15:#check for collision with food
        sfood.renew()#get food at other random instance#snake food module function
        snake.extend()#extend turtle length #snake module function
        score.increase()#score increaser #snake score module's function
        
    if snake.head.xcor()>290 or snake.head.xcor()<-290:
        print("you lose")
        game_is_on=False#while loop terminates here and game ends
        score.endgame()#function to print game end message
    elif snake.head.ycor()>290 or snake.head.ycor()<-290:
         print("you lose")
         game_is_on=False
         score.endgame()
    
    for segs in snake.turt_seg[1:]:#check if snake is not colliding with its tail
        if snake.head.distance(segs)<10:
            print("you lose")
            game_is_on=False
            score.endgame()  

scrn.exitonclick() 