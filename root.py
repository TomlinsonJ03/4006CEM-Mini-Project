import tkinter as tk
from tkinter import *
from Filip import Chat, Fight, Lounge, Monologue 
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
    BadEnding.grid(column=4, row=4)

def BaseGoodEnding():
    BseGoodEnding=Label(root, text=BaseTextGood)
    BseGoodEnding.grid(row=5, column=2,columnspan=4)

def BaseBadEnding():
    BseBadEnding=Label(root, text=BaseTextBad)
    BseBadEnding.grid(row=5, column=3,columnspan=4)
    


 
def Kitchen():

    KitchenText=Label(root, text= Kitchentext)
    KitchenText.grid(row=3, column=2,
                     columnspan=4)

    GoodEndingKitchen=Button(root, text = "Be nice", command=KitchenGoodEnding,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#E8DCD0")
    GoodEndingKitchen.grid(row=4 ,column= 3,)

    BadEndingKitchen=Button(root, text = "Be mean", command=KitchenBadEnding,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#E8DCD0")
    BadEndingKitchen.grid(row=4, column= 4)

9
def KitchenGoodEnding():
    KichGoodEnding=Label(root, text=BaseTextGood)
    KichGoodEnding.grid(row=5, column=3,columnspan=4)

def KitchenBadEnding():
    pass



def lounge():
    global LoungeText
    LoungeText=Label(root, text=Loungetext)
    LoungeText.grid(row=3, column=2, columnspan=4)

    global GoodEndinglounge
    GoodEndinglounge=Button(root, text = " Yes, Thats me ", command=YesThatIsMe,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#D4C0AB")
    GoodEndinglounge.grid(row=4, column= 2)

    global BadEndingLounge
    BadEndingLounge=Button(root, text = "No, That isn't me", command=NoThatIsNotMe,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#D4C0AB")
    BadEndingLounge.grid(row=4, column= 4)

def CoffeeYes():
    global AgreeToCoffee
    AgreeToCoffee=Label(root, text=coffee)
    AgreeToCoffee.grid(row=2, column=3) 

def CoffeeNo():
    global DeclineCoffee
    DeclineCoffee=Label(root, text=NoCoffee)
    DeclineCoffee.grid(row=3, column=4)


def YesThatIsMe():
    global PositiveAnswer
    PositiveAnswer=Label(root, text=YesThatIs)
    PositiveAnswer.grid(row=5, column=2,columnspan=4)

    global CoffeeButton
    CoffeeButton=Button(root,text="Yes, please", command=CoffeeYes,
                            width=12, height=4, borderwidth=2, relief="solid",
                            background="#D4C0AB")

    CoffeeButton.grid(row=6, column=2)



def NoThatIsNotMe():
    global NegativeAnswer
    NegativeAnswer=Label(root, text=NoThatIsntMe)
    NegativeAnswer.grid(row=5, column=3,columnspan=4)
    pass

def delete():
    chat.grid_forget()
    

def BeginChat():
    LoungeText.grid_forget()
    GoodEndinglounge.grid_forget()
    BadEndingLounge.grid_forget()
    PositiveAnswer.grid_forget()
    CoffeeButton.grid_forget()
    AcceptCoffee.grid_forget()
    ChatButton.grid_forget()
    global chat 
    global QuestionButton
    chat = Label(root, text=Talk)
    chat.grid(row = 3 , column=2 ,rowspan=5)

    QuestionButton=Button(root, text=" why tell me ? ",command=monologue 
                        ,width=12, height=4, borderwidth=2, relief="solid",
                        background="#D4C0AB")

    QuestionButton.grid(row=8, column=2)


def monologue():
    chat.grid_forget()
    QuestionButton.grid_forget()
    Monologue=Label(root, text=Explaination)
    Monologue.grid(row=3, column=2)

    FightButton=Button(root, text="Stay",command=Fight
                    ,width=12, height=4, borderwidth=2, relief="solid",
                    background="#D4C0AB")
    FightButton.grid(row=4, column=2)


def Fight():
    fight=Label(root, text = Fighting)
    fight.grid(row=5,column=2)




def CoffeeYes():
    global AcceptCoffee
    global ChatButton
    AcceptCoffee=Label(root, text=coffee)
    AcceptCoffee.grid(row=7, column=2,columnspan=4) 

    ChatButton=Button(root, text="Chat", command=BeginChat,
                            width=12, height=4, borderwidth=2, relief="solid",
                            background="#D4C0AB")
    ChatButton.grid(row=8, column=2)



    


def CoffeeNo():
    pass





















































def Nursery():
    NurseryText=Label(root, text=NurseryStory)
    NurseryText.grid(row=3, column=2, columnspan=4,rowspan=2)

    GoodEndingNursery=Button(root, text = "Be nice", command=NurseryGDEnding,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#C19E77")
    GoodEndingNursery.grid(row=5, column= 3)

    BadEndingNursery=Button(root, text = "Be mean", command=NurseryBDEnding,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#C19E77")
    BadEndingNursery.grid(row=5, column= 4)

def NurseryGDEnding():
    NrsGoodEnding=Label(root, text=NurseryGoodEnding)
    NrsGoodEnding.grid(row=5, column=2,columnspan=4)

def NurseryBDEnding():
    NrsBadEnding=Label(root, text=NurseryBadEnding)
    NrsBadEnding.grid(row=5, column=2,columnspan=4)
    



def Office():
    OfficeText=Label(root, text=OfficeStory)
    OfficeText.grid(row=3, column=2, columnspan=4)

    GoodEndingOffice=Button(root, text = "Be nice", command=OfficeGoodEnding,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#91683C")
    GoodEndingOffice.grid(row=4, column= 3)

    BadEndingOffice=Button(root, text = "Be mean", command=OfficeBadEnding,
                             width=12, height=4, borderwidth=2, relief="solid",
                             background="#91683C")
    BadEndingOffice.grid(row=4, column= 4)
def OfficeGoodEnding():
    OffGoodEnding=Label(root, text=OfficeTextGood)
    OffGoodEnding.grid(row=5, column=2,columnspan=4)

def OfficeBadEnding():
    OffBadEnding=Label(root, text=OfficeTextBad)
    OffBadEnding.grid(row=5, column=2,columnspan=4)
    


   


#Button Calling

 
OfficeButton=Button(root, text="Office",
                    command= Office, width=12,
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
