from tkinter import*
import random
import tkinter.messagebox
root=Tk()
root.title("Guess The Number ")
root.minsize(500,600)
root.config(background="Orange")
a=random.randint(1,20)
def btn():
    name=h.get()
    tkinter.messagebox.showinfo("Welcome^_^",'well,'+name+' i am thinking of a number bettwen 1 and 20')

f=Label(root,text="What's your name")
h=Entry(root,width=20)
h.place(x=210,y=200)
f.place(x=100,y=200)
g=Button(root,text='ok',command=btn)
g.place(x=250,y=250)

root.mainloop()