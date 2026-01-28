import turtle
import random

t = turtle.Turtle()
t.speed(0)

for _ in range(50):
	t.penup()
	t.goto(random.randint(-200, 200), random.randint(-200, 200))
	t.pendown()

	t.color(random.random(), random.random(), random.random())
	sides = random.randint(3, 8)

	for _ in range(sides):
		t.forward(50)
		t.right(360 / sides)

turtle.done()