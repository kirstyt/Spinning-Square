import turtle
import random

turtle.bgcolor('black')
turtle.colormode(255)
x=0
turtle.speed(0)
def draw_graphic():
    for x in range(500):
     r,b,g=random.randint(0,255),random.randint(0,255),random.randint(0,255)
     turtle.pencolor(r,g,b)
     turtle.fd(x+50)
     turtle.rt(91)

turtle.ontimer(draw_graphic, 60000)

turtle.exitonclick()