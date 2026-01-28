import turtle
import random

t = turtle.Turtle()
t.speed(0)

for i in range(36):
	t.color(random.choice(["red", "purple", "blue", "orange"]))
	t.circle(100)
	t.right(10)

turtle.done()