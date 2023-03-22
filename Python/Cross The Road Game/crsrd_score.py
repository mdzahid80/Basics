from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level=0
        self.update()

    def update(self):
        self.clear()
        self.level+=1
        self.goto(-280,280)
        self.write("Level=",align="center",font=("Courier" ,40, "normal"))
        self.goto(-180,280)
        self.write(self.level,font=("Courier" ,40, "normal"))
    
    def game_over(self):
        self.goto(-300,0)
        self.write("Game Over,Your score is:",font=("Courier" ,40, "normal"))
        self.goto(100,-50)
        self.write(self.level-1,font=("Courier" ,40, "normal"))
        return False
    