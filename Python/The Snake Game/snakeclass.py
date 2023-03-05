from turtle import Turtle
BASE_POS=[(0,0),(-20,0),(-40,0)]#default position of turtles
BASE_MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.turt_seg=[]#list to keep details of each turtle
        self.create_snake()
        self.head=self.turt_seg[0]

    def create_snake(self):#iterating through each position in base position for snake shape turtle creation
        for pos in BASE_POS:
            self.new_seg(pos)
    
    def new_seg(self,pos):#construction of turtles at position passed from create_snake function or extend function
            turt=Turtle("square")
            turt.penup()
            turt.speed(7)
            turt.color("white")
            turt.goto(pos)
            self.turt_seg.append(turt)
    
    def extend(self):#function to add segment in turtle/extending length of snake
        self.new_seg(self.turt_seg[-1].position())

        


    def move(self):
        for seg in range(len(self.turt_seg)-1,0,-1):
            new_x=self.turt_seg[seg-1].xcor()
            new_y=self.turt_seg[seg-1].ycor()
            self.turt_seg[seg].goto(new_x,new_y)

        self.head.forward(BASE_MOVE)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)