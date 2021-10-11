from tkinter import *
from app import App
from options import options
from root import *
from UserStories import *

def main():
    global app
    root = Tk()
    root.title("4006CEM Mini-Project")
    root.geometry('1920x1200')

    app = App(root)

    app.createButton(options['Start']['xStart'], options['Start']['yStart'],
                     options['Start']['xEnd'], options['Start']['yEnd'], 'Start')
    createButtons()
    app.updateButton('Start')
    root.mainloop()

def createStoryFrame(text):
    storyFrame = LabelFrame(app.master, text=text, background='#F1F1F1')
    storyFrame.grid(row=2, column=1, columnspan=2)

    return storyFrame

def createButtons():
    buttonFrame = Frame()
    buttonFrame.grid(row=1, column=0, rowspan=6)

    storyFrame = createStoryFrame('')

    OfficeButton=Button(buttonFrame, text="Office",
                        command= lambda: Office(app.master, storyFrame), width=12,
                        height=4, borderwidth=2, relief="solid",
                        background="#91683C")
    OfficeButton.grid(column=0, row=5, pady=5)

    NurseryButton=Button(buttonFrame, text="Nursery", 
                        command= lambda: Nursery(app.master, storyFrame), width=12,
                        height=4, borderwidth=2, relief="solid",
                        background="#C19E77")
    NurseryButton.grid(column=0, row=4, pady=5)

    LoungeButton=Button(buttonFrame, text="Lounge", 
                        command= lambda: lounge(app.master, storyFrame), width=12,
                        height=4, borderwidth=2, relief="solid",
                        background="#D4C0AB")
    LoungeButton.grid(column=0, row=3, pady=5)

    KitchenButton=Button(buttonFrame, text="Kitchen", 
                        command= lambda: Kitchen(app.master, storyFrame), width=12,
                        height=4, borderwidth=2, relief="solid",
                        background="#E8DCD0")
    KitchenButton.grid(column=0, row=2, pady=5)
    
    Basement=Button(buttonFrame, text="Basement", 
                    command= lambda: EnterBasement(app.master, storyFrame), width=12,
                    height=4, borderwidth=2, relief="solid",
                    background="#F1F1F1" )
    Basement.grid(column=0, row=1, pady=5)

def EnterBasement(root, basementFrame):
    basementFrame.destroy()
    basementFrame = createStoryFrame('Basement')

    BasementText= Label(basementFrame, text= BaseText)
    BasementText.grid(row=0, column=0, columnspan=2)

    GoodEndingBase=Button(basementFrame, text="Be Nice", width=12, height=4, 
                    borderwidth=2, relief="solid", background="#F1F1F1")
    GoodEndingBase.grid(column=0, row=1)

    BadEnding=Button(basementFrame, text="Be Mean", width=12, height=4, 
                     borderwidth=2, relief="solid", background="#F1F1F1",)
    BadEnding.grid(column=1, row=1)

    GoodEndingBase['command'] = lambda: BaseGoodEnding(basementFrame, BasementText, GoodEndingBase, BadEnding)
    BadEnding['command'] = lambda: BaseBadEnding(basementFrame, BasementText, GoodEndingBase, BadEnding)
    
    app.updateButton('Basement')

def BaseGoodEnding(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    BseGoodEnding=Label(root, text=BaseTextGood)
    BseGoodEnding.grid(row=0, column=0,columnspan=2)

    app.updateButton('Help')

def BaseBadEnding(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    BseBadEnding=Label(root, text=BaseTextBad)
    BseBadEnding.grid(row=0, column=0, columnspan=2)
    
    app.updateButton("Don't help")

def Kitchen(root, kitchenFrame):
    kitchenFrame.destroy()
    kitchenFrame = createStoryFrame('Kitchen')

    KitchenText=Label(kitchenFrame, text= Kitchentextpt1)
    KitchenText.grid(row=0, column=0,
                     columnspan=2)
    Part2=Button(kitchenFrame, text = "Next", width=12, height=4, 
                 borderwidth=2, relief="solid", background="#E8DCD0")
    Part2.grid(row=1 ,column=0, columnspan=2)

    Part2['command'] = lambda: KitchenPart2(kitchenFrame, KitchenText, Part2)

def KitchenPart2(root, text, button):
    text.grid_forget()
    button.grid_forget()

    KitchenText2=Label(root, text=Kitchentextpt2)
    KitchenText2.grid(row=0, column=0, columnspan=2)

    Part3=Button(root, text = "Next", width=12, height=4,   
                 borderwidth=2, relief="solid", background="#E8DCD0")
    Part3.grid(row=1 ,columnspan=2)
    
    Part3['command'] = lambda: KitchenPart3(root, KitchenText2, Part3)

def KitchenPart3(root, text, button):
    text.grid_forget()
    button.grid_forget()

    KitchenText3=Label(root, text=Kitchentextpt3)
    KitchenText3.grid(row=0, column=0, columnspan=2)

    EscapeButton=Button(root, text="Escape", width=12, height=4,    
                        borderwidth=2, relief="solid", background="#E8DCD0")
    EscapeButton.grid(row=1, column=0)

    FightButton=Button(root, text="Fight", width=12, height=4, 
                       borderwidth=2, relief="solid", background="#E8DCD0")
    FightButton.grid(row=1, column=1)

    EscapeButton['command'] = lambda: Escaperobot(root, KitchenText3, EscapeButton, FightButton)
    FightButton['command'] = lambda: Fightrobot(root, KitchenText3, EscapeButton, FightButton)

    app.updateButton("Kitchen")

def Escaperobot(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    KitchenTextPt3=Label(root, text=EscapeRobot) 
    KitchenTextPt3.grid(row=2, column=0, columnspan=2)

    app.updateButton("Escape")

def Fightrobot(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    fightRobot=Label(root, text=FightRobot)
    fightRobot.grid(row=2, column=0, columnspan=2)

    app.updateButton("Fight")

def lounge(root, loungeFrame):
    loungeFrame.destroy()
    loungeFrame = createStoryFrame('Lounge')

    LoungeText=Label(loungeFrame, text=Loungetext)
    LoungeText.grid(row=0, column=0, columnspan=2)

    GoodEndinglounge=Button(loungeFrame, text = " Yes, Thats me ", width=12, height=4, 
                            borderwidth=2, relief="solid", background="#D4C0AB")
    GoodEndinglounge.grid(row=1, column= 0)

    BadEndingLounge=Button(loungeFrame, text = "No, That isn't me", width=12, height=4, 
                           borderwidth=2, relief="solid", background="#D4C0AB")
    BadEndingLounge.grid(row=1, column= 1)

    GoodEndinglounge['command'] = lambda: YesThatIsMe(loungeFrame, LoungeText, GoodEndinglounge, BadEndingLounge)
    BadEndingLounge['command'] = lambda: NoThatIsNotMe(loungeFrame, LoungeText, GoodEndinglounge, BadEndingLounge)

    app.updateButton("Lounge")

def YesThatIsMe(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    PositiveAnswer=Label(root, text=YesThatIs)
    PositiveAnswer.grid(row=0, column=0, columnspan=2)

    CoffeeButton=Button(root,text="Yes, please", width=12, height=4, 
                        borderwidth=2, relief="solid", background="#D4C0AB")
    CoffeeButton.grid(row=1, column=0)

    DeclineCoffeeButton=Button(root, text="No, Thanks", width=12, height=4, 
                               borderwidth=2, relief="solid", background="#D4C0AB")
    DeclineCoffeeButton.grid(row=1, column=1)

    CoffeeButton['command'] = lambda: CoffeeYes(root, PositiveAnswer, CoffeeButton, DeclineCoffeeButton)
    DeclineCoffeeButton['command'] = lambda: CoffeeNo(root, PositiveAnswer, CoffeeButton, DeclineCoffeeButton)

    app.updateButton("Truth")

def NoThatIsNotMe(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    NegativeAnswer=Label(root, text=NoThatIsntMe)
    NegativeAnswer.grid(row=0, column=0,columnspan=2)
    
    app.updateButton("Lie")

def CoffeeNo(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    DeclineCoffee=Label(root, text=NoCoffee)
    DeclineCoffee.grid(row=0, column=0,columnspan=2)

    ChatButton=Button(root, text="Chat", width=12, height=4, 
                      borderwidth=2, relief="solid", background="#D4C0AB")
    ChatButton.grid(row=1, column=0)
    
    DontChatButton=Button(root, text="Don't chat", width=12, height=4, 
                          borderwidth=2, relief="solid", background="#D4C0AB")
    DontChatButton.grid(row=1, column=1)

    ChatButton['command'] = lambda: BeginChat(root, DeclineCoffee, ChatButton, DontChatButton)
    DontChatButton['command'] = lambda: BeginChat(root, DeclineCoffee, ChatButton, DontChatButton)

    app.updateButton("No Coffee")
    
def CoffeeYes(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    
    AcceptCoffee=Label(root, text=coffee)
    AcceptCoffee.grid(row=0, column=0, columnspan=2) 

    ChatButton=Button(root, text="Chat", width=12, height=4, 
                      borderwidth=2, relief="solid", background="#D4C0AB")
    ChatButton.grid(row=1, column=0)

    DontChatButton=Button(root, text="Don't chat", width=12, height=4, 
                          borderwidth=2, relief="solid", background="#D4C0AB")
    DontChatButton.grid(row=1, column=1)

    ChatButton['command'] = lambda: BeginChat(root, AcceptCoffee, ChatButton, DontChatButton)
    DontChatButton['command'] = lambda: ForcedChat(root, AcceptCoffee, ChatButton, DontChatButton)

    app.updateButton("Coffee")

def BeginChat(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    chat = Label(root, text=Talk)
    chat.grid(row=0, column=0, columnspan=2)

    QuestionButton=Button(root, text=" why tell me ? ", width=12, height=4, 
                          borderwidth=2, relief="solid", background="#D4C0AB")
    QuestionButton.grid(row=1, columnspan=2)

    QuestionButton['command'] = lambda: monologue(root, chat, QuestionButton)

    app.updateButton("Chat")

def ForcedChat(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    chat = Label(root, text=Talk2)
    chat.grid(row=0 , column=0 ,columnspan=2)

    QuestionButton=Button(root, text=" why tell me ? ", width=12, height=4, 
                          borderwidth=2, relief="solid", background="#D4C0AB")
    QuestionButton.grid(row=1, columnspan=2)

    QuestionButton['command'] = lambda: monologue(root, chat, QuestionButton)

    app.updateButton("Don't chat")

def monologue(root, text, button):
    text.grid_forget()
    button.grid_forget()

    Monologue=Label(root, text=Explaination)
    Monologue.grid(row=0, column=0, columnspan=2)

    FightButton=Button(root, text="Fight", width=12, height=4, 
                       borderwidth=2, relief="solid", background="#D4C0AB")
    FightButton.grid(row=1, column=0)

    FleeButton=Button(root, text="Flee", width=12, height=4, 
                      borderwidth=2, relief="solid", background="#D4C0AB")
    FleeButton.grid(row=1, column=1)

    FightButton['command'] = lambda: Fight(root, Monologue, FightButton, FleeButton)
    FleeButton['command'] = lambda: Flee(root, Monologue, FightButton, FleeButton)

    app.updateButton("Reasons")

def Fight(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    fight=Label(root, text = Fighting)
    fight.grid(row=0, column=0, columnspan=2)

    StruggleButton=Button(root, text="Struggle", width=12, height=4, 
                       borderwidth=2, relief="solid", background="#D4C0AB",)
    StruggleButton.grid(row=1, column=0)

    KnifeButton=Button(root, text="Take knife", width=12, height=4, 
                       borderwidth=2, relief="solid", background="#D4C0AB",)
    KnifeButton.grid(row=1, column=1)

    StruggleButton['command'] = lambda: struggle(root, fight, StruggleButton, KnifeButton)
    KnifeButton['command'] = lambda: knife(root, fight, StruggleButton, KnifeButton)

    app.updateButton("Stay")

def Flee(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    
    flee=Label(root, text = Running)
    flee.grid(row=0, column=0, columnspan=2)

    StruggleButton=Button(root, text="Fight", width=12, height=4, 
                      borderwidth=2, relief="solid", background="#D4C0AB",)
    StruggleButton.grid(row=1, column=0)

    WindowButton=Button(root, text="Run for window", width=12, height=4, 
                       borderwidth=2, relief="solid", background="#D4C0AB",)
    WindowButton.grid(row=1, column=1)

    StruggleButton['command'] = lambda: Fight(root, flee, StruggleButton, WindowButton)
    WindowButton['command'] = lambda: window(root, flee, StruggleButton, WindowButton)

    app.updateButton("Flee")

def struggle(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    
    struggling=Label(root, text=Struggle)
    struggling.grid(row=0, column=0, columnspan=2)

    app.updateButton("Struggle")

def knife(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    
    struggling=Label(root, text=takeKnife)
    struggling.grid(row=0, column=0, columnspan=2)

    app.updateButton("Knife")

def window(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    window = Label(root, text=runForWindow)
    window.grid(row=0, column=0, columnspan=2)

    BushesButton=Button(root, text="Jump in bushes", width=12, height=4, 
                       borderwidth=2, relief="solid", background="#D4C0AB",)
    BushesButton.grid(row=1, column=0)

    ScaleButton=Button(root, text="Climb down", width=12, height=4, 
                       borderwidth=2, relief="solid", background="#D4C0AB",)
    ScaleButton.grid(row=1, column=1)

    BushesButton['command'] = lambda: bushes(root, window, BushesButton, ScaleButton)
    ScaleButton['command'] = lambda: scale(root, window, BushesButton, ScaleButton)

    app.updateButton("Window")

def bushes(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    
    bushes=Label(root, text=jumpForBush)
    bushes.grid(row=0, column=0, columnspan=2)

    app.updateButton("Jump")

def scale(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    
    bushes=Label(root, text=jumpForBush)
    bushes.grid(row=0, column=0, columnspan=2)

    app.updateButton("Climb")

def Nursery(root, nurseryFrame):
    nurseryFrame.destroy()
    nurseryFrame = createStoryFrame('Nursery')

    NurseryText=Label(nurseryFrame, text=NurseryStory)
    NurseryText.grid(row=0, column=0, columnspan=2)

    GoodEndingNursery=Button(nurseryFrame, text = "Be nice", width=12, height=4, 
                             borderwidth=2, relief="solid", background="#C19E77")
    GoodEndingNursery.grid(row=1, column=0)

    BadEndingNursery=Button(nurseryFrame, text = "Be mean", width=12, height=4, 
                            borderwidth=2, relief="solid", background="#C19E77")
    BadEndingNursery.grid(row=1, column=1)

    GoodEndingNursery['command'] = lambda: NurseryGDEnding(nurseryFrame, NurseryText, GoodEndingNursery, BadEndingNursery)
    BadEndingNursery['command'] = lambda: NurseryBDEnding(nurseryFrame, NurseryText, GoodEndingNursery, BadEndingNursery)

    app.updateButton('Nursery')

def NurseryGDEnding(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    NrsGoodEnding=Label(root, text=NurseryGoodEnding)
    NrsGoodEnding.grid(row=0, column=0,columnspan=2)

    app.updateButton('Listen')

def NurseryBDEnding(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    NrsBadEnding=Label(root, text=NurseryBadEnding)
    NrsBadEnding.grid(row=0, column=0,columnspan=2)
    
    app.updateButton('Hack')


def Office(root, officeFrame):
    officeFrame.destroy()
    officeFrame = createStoryFrame('Office')
    
    OfficeText=Label(officeFrame, text=OfficeStory)
    OfficeText.grid(row=0, column=0, columnspan=2)

    GoodEndingOffice=Button(officeFrame, text = "Be nice", width=12, height=4, 
                            borderwidth=2, relief="solid", background="#91683C")
    GoodEndingOffice.grid(row=1, column=0)

    BadEndingOffice=Button(officeFrame, text = "Be mean", width=12, height=4, 
                           borderwidth=2, relief="solid", background="#91683C")
    BadEndingOffice.grid(row=1, column=1)

    GoodEndingOffice['command'] = lambda: OfficeGoodEnding(officeFrame, OfficeText, GoodEndingOffice, BadEndingOffice)
    BadEndingOffice['command'] = lambda: OfficeBadEnding(officeFrame, OfficeText, GoodEndingOffice, BadEndingOffice)

    app.updateButton('Office')

def OfficeGoodEnding(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    OffGoodEnding=Label(root, text=OfficeTextGood)
    OffGoodEnding.grid(row=0, column=0,columnspan=2)

    app.updateButton('Talk')

def OfficeBadEnding(root, text, button1, button2):
    text.grid_forget()
    button1.grid_forget()
    button2.grid_forget()

    OffBadEnding=Label(root, text=OfficeTextBad)
    OffBadEnding.grid(row=0, column=0,columnspan=2)

    app.updateButton('Steal')

if __name__ == '__main__':
    main()
