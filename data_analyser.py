
s=""

import os
def avg(a,o):
    if o=="v":
        ss=0
        for i in range(len(a)-1):
            att=a[i].split(",")
            ss+=float(att[0])
        avg=ss/(len(a)-1)
        return avg
    else:
        ss=0
        for i in range(len(a)-1):
            att=a[i].split(",")
            ss+=float(att[1])
        avg=ss/(len(a)-1)
        return avg


def mode():
    pass
nam=1
def dt(f,cwd,nwd):
    os.chdir(cwd)
    s=f+".txt"
    with open(s,"r") as file:
        run=True
        i=-1
        while run:
            c=file.readline()
            if i%2==1 and i!=-1:
                if c == "":
                    run = False
                    continue
                a=c.split(" ")
                sense=avg(a,"sense")
                velocity=avg(a,"v")
                os.chdir(nwd)
                with open("processed"+f+".txt","a") as hand:
                     hand.write(str(velocity)+" ")
                     hand.write(str(sense)+"\n")



            i+=1
    os.chdir(cwd)