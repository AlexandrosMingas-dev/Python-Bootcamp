import colorgram
import turtle as t
import random

screen=t.Screen()
colors=colorgram.extract("hirst.jpeg",30)
rgb_colors=[]
for color in colors:
    R=color.rgb.r
    G=color.rgb.g
    B=color.rgb.b

    new_color=(R,G,B)
    rgb_colors.append(new_color)

timmyT=t.Turtle()
timmyT.hideturtle()
screen.colormode(255)
timmyT.penup()
timmyT.goto(-250.0,-250.0)
timmyT.pendown()
timmyT.speed(0)

for i in range(10):
    for j in range (10):
        rColor=random.choice(rgb_colors)
        timmyT.dot(20,rColor)
        timmyT.penup()
        timmyT.forward(50)
        timmyT.pendown()
    timmyT.penup()
    timmyT.left(90)
    timmyT.forward(50)
    timmyT.left(90)
    timmyT.forward(500)
    timmyT.setheading(0)
screen.exitonclick()
