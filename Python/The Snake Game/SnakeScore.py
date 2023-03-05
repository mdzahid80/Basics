from turtle import Turtle,Screen
ALIGNMENT='Center'
FONT=('Arial', 20, 'normal')

class Scoreb(Turtle):

    def __init__(self,):#initialise score
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-30,270)
        self.write(f"Score,{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase(self):#incriment in score as turtle collide with food object
        self.score+=1
        self.clear()
        self.write(f"Score,{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def endgame(self):#endgame function if user lose in any condition
        print(self.score)
        self.clear
        self.goto(-20,0)
        self.write(f"You Lose,Your final score is {self.score}", move=False, align=ALIGNMENT, font=FONT)



