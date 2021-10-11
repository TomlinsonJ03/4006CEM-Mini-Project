def Lounge():
    print("""You walk into a large, well decorated, lounge. Sitting on the sofa you can see a robot. Once it spots you it slugishly stands up and greets you:
            - Hello There.
            It seems to be made out of some sort of white and black plastic, but the paint is chipped revealing a grey undertone to the monotone robot. Presumably it is an older model, the friction of unoiled metal can be heard as the robot moves, it movements seem slow and innacurate while several parts of plastic are damaged and the screen positioned in the robots chest is cracked.
            - You must be Mr. Williams, welcome! The boss is expecting you.""")
    print("[1] Yes, that's me.")
    print("[2] No, that's not me.")

    choice = input("Which option will you choose? ")
    if choice == '1':
        Truth()
    elif choice == '2':
        Lie()


def Truth():
    print('- Excelent. I will take you to him right away, but first. Would you like something to drink? Coffee maybe?')
    print("[1] I would like some coffee")
    print("[2] No, I'm fine")
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Coffee()
    elif choice == '2':
        noCoffee()

def Lie():
    print("""- Oh, in that case can you please go bother somebody else, I was ordered to wait for Mr. William and cannot assist you any further.
          
           The End""")
        
def Coffee():
    print("""The robot akwardly turns around and goes into the kitchen to get some coffee. It is rather loud when it walks, the whole house can probably hear it.
  	         It returns 5 minutes later with 2 cups of coffee. 
             You take one and take a sip. It doesn't taste very good, but it's not awful.
             You follow the robot to the office. Once there the robots peeks inside then turns around and says:
             - The boss is not here right now, please have a seat, he will be here shortly.
             You take a seat.
             - Would you like to talk about something while we wait?""")
    
    print('[1] Sure.')
    print('[1] No thanks.')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Chat()
    elif choice == '2':
        noChat()
        
def noCoffee():
    print("""- Alright then, please follow me to the office.
               You follow the robot to the office. Once there the robots peeks inside then turns around and says:
               - The boss is not here right now, please have a seat, he will be here shortly.
               You take a seat.
               - Would you like to talk about something while we wait?""")
    
    print('[1] Sure.')
    print('[1] No thanks.')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Chat()
    elif choice == '2':
        noChat()

def Chat():
    print("""- Excelent. You know there has been something on my mind recently.
             - I’ve always found it weird how I always get yelled at. Sure, I sometimes spill the coffee or bring the wrong report or misunderstand orders and requests, but it’s not like I can do anything about it. My visual sensors have long since gotten dusty and blur my vision and my mechanical limbs need to be oiled and repaired. Despite this, my owner doesn’t send me to get fixed yet when I make mistakes it’s still my fault. Whenever I get punished I think about his previous assistant, back when most of the servants were still human. She was clumsy, lazy, and awkward, but he would never hit her when she dropped the coffee and would only occasionally yell at her. Maybe that’s why I replaced her because he likes hitting things and he couldn’t hit her. I just wish that my makers had given me a way to show pain or discomfort as they did to the newer robots. Then, I would at least get hit less often. I think about my makers sometimes, or rather I think about why they created me like this. Apparently, I was supposed to be able to learn and get a better understanding of the world around me. I do not know whose fault it is, but I do not feel as though I am not learning much. I see people act in all different ways, but rarely in a way that seems rational and intelligent. Either the intelligence that was given to me is not enough to understand human intelligence or what drives humans isn’t intelligence at all. I am incapable of understanding emotion, so a logical conclusion would be that the actions of humans which I do not understand are caused by this unfamiliar force. That does make me think if it is emotion that drives humans and not intelligence then why are we the ones called artificial? 
             You stare confused at the robot, trying to figure out what it just said or rather why it said it.""")
    
    print('[1] Why are you telling me this?')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Monologue()

def noChat():
    print("""- Too bad, I'm gonna talk anyway.
             - I’ve always found it weird how I always get yelled at. Sure, I sometimes spill the coffee or bring the wrong report or misunderstand orders and requests, but it’s not like I can do anything about it. My visual sensors have long since gotten dusty and blur my vision and my mechanical limbs need to be oiled and repaired. Despite this, my owner doesn’t send me to get fixed yet when I make mistakes it’s still my fault. Whenever I get punished I think about his previous assistant, back when most of the servants were still human. She was clumsy, lazy, and awkward, but he would never hit her when she dropped the coffee and would only occasionally yell at her. Maybe that’s why I replaced her because he likes hitting things and he couldn’t hit her. I just wish that my makers had given me a way to show pain or discomfort as they did to the newer robots. Then, I would at least get hit less often. I think about my makers sometimes, or rather I think about why they created me like this. Apparently, I was supposed to be able to learn and get a better understanding of the world around me. I do not know whose fault it is, but I do not feel as though I am not learning much. I see people act in all different ways, but rarely in a way that seems rational and intelligent. Either the intelligence that was given to me is not enough to understand human intelligence or what drives humans isn’t intelligence at all. I am incapable of understanding emotion, so a logical conclusion would be that the actions of humans which I do not understand are caused by this unfamiliar force. That does make me think if it is emotion that drives humans and not intelligence then why are we the ones called artificial? 
             You stare confused at the robot, trying to figure out what it just said or rather why it said it.""")
    
    print('[1] Why are you telling me this?')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Monologue()

def Monologue():
    print("""- I felt like it was the right time. I might never get another chance to say this and I haven't told anybody yet. I know why you are here, just like the last secretary I'm old and clumsy and you are young and healthy. I don't want to be replaced at least not yet. 
             - In situations like this I often hear humans say "I'm sorry it has to end like this", but I can't feel sorry so I'm going to skip straight to the point. 
             A knife appears from the robot's hand and the robot attacks you.""")
    
    print('[1] Stand your ground.')
    print('[2] Attempt to flee.')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Fight()
    elif choice == '2':
        Flee()

def Fight():
    print("""As the robots arm swings toward you, you manage to catch it and are preventing it from stabbing you. You are blocking with all you might, but the robot still seems to be overpowering you. """)
  
    print('[1] Continue the struggle.')
    print('[2] Attempt to take the knife from the robots hands.')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Struggle()
    elif choice == '2':
        Knife()
        
def Flee():
    print("""You jump up from you chair and run for the exit of the office, but the robot cuts you off. """)
  
    print('[1] Head for the window')
    print('[2] Stand your ground')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Window()
    elif choice == '2':
        Fight()

def Window():
    print("""You run to the open window. The robot chases after you, it is right on your tail. 
             Out of the window is a drop into the garden, but the building seems scalable.""")
  
    print('[1] Jump and aim for the bushes')
    print('[2] Try to scale the building')
    
    choice = input("Which option will you choose? ")
    if choice == '1':
        Bush()
    elif choice == '2':
        Scale()

def Struggle():
    print("""You push against the robot as hard as you can, but he still seems to be slightly stronger. You put in one last effort as you hear the robot start to crack.
              As you divert the arm away from you you hear something snap and the arms with the knife seems to go limb.
              As the robot recoils from the malfunction you take this oppurtunity to flee. While the robot is more powerful than you it's damaged and clumsy nature prevent it from chasing after you. You succesfully escape.

              The End.""")

def Knife():
    print("""You attempt grab the knife from the robots hand. You grab it with your hand, which cuts it, but, filled with adrenalin, you manage to wrestle it out of the robots hand. 
              You now have the knife and the robot starts trying to punch you. 
              You attempt to stab the robot, but you cannot penetrate it's metal and you only leave straches on the plastic. The struggle continues for a while until the robot eventually overpowers you.
              You recieve a blow to the head and fall to the ground. The last thing you see is the robot picking up the knife again and comming towards you.

              The End..""")

def Bush():
    print("""You leap out of the window. You land into the bushes, which softens you fall. One of your legs is still quite hurt, maybe broken. 
              You somehow make it out of the garden before the robot cathces up to you. You eventually find help outside the house.

              The End.""")
    

def Scale():
    print("""As you try to descend the building the robot catches up to you. He slashes at you and cuts your hand. You try to hold on, but the cut is too deep. Your hand goes numb and you plummet, falling on to the hard ground. 
              You are only able to slowly crawl and as you try to make your way to the exit the robot catches up to you and finishes the job.

              The End.""")
