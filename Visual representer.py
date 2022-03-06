import turtle
import os
cwd=os.getcwd()
pwd=cwd+"\\Collected data\\processed"
os.chdir(pwd)
##s=input()
s="processeddata2.txt"
##r=input()
r="o"
wn=turtle.Screen()
grapher=turtle.Turtle()
scalar_x=turtle.Turtle()
scalar_y=turtle.Turtle()
grapher.speed(0)
scalar_x.speed(0)
scalar_y.speed(0)
def draw_scales_x(t,sx):
    t.home()
    i=0
    while i<300:
        t.fd(sx)
        t.rt(90)
        t.fd(10)
        t.bk(10)
        t.lt(90)
        i+=sx
def draw_scales_y(t,sy):
    t.home()
    t.lt(90)
    i=0
    while i<300:
        t.fd(sy)
        t.lt(90)
        t.fd(10)
        t.bk(10)
        t.rt(90)
        i+=sy
def draw_axis(t):
    t.ht()
    t.fd(500)
    t.bk(1000)
    t.fd(500)
    t.lt(90)
    t.fd(300)
    t.bk(600)
    t.home()


draw_axis(grapher)
draw_scales_x(scalar_x,50)
draw_scales_y(scalar_y,25)



    
scale=5
grapher.speed(0)
##draw_axis(grapher)
if r=="v":
    y=[]
    with open(s,"r") as file:
        run=True
        while run:
            c=file.readline()
            if c=="":
                run=False
            else:
                cont=c.split(" ")
                y.append(cont[0])
   
else:
    y=[]
    with open(s,"r") as file:
        run=True
        while run:
            c=file.readline()
            if c=="":
                run=False
            else:
                cont=c.split(" ")
                y.append(cont[1])
    pass
turtle.home()
turtle.setpos(1.2,0.1*scale)
for i in range(len(y)):
    posn=((i+2)*1.2,float(y[i])*scale)
    turtle.setpos(posn)
turtle.ht()
















