import turtle
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.pensize(1)
t.speed(1)

width = 250
height = 175
t.color("red", "red")
t.begin_fill()
for _ in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-40, 80)
t.pendown()
t.color("white", "white")
t.begin_fill()
t.circle(120)
t.end_fill()

t.penup()
t.goto(-200, 180)
t.pendown()
t.color("green", "green")
t.begin_fill()
for _ in range(3):
    t.forward(250)
    t.left(120)
t.end_fill()

t.hideturtle()
turtle.done()

