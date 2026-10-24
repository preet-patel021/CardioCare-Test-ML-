'''import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = ["red", "blue", "lime", "yellow", "cyan",
          "magenta", "orange", "pink", "white"]

for i in range(120):
    t.penup()
    t.goto(0, 40)      # or (0,0)
    angle = i * (math.pi * 2) / 120

    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle)) * 15

    c = random.choice(colors)
    t.color(c)

    t.pendown()
    t.goto(x, y)

    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()'''

import turtle
t = turtle.Turtle()
t.screen.bgcolor("black")
t.pensize(2)
t.color("green")
t.left(90)
t.backward(100)
t.speed(100)

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color('pink')
        t.circle(2)
        t.color('brown')

        t.left(20)
        tree(4 * i / 5)
        t.right(40)
        tree(4 * i / 5)
        t.left(20)

        t.backward(i)
tree(100)
turtle.done()
