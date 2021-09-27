import turtle

dt=0.1
x=0
y=200
Vy=0
Vx=5
ay=-10
k=0.9

turtle.penup()
turtle.goto(x,y)
turtle.pendown()

for iter in range(0,10000,1):
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if y>0.1: turtle.goto(x,y)
    if y<=0.1: Vy=-Vy*k
