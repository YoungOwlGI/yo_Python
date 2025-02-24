import turtle
from time import *
from turtle import *

t = Turtle()
t.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow", 'purple', 'blue']
t._tracer(False)
for x in range(400):
    t.forward(2 * x)
    t.color(colors[x % 4])
    t.left(91)
t._tracer(True)
done()
