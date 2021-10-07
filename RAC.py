import tkinter as tk
from tkinter import *
from UserStories import *

root=Tk.tk()



def Nursury():
    NursuryText=Label(root, text="")

Nursury=Button(root, text="Nursury", width=15,
          height=4, borderwidth=2, relief="solid",
          background="")
Nursury.grid(column=3, row=6,columnspan=1, padx=100, pady=10)


def Office():
    OfficeText=Label(root, text="")

Office=Button(root, text="Office", width=15,
          height=4, borderwidth=2, relief="solid",
          background="#FDFD96")
Office.grid(column=4, row=6,columnspan=1, padx=100, pady=10)
          

def Lounge():
    LoungeText=Label(root, text="")

Lounge=Button(root, text="Lounge ", width=15,
          height=4, borderwidth=2, relief="solid",
          background="#dea5a4")
Lounge.grid(column=5, row=6, columnspan=1,  padx=100, pady=10)


my_menu=Menu(root)
root.config(menu=Menu)

def refresh(self):
    self.destroy()
    self.__init__()


file_menu= Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="Reset Window", command=refresh)














    