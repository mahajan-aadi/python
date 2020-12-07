from tkinter import *

class calculator():
    def __init__(s):
        s.operand=0
        s.store=0
    def assign(s):
        s.operand=float(op.get())
        print(calculator.__str__(s))
    def add(s):
        s.store+=s.operand
        print(calculator.__str__(s))
    def sub(s):
        s.store-=s.operand
        print(calculator.__str__(s))
    def mul(s):
        s.store*=s.operand
        print(calculator.__str__(s))
    def div(s):
        try:
            s.store/=s.operand
        except ZeroDivisionError:
            print("cannot divide by zero")
        except:
            print("something went wrong")
        print(calculator.__str__(s))
    def swap(s):
        s.store,s.operand=s.operand,s.store
        print(calculator.__str__(s))
    def __str__(s):
        return (f'store={s.store}\noperand={s.operand}\n')

cal=calculator()

frame=Tk(className="calculator")
frame.geometry("300x300")
op=Entry(frame)
op.place(x=170,y=150)
enter=Button(frame,text="enter",command=cal.assign).place(x=200,y=180)
swap=Button(frame,text="swap",command=cal.swap).place(x=0,y=0)
add=Button(frame,text="add",command=cal.add).place(x=0,y=50)
sub=Button(frame,text="subtract",command=cal.sub).place(x=0,y=100)
mul=Button(frame,text="multiply",command=cal.mul).place(x=0,y=150)
div=Button(frame,text="divide",command=cal.div).place(x=0,y=200)
operand=Label(frame,text="operand").place(x=110,y=150)

frame.mainloop()
