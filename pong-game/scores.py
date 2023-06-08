from turtle import Turtle

class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-200,200)
        self.color("white")
        self.new_score = self.write(0, font=("Verdana", 70, "normal"))
        self.counter = 0
    def addscore(self):
        self.clear()
        self.new_score = self.write(self.counter +1, font=("Verdana", 70, "normal"))
        self.counter += 1
