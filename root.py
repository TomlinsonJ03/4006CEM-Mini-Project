import tkinter as tk
from tkinter import * 
from UserStories import *


root = tk.Tk()
root.title("4006CEM Mini-Project")
root.geometry('1920x1200')


name=tk.Entry(root, width=35, borderwidth=3)
name.grid(row=0, column=0, columnspan=2 , padx=10, pady=10)


def NameClick():

    myLabel= Label(root, text= "Hello " + name.get() + """, Enjoy :)""" )
    myLabel.grid(row= 0, column=3, columnspan=2)
myButton = Button(root, text="Enter your name!", padx= 15, pady= 15, command=NameClick)
myButton.grid(row=0, column=2,columnspan=1)

labelframe = LabelFrame(root, text="Introduction",background="#F1F1F1")
labelframe.grid(row = 1, column = 1, columnspan=5)

Firstlabelframe = Label(labelframe, text= IntroTxt, padx=2, pady=20)
Firstlabelframe.grid(row=2, column=2,columnspan=3)
Firstlabelframe.config(font=("Helvetica", 8))


#location buttons


def EnterBasement():
    BasementText= Label(root, text= BaseText)
    BasementText.grid(row=3, column=2, 
                    columnspan=4)
    GoodEndingBase=Button(root, text="Be Nice", width=12, 
                    height=4, borderwidth=2, relief="solid", 
                    background="#F1F1F1",command=BaseGoodEnding)
    GoodEndingBase.grid(column=3, row=4,)

    BadEnding=Button(root, text="Be Mean", width=12, 
                    height=4, borderwidth=2, relief="solid", 
                    background="#F1F1F1",command=BaseBadEnding)
    BadEnding.grid(column=4, row=4,)

def BaseGoodEnding():
    BseGoodEnding=Label(root, text=BaseTextGood)
    BseGoodEnding.grid(row=5, column=3,columnspan=4)

def BaseBadEnding():
    BseBadEnding=Label(root, text=BaseTextBad)
    BseBadEnding.grid(row=5, column=3,columnspan=4)
    


 
def Kitchen():

    KitchenText=Label(root, text= Kitchentext)
    KitchenText.grid(row=3, column=2,
                     columnspan=4)

    GoodEndingKitchen=Button(root, text = "Be nice", command=KitchenText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#E8DCD0")
    GoodEndingKitchen.grid(row=4 ,column= 3,)

    BadEndingKitchen=Button(root, text = "Be mean", command=KitchenText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#E8DCD0")
    BadEndingKitchen.grid(row=4, column= 4)


def KitchenGoodEnding():
    KichGoodEnding=Label(root, text=BaseTextGood)
    KichGoodEnding.grid(row=5, column=3,columnspan=4)

def KitchenBadEnding():
    pass


def lounge():
    LoungeText=Label(root, text=Loungetext)
    LoungeText.grid(row=3, column=2, columnspan=4)

    GoodEndingKitchen=Button(root, text = "Be nice", command=LoungeText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#D4C0AB")
    GoodEndingKitchen.grid(row=3, column= 4)

    BadEndingKitchen=Button(root, text = "Be mean", command=LoungeText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#D4C0AB")
    BadEndingKitchen.grid(row=4, column= 4)

def Nursery():
    NurseryText=Label(root, text=Loungetext)
    NurseryText.grid(row=3, column=2, columnspan=4)

    GoodEndingNursery=Button(root, text = "Be nice", command=NurseryText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#C19E77")
    GoodEndingNursery.grid(row=3, column= 4)

    BadEndingNursery=Button(root, text = "Be mean", command=NurseryText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#C1977")
    BadEndingNursery.grid(row=4, column= 4)

def Office():
    OfficeText=Label(root, text=Loungetext)
    OfficeText.grid(row=3, column=2, columnspan=4)

    GoodEndingOffice=Button(root, text = "Be nice", command=OfficeText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#91683C")
    GoodEndingOffice.grid(row=3, column= 4)

    BadEndingOffice=Button(root, text = "Be mean", command=OfficeText,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#91683C")
    BadEndingOffice.grid(row=4, column= 4)







#Button Calling

OfficeButton=Button(root, text="Office",
                    command= OfficeText, width=12,
                    height=4, borderwidth=2, relief="solid",
                    background="#91683C")
OfficeButton.grid(column=0, row=7,columnspan=1, pady=5)


NurseryButton=Button(root, text="Nursery", 
                    command= Nursery, width=12,
                    height=4, borderwidth=2, relief="solid",
                    background="#C19E77")
NurseryButton.grid(column=0, row=6,columnspan=1, pady=5)


LoungeButton=Button(root, text="Lounge", 
                    command= lounge, width=12,
                    height=4, borderwidth=2, relief="solid",
                    background="#D4C0AB")
LoungeButton.grid(column=0, row=5,columnspan=1, pady=5)

KitchenButton=Button(root, text="Kitchen", 
                    command= Kitchen, width=12,
                    height=4, borderwidth=2, relief="solid",
                    background="#E8DCD0")
KitchenButton.grid(column=0, row=4,columnspan=1, pady=5)
    
Basement=Button(root, text="Basement", 
                    command= EnterBasement, width=12,
                    height=4, borderwidth=2, relief="solid",
                    background="#F1F1F1" )
Basement.grid(column=0, row=3,columnspan=1, pady=5)
    
root.mainloop()
