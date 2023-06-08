from turtle import Screen, Turtle
from paddles import Paddles
from ball import Ball
from scores import Scores
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

p1 = Paddles((370, 0), "white")
p2 = Paddles((-370, 0), "yellow")
ball = Ball()
score = Scores()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, "s")

#paddle = Turtle()
#paddle.color("white")
#paddle.shape("circle")
#paddle.penup()
#paddle.goto(350, 50)

game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move()
    print(ball.balldistance())
    print(p1.pdistance())
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif ball.xcor() > 400 or ball.xcor() < -400:
        score.addscore()
        ball.ballreset()
        time.sleep(0.5)
    #elif ball.balldistance() == p1.pdistance():
        #ball.bounce()

screen.exitonclick()