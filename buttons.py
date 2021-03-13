from   tkinter import  *
root = Tk()

def ontap():
    ml = Label(root,text = "hey you clicked me!!")
    ml.pack()

b1 = Button(root, text="hello jags",command=ontap)
b2 = Button(root, text="hello bro!", state = DISABLED)

b1.pack()
b2.pack()

root.mainloop()
