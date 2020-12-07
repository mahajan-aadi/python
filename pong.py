from tkinter import *
import random

#declare
height=500
width=1080
pos_ball=[width/2,height/2]
fun=[(i,j)for i in range(1,3) for j in range(1,3)]
fun.extend([(i,j)for i in range(-2,0) for j in range(-2,0)])
v_x,v_y=random.choice(fun)
p1=0
p2=0
turn={'Up':False,'Down':False,"w":False,"s":False}
tim=0
#function

def up(event):
    global turn
    turn[event.keysym]=True

def down(event):
    global turn
    turn[event.keysym]=False

def abs(t):
    if t>=0:
        t+=tim/3
    else:
        t-=tim/3
    return t
def collide():
    global tim
    cp1=can.coords(SP1)
    cp2=can.coords(SP2)
    ba=can.coords(ball)
    if ba[0]<=cp1[2] and ba[3]<cp1[3] and ba[1]>cp1[1]:
        tim+=1
        return True
    if ba[2]>=cp2[0]and ba[3]<cp2[3] and ba[1]>cp2[1]:
        tim+=1
        return True
    return False
#balls
def move():
    global v_x,v_y,p1,p2,tim
    can.move(ball,abs(v_x),abs(v_y))

    #conditions to change directions
    if can.coords(ball)[1]<0 or can.coords(ball)[3]>(height-15):
        v_y=-v_y
    if can.coords(ball)[0]<0:
        p2+=1
        can.itemconfig(P2,text=("Player 2="+str(p2)))
        can.coords(ball,pos_ball[0]-10,pos_ball[1]-10,pos_ball[0]+10,pos_ball[1]+10)
        v_x,v_y=random.choice(fun)
        tim=0
    if can.coords(ball)[2]>width:
        p1+=1
        can.itemconfig(P1,text=("Player 1="+str(p1)))
        can.coords(ball,pos_ball[0]-10,pos_ball[1]-10,pos_ball[0]+10,pos_ball[1]+10)
        v_x,v_y=random.choice(fun)
        tim=0
    if collide():
        v_x=-v_x
    window.after(6,move)
#sliders
def pmove():
    for i in turn:
        window.bind('<KeyPress-%s>'%i,up)
        window.bind('<KeyRelease-%s>'%i,down)
    if turn["Up"] == True and can.coords(SP2)[1]>0:
        can.move(SP2,0,-2-tim/6)
    if turn["Down"] == True and can.coords(SP2)[3]<height:
        can.move(SP2,0,2+tim/6)
    if turn["w"] == True and can.coords(SP1)[1]>0:
        can.move(SP1,0,-2-tim/6)
    if turn["s"] == True and can.coords(SP1)[3]<height:
        can.move(SP1,0,2+tim/6)
    window.after(10,pmove)
#animation
window=Tk()
can=Canvas(window,bg="black",height=height,width=width)
can.pack()
can.create_oval(width/2-50,height/2-60,width/2+50,height/2+60,outline="white")
can.create_line(width/2,0,width/2,height,fill="white")
can.create_line(15,0,15,height,fill="white")
can.create_line(1065,0,1065,height,fill="white")
can.create_rectangle(15,height-15,width-15,height,fill="orange")
P1=can.create_text(200,height-8,text=("Player 1="+str(p1)),fill="red",font=("bold",10))
P2=can.create_text(800,height-8,text=("Player 2="+str(p2)),fill="red",font=("bold",10))
SP1=can.create_rectangle(0,200,15,300,fill="grey")
SP2=can.create_rectangle(width-15,200,width,300,fill="grey")

#ball
ball=can.create_oval(pos_ball[0]-10,pos_ball[1]-10,pos_ball[0]+10,pos_ball[1]+10,fill="red")
move()
pmove()

#sliders
window.mainloop()
