

import turtle as t
import random

t.colormode(255)
colours_list = [(219, 167, 86), (84, 101, 149), (116, 153, 200), (68, 127, 97), (112, 175, 134), (129, 23, 62), (173, 154, 48)]
tim = t.Turtle()
tim.hideturtle()


def create_dot():
        tim.dot(20, colours_list[random.randint(0, len(colours_list) - 1)])

def create_painting():
    for y in range(10):
        for x in range(10):
            tim.penup()
            tim.goto((x * 30) - 150, (y * 30) - 150)
            tim.pendown()
            create_dot()

create_painting()

screen = t.Screen()
screen.exitonclick()
