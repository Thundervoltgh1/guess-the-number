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

def Random():
    guess=l.get()
    guess=int(guess)
    if guess>a:
        tkinter.messagebox.showinfo("high","your guess is too high")
    elif guess<a:
        tkinter.messagebox.showinfo("low","your guess is too low")
    elif guess==a:
        tkinter.messagebox.showinfo("good","your guess is CORRECT")
    
f=Label(root,text="What's your name")
k=Label(root,text="Take a guess")
h=Entry(root,width=20)
h.place(x=210,y=200)
f.place(x=100,y=200)
k.place(x=100,y=300)
g=Button(root,text='ok',command=btn)
g.place(x=250,y=250)
l=Entry(root,width=20)
l.place(x=210,y=300)
u=Button(root,text='guess',command=Random)
u.place(x=250,y=350)
root.mainloop()
