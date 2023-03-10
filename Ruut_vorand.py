from math import *
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


def lahenda():
    if a.get()=="":
        a.configure(bg="red")
    else:
        a.configure(bg="lightblue")
    if b.get()=="":
        b.configure(bg="red")
    else:
        b.configure(bg="lightblue")
    if c.get()=="":
        c.configure(bg="red")
    else:
        c.configure(bg="lightblue")
    if a.get()!="" and b.get()!="" and c.get()!="":
        a1=float(a.get())
        b1=float(b.get())
        c1=float(c.get())
        D=b1**2-4*a1*c1
        if D>0:
            x1=round((-b1-sqrt(D))/(2*a1),2)
            x2=round((-b1+sqrt(D))/(2*a1),2)
            vas=f"x1={x1}\nx2={x2}"
        elif D==0:
            x=round((-1*b1)/(2*a1),2)
            vas=f"x={x}"
        else:
            vas="Lahendust pole"
        res.configure(text=vas)

def graafik():
    a1=float(a.get())
    b1=float(b.get())
    c1=float(c.get())
    x0=(-b1)/2*a1
    y0=a1*x0**2+b1*x0+c1
    x=np.arange(x0-15,x0+15,1) #min,max,step
    y=a1*x**2+b1*x+c1
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title("Ruutvõrrand")
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()




aken=Tk()
aken.geometry("750x200")
aken.title("Ruudukujulised võrrandid")
lbl=Label(aken,text="Kvadraatilise võrrandi lahendamine",bg="lightblue",fg="green",font="Arial 20")
a=Entry(aken, fg="blue",bg="lightblue",width=5,font="Arial 20",justify=CENTER)
t1=Label(aken,text="x**2+",fg="green",font="Arial 20")
b=Entry(aken, fg="blue",bg="lightblue",width=5,font="Arial 20",justify=CENTER)
t2=Label(aken,text="x+",fg="green",font="Arial 20")
c=Entry(aken, fg="blue",bg="lightblue",width=5,font="Arial 20",justify=CENTER)
t3=Label(aken,text="=0",fg="green",font="Arial 20")
lah=Button(aken,text="Lahenda", font="Arial 24",bg="green", relief=GROOVE, width=10,command=lahenda)
graf=Button(aken,text="Graafik", font="Arial 24",bg="green", relief=GROOVE, width=10,command=graafik)
res=Label(aken,text="Lahendus",bg="yellow",font="Arial 10",width=50,height=3)

res.pack(side=BOTTOM)
lbl.pack()
a.pack(side=LEFT)
t1.pack(side=LEFT)
b.pack(side=LEFT)
t2.pack(side=LEFT)
c.pack(side=LEFT)
t3.pack(side=LEFT)
lah.pack(side=LEFT)
graf.pack(side=RIGHT)
aken.mainloop()
