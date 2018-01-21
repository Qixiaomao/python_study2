from turtle import Turtle

def main():
    p = Turtle()
    p.color("green")
    p.pensize(6)
    p.hideturtle()
    p.getscreen().tracer(30,0)
    p.left(90)
    p.penup()
    p.goto(x,y)
    p.pendown()

    t = tree([p],110,65,0.6375)

def tree(plist,l,a,f):
    """plist is list of pens
     l is length of branch
     a  is half of the angle between
     f  is factor by which branch is shortened
     from level to level."""
    if l > 5:
        lst = []
        for p in plist:
            p.forward(1)#沿着当前的方向前行
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)

main()
