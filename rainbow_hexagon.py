from turtle import *
window=Screen()
pen=Turtle()
colors=["red","orange","yellow","blue","green","indigo","violet"]

for i in range(300):
    pen.speed(20)
    pen.color(colors[i%7])
    pen.pensize(i/50+1) 
    pen.forward(i)
    pen.left(51)
