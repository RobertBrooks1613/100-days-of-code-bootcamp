import random
from random import randrange
from turtle import Turtle, Screen
from tkinter import messagebox
loop = 0

screen = Screen()
screen.title("Timmy = red , Tom = blue , Dave = yellow , randy = black, steve = purple")
screen.setup(width=750 ,height=500)
timmy = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
dave = Turtle(shape="turtle")
randy = Turtle(shape="turtle")
steve = Turtle(shape="turtle")

started = True
turtle_index = [timmy,tom,dave,randy,steve]
racers_pos = [timmy, tom, dave, randy, steve]
racers_name = ["Timmy", "Tom", "Dave", "Randy", "Steve"]
for turtle in turtle_index:
    turtle.shapesize(3)
    turtle.penup()


race_going = True
random_choice = [0,90,180,270]
x_axis = [-300,-200,-100,0,100,200,300]
y_axis = [-200,-100,0,100,200,300]


loops_to_run = len(x_axis) - 1
def rgb_():
    red = random.uniform(0.0,1.0)
    green = random.uniform(0.0,1.0)
    blue = random.uniform(0.0,1.0)
    rgb = (red,blue,green)
    return rgb

timmy.color("red")
tom.color("blue")
dave.color("yellow")
randy.color("black")
steve.color("purple")
def forward():
    timmy.forward(random.randint(1,10))
    tom.forward(random.randint(1,10))
    dave.forward(random.randint(1,10))
    randy.forward(random.randint(1,10))
    steve.forward(random.randint(1,10))
def check_winner(position):
    global race_going
    x_pos = position[0]
    if x_pos > 300:
        race_going = False
        return True

user_picked = screen.textinput(title="Make your Bet!" , prompt=f"Which turtle will win the Race? {racers_name}").title()
while race_going:
    if started:
        for index, start_pos in enumerate(turtle_index):
            start_pos.goto(x=x_axis[0], y=y_axis[index])

        started = False
    for index, racer in enumerate(racers_pos):
        winner_found = check_winner(racer.position())
        if winner_found:
            if racers_name[index] == user_picked:
                user_picked_txt = "Congrats! you picked the Winner!!"
                messagebox.showinfo("Winner found!", f"{user_picked_txt}\nThe winner was {racers_name[index]}")
                break
            elif racers_name[index] != user_picked:
                user_picked_txt = "Oh no! you picked wrong.."
                messagebox.showinfo("Winner found!", f"{user_picked_txt}\nThe winner was {racers_name[index]}")
                break
    if race_going:
        forward()


# def turn_left():
#     timmy.left(15)
#     timmy.pencolor(rgb_())
# def turn_right():
#     timmy.right(15)
#     timmy.pencolor(rgb_())
# def reset():
#     timmy.reset()
#     timmy.pensize(10)
#     timmy.speed("fastest")
#
# def circle():
#     for i in range(20):
#         forward()
#         timmy.right(360/20)
# screen.turtles()
# screen.listen()
# screen.onkey(fun=circle,key="space")
# screen.onkeypress(fun=forward,key="w")
# screen.onkeypress(fun=turn_right,key="d")
# screen.onkeypress(fun=turn_left,key="a")
# screen.onkey(fun=reset,key="r")


screen.exitonclick()