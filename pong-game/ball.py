from turtle import Turtle, Screen
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.add_x = 10
        self.add_y = 10
        
    def move(self):
        x_move = self.xcor() + self.add_x
        y_move = self.ycor() + self.add_y
        self.goto(x_move, y_move)

    def bounce(self):
        self.add_y *= -1
    
    def ballreset(self):
        self.goto(0,0)
    def balldistance(self):
        self.distance(self.xcor(), self.ycor())

        
        
