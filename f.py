from engine import *
from tkinter import *

def generate_game(filename):
    with open(filename, "r") as file:
        c = file.readlines()
        last_gen = c[-2].split(" ")
        last_gen = last_gen[:len(last_gen) - 1]
        game_signature=c[-1]
        print(game_signature)
    list_of_animals = []
    for i in last_gen:
        attr = list(map(float, i.split(",")))
        o = objects("a", attr[0], attr[1])
        list_of_animals.append(o)


win=Tk()
win.geometry("200x200")
text1=Label(win,text="lqeifgoeufgy",)
text1.place(x=0,y=0)
for e in text1.keys():
    print(e,text1[e])
win.mainloop()