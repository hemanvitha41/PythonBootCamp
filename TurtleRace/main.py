from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(600, 450)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-80,-40,0, 40, 80, 120]
speed = [10,20,30,40,50,60]
race_on = False
all_turtles = []
for turtle_index in range(6):
    tim = Turtle("turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(-290, y_positions[turtle_index])
    tim.speed(random.choice(speed))
    all_turtles.append(tim)

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 255:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is winner!")
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)



screen.exitonclick()