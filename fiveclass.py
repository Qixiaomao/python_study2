#fiveclass.py

from turtle import Turtle

p = Turtle()

p.speed(5)
p.pensize(10)
p.color("black","yellow")
#p.fillcolor("red")
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()
