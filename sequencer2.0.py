from Main import *
import os
import sys
from data_analyser import *


cwd=os.getcwd()
nwd="\Collected data\\raw"
nwd=cwd+nwd
os.chdir(nwd)


c=len(os.listdir())+1

##gen,animal,food=main(100,100)                ##main function call


pwd=cwd+"\\Collected data\\processed"

 
##dt("data"+str(c),nwd,pwd)                   ## processing data

gen,animal,food=sim_asap(10,100,100)
##print(len(food))
sim_from(food,animal)
