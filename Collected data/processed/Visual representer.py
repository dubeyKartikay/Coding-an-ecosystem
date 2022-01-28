import turtle
import os
##s=input()
s="processeddata2.txt"
##print(os.listdir())
##r=input()
r="o"
wn=turtle.Screen()
grapher=turtle.Turtle()
def draw_axis(t,sx,sy):
    t.ht()
    t.fd(500)
    t.bk(1000)
    t.fd(500)
    t.lt(90)
    t.fd(300)
    t.bk(600)
    t.home()
scale=5
draw_axis(grapher,1.2,50)
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
















