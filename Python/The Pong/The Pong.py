from turtle import Turtle,Screen
from pong_paddle import paddle
from pong_ball import ball
from pong_score import Score
import time

scrn=Screen()
scrn.setup(800,600)
scrn.bgcolor("cyan")
scrn.tracer(0)
rscore=0
lscore=0
score=Score()
rt_paddle=paddle(350)
lt_paddle=paddle(-350)

p_ball=ball()

scrn.listen()

scrn.onkey(key="Up",fun=rt_paddle.fwd) 
scrn.onkey(key="Down",fun=rt_paddle.bwd) 
scrn.onkey(key="w",fun=lt_paddle.fwd) 
scrn.onkey(key="s",fun=lt_paddle.bwd) 


game_on=True
while game_on:
    time.sleep(0.1)
    scrn.update()
    p_ball.move()

    if p_ball.distance(rt_paddle) < 50 and p_ball.xcor() > 320 or p_ball.distance(lt_paddle) < 50 and p_ball.xcor() < -320:
        p_ball.xbounce()

    if p_ball.ycor()<-280 or p_ball.ycor()>280:
        p_ball.ybounce()

    if p_ball.xcor()<-380:
        p_ball.resetL()
        score.rpoint()

    if p_ball.xcor()>380:
        p_ball.resetR()
        score.lpoint()
        
scrn.exitonclick()
