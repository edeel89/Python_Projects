from turtle import Turtle, Screen
import pandas

#Setting up the screen
screen = Screen()
#screen.bgpic("blank_states_img.gif")
screen.bgcolor("black")
screen.setup(width=725, height=491)
screen.title("Guess the State")
#screen.tracer(0)

paddle = Turtle()
paddle.color("white")
paddle.shape("circle")
paddle.penup()
print(paddle.isvisible())

screen.exitonclick()