from tkinter import *
from tkinter import filedialog
import sqlite3
import time


class main:
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widget()

    def widget(self):
        self.head = Label(self.master,text="Login",font=('',35))
        self.head.pack(pady=30)
        self.logf = Frame(self.master)
        Label(self.logf,text="LRN : ",font=('',18)).pack()
        Entry(self.logf,width=30,font=15).pack()
        Label(self.logf,text="Pass : ",font=('',18)).pack()
        Entry(self.logf,width=30,font=15).pack()
        self.logf.pack()
        Button(self.logf,text="Login",font=('',15)).pack()
        Button(self.logf,text="Create Account",font=('',15)).pack()




root = Tk()
main(root)
root.mainloop()







