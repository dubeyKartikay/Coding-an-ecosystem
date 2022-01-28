from Main import main
import os
import sys
sys.path.append("D:\\chikki\\Games\\Sim\\data_analyser")
from d import *
c=0
def move_data():
    try:
        os.rename("\u202adata.txt","D:\\chikki\\Games\\Sim\\Collected data\\raw\\data.txt")
    except:
        run=True
        i=1
        while run:
            try:
                os.rename("\u202adata.txt","D:\\chikki\\Games\\Sim\\Collected data\\raw\\data"+str(i)+".txt")
                run=False
            except:
                i+=1
def move_processed():
        try:
            os.rename("processeddata.txt","D:\\chikki\\Games\\Sim\\Collected data\\processed\\processeddata.txt")
        except:
            run=True
            i=1
            while run:
                try:
                    os.rename("processeddata.txt","D:\\chikki\\Games\\Sim\\Collected data\\processed\\processeddata"+str(i)+".txt")
                    run=False
                except:
                    i+=1
while c<250:
    c=main()
    source="data.txt"
    dest="data_analyser\‪data.txt"
    try:
        os.rename(source,dest)
    except:
        source="\u202a"+source
        os.rename(source,dest)
    dt("data")

    move_data()
    move_processed()
    os.chdir("D:\chikki\Games\Sim")














    

