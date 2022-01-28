from Main import *
import os
import sys
from data_analyser import *
from tkinter import filedialog
from tkinter import *


def init_start_from():
    new_win = Tk()
    new_win.geometry("500x200")
    text1 = Label(new_win, text="Current File:  ")
    text1.place(x=65, y=0)

    def open_file():
        def change_save_name():
            text2["text"] = "Save file Name:  "
            entry1 = Entry(new_win)
            entry1.place(x=150, y=40)

        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="open file",
                                              filetypes=(("text file", "*.txt*"),))
        text1["text"] = "Current File:  " + filename
        button1["text"] = "Load Another File"
        text2["text"] = "Save file Name:  " + get_save_name(filename)
        text3["text"] = "Generations simulated:  " + get_gens(filename)
        text4["text"] = "Population Size:  " + get_pop_sz(filename)
        text5["text"] = "Food Scarcity:  " + str(round(get_food_n(filename)/int(get_pop_sz(filename)), 2))
        button2 = Button(new_win, text="Change", command=change_save_name)
        button2.place(x=15, y=40)





    def get_save_name(filename):
        with open(filename, "r") as file:
            line = file.readline()
        return line[:len(line) - 1]

    def get_gens(filename):
        attr = master(filename)
        return str(attr[0])

    def get_pop_sz(filename):
        attr = master(filename)
        return str(attr[1])

    def get_food_n(filename):
        attr = master(filename)
        return attr[2]

    def master(filename):
        with open(filename)as file:
            c = file.readlines()
            a = c[-1].split("-")
            a = a[1:len(a) - 1]
            b = list(map(int, a))
        return b
    text2 = Label(new_win, text="Save file Name:")
    text2.place(x=65, y=40)

    text3 = Label(new_win, text="Generations simmed:")
    text3.place(x=65, y=75)

    text4 = Label(new_win, text="Population Size:")
    text4.place(x=65, y=106)

    text5 = Label(new_win, text="Food Scarcity: ")
    text5.place(x=65, y=140)

    button1 = Button(new_win, text="Load File", command=open_file)
    button1.place(x=65, y=170)


    new_win.mainloop()


def init_sim_asap():
    def Start_sim_asap():
        food = int(entry1.get())*int(entry2.get())
        animal = int(entry2.get())
        gens = int(entry3.get())

        cwd = os.getcwd()
        nwd = "\Collected data\\raw"
        nwd = cwd + nwd
        os.chdir(nwd)

        c = len(os.listdir()) + 1

        gen, animal, food = sim_asap(gens, food, animal)  ##main function call

        pwd = cwd + "\\Collected data\\processed"

        dt("data" + str(c), nwd, pwd)  ## processing data

    new_win = Tk()
    new_win.geometry("200x200")

    text1 = Label(new_win, text="Food Scarcity:", font="Times 12")
    text1.place(x=20, y=20)

    entry1 = Entry(new_win)
    entry1.place(x=120, y=25, width="70", height="20")

    text2 = Label(new_win, text="Animals:", font="Times 12")
    text2.place(x=20, y=50)

    entry2 = Entry(new_win)
    entry2.place(x=120, y=55, width="70", height="20")

    text3 = Label(new_win, text="No. of generations:", font="Times 10")
    text3.place(x=20, y=80)

    entry3 = Entry(new_win)
    entry3.place(x=130, y=80, width="60", height="20")

    button2 = Button(new_win, text="Start", command=Start_sim_asap)
    button2.place(x=75, y=120)


def init_sim_basic():
    def Start_sim():
        food = int(float(entry1.get())*int(entry2.get()))
        animal = int(entry2.get())

        cwd = os.getcwd()

        nwd = "\Collected data\\raw"
        nwd = cwd + nwd
        os.chdir(nwd)

        c = len(os.listdir()) + 1

        main(food, animal)  # main function call

        pwd = cwd + "\\Collected data\\processed"

        dt("data" + str(c), nwd, pwd)  # processing data

    new_win = Tk()
    new_win.geometry("200x200")

    text1 = Label(new_win, text="Food Scarcity:", font="Times 12")
    text1.place(x=20, y=20)

    entry1 = Entry(new_win)
    entry1.place(x=120, y=25, width="50", height="20")

    text2 = Label(new_win, text="Animals:", font="Times 12")
    text2.place(x=20, y=50)

    entry2 = Entry(new_win)
    entry2.place(x=120, y=55, width="50", height="20")

    button2 = Button(new_win, text="Start", command=Start_sim)
    button2.place(x=75, y=100)


win = Tk()

win.geometry("500x300")

Title = Label(text=" Eco Sim ", font="Verdana 20 bold")
Title.place(x=175, y=0)

Button1 = Button(win, text="Start Simulation", fg="red", command=init_sim_basic)
Button1.place(x=120, y=100, width=100, height=50)

Button2 = Button(win, text="Sim Generations", fg="Blue", command=init_sim_asap)
Button2.place(x=120, y=155, width=100, height=50)

Button3 = Button(win, text="Load Data", fg="red", command=init_start_from)
Button3.place(x=225, y=100, width=100, height=50)

win.mainloop()
