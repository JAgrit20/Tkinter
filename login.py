from tkinter import *
import tkinter.messagebox

def entry():
    if(ent1.get()=="ABC" and ent2.get()=="1234"):
        print("Sign IN succesful")
    else:
        tkinter.messagebox.showinfo("SIgn Problem", "Wrong username or password")
        tk.close()

def userent1():
    print(ent1.get())
    print(ent2.get())   
    print("amount withdraw", ent3.get())
    print("amount deposited", ent4.get())
    
    

tk=Tk()
lab1=Label(tk,text="Name")
lab1.grid(row=0, column=0)
ent1=Entry(tk)
ent1.grid(row=0, column=1, columnspan=2)

lab2=Label(tk,text="Password")
lab2.grid(row=1, column=0)
ent2=Entry(tk)
ent2.grid(row=1, column=1, columnspan=2)

Button(tk,text="LOGIN", command=entry).grid(row=2,column=1)

text1=Label(tk,text="Which  account")
text1.grid(row=3,column=0)
v=IntVar()


Radiobutton(tk,text="saving", variable=v, value=1).grid(row=4,column=0)
Radiobutton(tk,text="current", variable=v, value=2).grid(row=5,column=0)

ent3=Entry(text="enter the ammount you want withdraw")
ent3.grid(row=7, column=0)
ent4=Entry(text="enter the ammount you want deposit")
ent4.grid(row=8, column=0)

Button(tk,text="show details", command=userent1).grid(row=2,column=1)


tk.mainloop()