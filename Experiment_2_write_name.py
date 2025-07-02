import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("MIJU Smooth Animation")
screen.setup(width=800, height=400)
turtle.tracer(0)  # Turn off auto update

bg = turtle.Turtle()
bg.hideturtle()

writer = turtle.Turtle()
writer.hideturtle()
writer.color("red")
writer.penup()

writer.goto(-320, 0)
writer.write("Miju Chowdhury", font=("Courier", 60, "italic"))
screen.update()

time.sleep(2)  

while True:
    for x in range(-950, 600, 2):
        writer.clear()  
        writer.goto(x, 0)
        writer.write("Miju Chowdhury", font=("Courier", 60, "italic"))
        screen.update()
        time.sleep(0.005)

    # time.sleep(1)
    # turtle.done()




