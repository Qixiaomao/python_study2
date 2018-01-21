from turtle import *

#p = Turtle
#This is the  triangle

def  angled():
    pensize(3)
    penup()
    goto(-200,-50)
    pendown()
    begin_fill()
    color("red")
    circle(40,steps=3)
    end_fill()

   #This is the square
    penup()
    goto(-90,-60)
    pendown()
    begin_fill()
    color("blue")
    circle(40,steps = 4)
    end_fill()

    #This is the pentagon
    penup()
    goto(30,-60)
    pendown()
    begin_fill()
    color("yellow")
    circle(40,steps=5)
    end_fill()

    #This is the hexagon
    penup()
    goto(150,-60)
    pendown()
    begin_fill()
    color("green")
    circle(40,steps=6)
    end_fill()

    #This is the roundness
    penup()
    goto(250,-60)
    pendown()
    begin_fill()
    color("purple")
    circle(38)
    end_fill()

    #This is the text
    
    penup()
    goto(-100,50)
    pendown()
    write(("Cool Colorful shapes"),font = ("Times",18,"bold"))
    hideturtle()

    done
    

def main():
     angled()
     #two()



main()
