import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

star = turtle.Turtle()
star.color("purple")
star.speed(3)  # Disminuye la velocidad


for i in range(100):
    star.forward(i * 10)
    star.right(144)

star.hideturtle()
turtle.done()
start_time = time.time()

while time.time() - start_time < 5:
    star.forward(10)
    star.right(144)