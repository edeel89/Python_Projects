from turtle import Turtle, Screen
import pandas

#Setting up the screen
screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(width=725, height=491)
screen.title("Guess the State")

#Reading States name column
data = pandas.read_csv("50_states.csv")
states_list = data["state"]

#Making a list of all States from CSV file
my_state_list = []
for i in states_list:
    my_state_list.append(i)

#Running the game
game_is_on = True
counter = 0
while game_is_on:
    x = screen.textinput(f"{counter}/50 Correct", "Guess the State:")
    if x in my_state_list:
        row_data = data[data.state == x]
        row_data_dict = row_data.to_dict()
        rdxcor = row_data_dict["x"]
        rdycor = row_data_dict["y"]
        rdxcor = list(rdxcor.values())
        rdycor = list(rdycor.values())
        rdxcor = rdxcor[0]
        rdycor = rdycor[0]
        xycor = (rdxcor, rdycor)
        paddle = Turtle()
        paddle.color("black")
        #paddle.hideturtle()
        paddle.penup()
        paddle.goto(xycor)
        paddle.write(x)
        counter += 1
        
    else:
        game_is_on = False
    





screen.exitonclick()