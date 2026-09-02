#Neon Mandala 

#Importing the turtle module and setting up the canvas

import turtle
canvas = turtle.Screen()
canvas.bgcolor("white")
canvas.title("Neon Mandala")

pen = turtle.Turtle()
#pen.speed("fastest")
pen.hideturtle()

#Outer SPIRAL

colors =["red","yellow","green","pink","purple","brown","blue"]
for i in range(100):
    pen.color(colors[i % len(colors)])
    pen.width(3)
    pen.forward(i * 2)
    pen.right(91)


#Pen positions

pen.penup()
pen.goto(0,0)
pen.setheading(90)
pen.pendown()
pen.color("gold","yellow")
pen.begin_fill()
for i in range(5):
    pen.forward(130)
    pen.right(144)
pen.end_fill()


















turtle.done()





