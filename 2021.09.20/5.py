import turtle
from random import *

time=10000
dt=0.1
number_of_turtles = 10
a=200
b=200

coor=[]
for i in range(number_of_turtles):
    coor.append([randint(-200, 200), randint(-200, 200),randint(-200, 200),randint(-200, 200)])

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

for i in range(time):
    iter=0
    for unit in pool:
        coor[iter][0]+=coor[iter][2]*dt
        coor[iter][1]+=coor[iter][3]*dt
        #unit.penup()
        unit.goto(coor[iter][0],coor[iter][1])
        if coor[iter][0]<-200: coor[iter][2]*=-1
        if coor[iter][0]>200: coor[iter][2]*=-1
        if coor[iter][1]<-200: coor[iter][3]*=-1
        if coor[iter][1]>200: coor[iter][3]*=-1
        iter+=1
