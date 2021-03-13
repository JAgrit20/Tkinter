from tkinter import *

root = Tk()
root.title("hello to my world")

my_img = PhotoImage(file="./me.png")
my_Lable = Label(root,image=my_img)
my_Lable.pack()



button_quit = Button(root,text="Exit",command=root.quit)
button_quit.pack()

root.mainloop()

