from   tkinter import  *
root = Tk()

e = Entry(root,fg="blue",bg="red")
e.insert(0,"Enter your name")
e.pack()

def ontap():
    variable1 = "hello " + e.get()
    ml = Label(root,text = variable1)
    ml.pack()

b1 = Button(root, text="hello jags",command=ontap)
b2 = Button(root, text="hello bro!", state = DISABLED)
b3 = Button(root, text="color dekho",fg="green",bg="red")

b1.pack()
b2.pack()
b3.pack()

root.mainloop()
