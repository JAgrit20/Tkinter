from tkinter import *
import sqlite3
connection=sqlite3.connect("gre.db")
cursor=connection.cursor()


tk=Tk()
lab1=Label(tk,text="Name")
lab1.grid(row=0, column=0)
ent1=Entry(tk)
ent1.grid(row=0, column=1, columnspan=2)

lab2=Label(tk,text="surname")
lab2.grid(row=1, column=0)
ent2=Entry(tk)
ent2.grid(row=1, column=1, columnspan=2)

l3=Label(tk,text="branch")
l3.grid(row=2, column=0)
e3=Entry(tk)
e3.grid(row=2, column=1, columnspan=2)

l4=Label(tk,text="marks")
l4.grid(row=3, column=0)
e4=Entry(tk)
e4.grid(row=3, column=1, columnspan=2)



Button(tk,text="submit", command=entry).grid(row=5,column=1)



def create_table():
    cursor.execute("create table if not exists gre(  name TEXT, surname TEXT, branch TEXT, marks REAL)");
    connection.commit()

    
def entry():
    connection=sqlite3.connect("gre.db")
    cursor=connection.cursor()
    cursor.execute("Insert into gre(name, surname,branch,  marks) values(?, ?, ?, ?)", (ent1.get(), ent2.get(), e3.get(), e4.get() ))
    connection.commit()
    cursor.close()
    connection.close()


 

tk.mainloop()