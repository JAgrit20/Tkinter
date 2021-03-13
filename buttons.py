from   tkinter import  *
root = Tk()

def ontap():
    ml = Label(root,text = "hey you clicked me!!")
    ml.pack()

b1 = Button(root, text="hello jags",command=ontap)
b2 = Button(root, text="hello bro!", state = DISABLED)
b3 = Button(root, text="color dekho",fg="green",bg="red")

b1.pack()
b2.pack()
b3.pack()

root.mainloop()
