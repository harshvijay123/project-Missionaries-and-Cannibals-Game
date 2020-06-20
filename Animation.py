from turtle import *
from time import perf_counter as clock, sleep
from tkinter import *

def mn_eck(p, ne,sz):
    turtlelist = [p]
    #create ne-1 additional turtles
    for i in range(1,ne):
        q = p.clone()
        q.rt(360.0/ne)
        turtlelist.append(q)
        p = q
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let those ne turtles make a step
        # in parallel:
        for t in turtlelist:
            t.rt(360./ne)
            t.pencolor(1-c,0,c)
            t.fd(sz)

def main(root):
    window = Toplevel(root)
    window.attributes('-fullscreen',1)
    canvas = Canvas(window,height=450,width=450)
    canvas.pack(fill=BOTH,expand=YES)
    p=RawTurtle(canvas)
    pen=RawTurtle(canvas)
    pen.speed(0)
    s = p.getscreen()
    s.bgcolor("black")
    p.speed(0)
    p.hideturtle()
    pen.hideturtle()
    p.pencolor("red")
    p.pensize(2)
    pen.pencolor("red")
    pen.pensize(2)
    pen.pu()
    pen.setpos(450,-500)
    pen.pd()
    pen.write('Loading....',font=('candara',30))
    p.pu()
    p.setpos(500,-200)
    p.pd()

    s.tracer(36,0)

    at = clock()
    mn_eck(p, 36, 19)
    et = clock()
    z1 = et-at

    sleep(1)

    at = clock()
    while any(t.undobufferentries() for t in s.turtles()):
        for t in s.turtles():
            t.undo()
    et = clock()
    return "runtime: %.3f sec" % (z1+et-at)


