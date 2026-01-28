import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(20)

for i in range(100):
    t.color(random.random(), random.random(), random.random()) # [0;1] RGB
    t.forward(i * 4)
    t.right(45)

turtle.done()