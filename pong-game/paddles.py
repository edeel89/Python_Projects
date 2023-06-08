from turtle import Turtle


class Paddles(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + 20
        top_screen = self.ycor()
        if top_screen == 240:
            pass
        else:
            self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        down_screen = self.ycor()
        if down_screen == -240:
            pass
        else:
            self.goto(self.xcor(), new_y)
    def pdistance(self):
        self.distance(self.xcor(), self.ycor())
        


