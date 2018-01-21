#drawdata.py

from turtle import *


def drawyear():
    #This is two
    penup()
    goto(-300,100)
    pendown()
    color("red")
    pensize(10)
    forward(50)
    right(90)
    forward(50)
    left(270)
    forward(50)
    right(-90)
    forward(50)
    right(-90)
    forward(50)
    

    #This is zero
    penup()
    goto(-200,100)
    pendown()
    begin_fill()
    color("red")
    pensize(10)
    end_fill()
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)

    #This is one
    penup()
    goto(-90,100)
    pendown()
    pensize(10)
    color("red")
    right(180)
    forward(100)

    #This is seven
    penup()
    goto(-60,100)
    pendown()
    pensize(10)
    color("red")
    left(90)
    forward(50)
    right(90)
    forward(100)

    #This is the text
    penup()
    goto(30,0)
    pendown()
    color("red")
    write(("年"),font = ("Times",30,"bold"))

def drawmonth():
    #This is the one
    penup()
    goto(150,100)
    pendown()
    pensize(1)
    color("blue")
    right(0)
    forward(100)

    #This is the two
    penup()
    goto(170,100)
    pendown()
    color("blue")
    pensize(1)
    left(90)
    forward(50)
    left(-90)
    forward(50)
    left(-90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

     #This is the text
    penup()
    goto(250,0)
    pendown()
    color("blue")
    write(("月"),font = ("Times",30,"bold"))

    #This is the two
    
    penup()
    goto(350,100)
    pendown()
    color("green")
    pensize(1)
    left(-0)
    forward(50)
    left(-90)
    forward(50)
    left(-90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

    #This is the six
    penup()
    goto(480,100)
    pendown()
    begin_fill()
    color("green")
    end_fill()
    left(180)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

    #This is the text
    penup()
    goto(500,0)
    pendown()
    color("green")
    write(("日"),font = ("Times",30,"bold"))

    hideturtle()#笔隐藏
    
    
    
    
    
    
    
    
    
    
def main():
    setup(2000,800,0,0)
    
    drawyear()
    drawmonth()
    
    
main()
