from turtle import Turtle,Screen
timmy=Turtle()
scrn=Screen()
user_col=str(scrn.textinput("Turtle Colour","Enter colour of your Turtle's pen"))
timmy.color(user_col)
timmy.speed(10)
def fwd():
    timmy.forward(10)
def bwd():
    timmy.backward(10)
def rt():
    timmy.right(10)
def lt():
    timmy.left(10)
def clr():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
scrn.listen()
scrn.onkey(key="W",fun=fwd)
scrn.onkey(key="w",fun=fwd)
scrn.onkey(key="S",fun=bwd)
scrn.onkey(key="s",fun=bwd)
scrn.onkey(key="A",fun=lt)
scrn.onkey(key="a",fun=lt)
scrn.onkey(key="D",fun=rt)
scrn.onkey(key="d",fun=rt)
scrn.onkey(key="C",fun=clr)
scrn.onkey(key="c",fun=clr)

scrn.exitonclick()