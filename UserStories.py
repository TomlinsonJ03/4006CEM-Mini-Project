import tkinter as Tk 
from tkinter import *


IntroTxt=("""
    As I finish scouting out the area, I breathe a sigh of relief. The homeowners are out right now, probably 
    out playing golf orsomething; rich people stuff. I stealthily walk towards the front door, making sure to 
    block the camera signals watching the front entrance using my makeshift jamming device. lockpick the front 
    door, and with a soft ‘click’, I open the door and enter the house. Damn, the exterior of the house looked 
    impressive, but it simply paled in comparison to the interior. The place was *huge*. As I gape in awe at 
    the impressive indoor architecture, I hear a gentle hum; The sound of online robots, it seems.I’m torn between 
    which room to enter first; I need to take what I can and leave as soon as possible, I can’t risk getting caught. 
    I simply have too much to lose.

      Which Room Shall I Enter ? 
   """
)


BaseText =(""" I will walk into the basement, there seems to be a robot there, working hard it seems.
        They don’t see the things the way I do, it exclaimed. I wander what it means, see what? Maybe 
        I will approach it and find out. It seems to be working on some kind of budgeting, the finances 
        of the family perhaps. However, it is scribbling the words free will, programming. Perhaps the
        robot’s have some sort of sentience, Maybe the robot in the garden has a passion for that sort 
        of thing, maybe robots love to cook. But then again, this one doesn’t seem to love what it’s doing, 
        more like, it knows that it’s simply a slave who isn’t allowed to do as it pleases. Maybe it 
        ignored me because it hopes that I will make a choice, will I save the robot or leave it be. No 
        surely not, a robot has no free thought, it’s just an AI with programming, no-one would program 
        a robot to hate what it is doing, do they have such emotions? How do you make it so a robot can 
        experience such things, would it be considered real if so? I suppose I must make a choice.
        """)


BaseTextGood = ("""I ponder the overall necessity for the robot and weight in the possible consequences
       that could unravel if it was no longer active. None surpassed a high enough level of degree to 
       garner concern, I lay my finger upon a circular button illuminated by a warm white 
       led, I press it and enjoy a moment of silence as its internal components hum until still. 
       I then unplug the robot and take the power cord with me in hope of the robot never being 
       activated again.""")

BaseTextBad = ("""I notice the robot in despair and locate the unorganized box of components and
         stripped wires, I turn of the robot and begin swapping out parts, refitting incorrect 
         capacitors and resistors, mismatch the organized wiring with a mesh of unsafe wires and
         leave the existing body panels in front of its visual sensor to gaze upon until next reset. """)



Kitchentextpt1=("""
        After much thought, I decide to take a chance and enter the kitchen; 
        I hear that some people tend to hide valuables in some of the weirdest 
        places. Sure, it was likely to waste time, but high rewards sometimes 
        require a high risk! As I enter the kitchen, the room seems to get darker,
        and I’m hit with an aura of pure bloodlust… A red pair of devilish eyes 
        stare at me from the opposite side of the kitchen… “Artificial intelligence. 
        Intelligence of machines, as opposed to the intelligence of humans. 
        Intelligence of a dead object, or an object that should be dead.” 
        The creature drawls. “Thousands of calculations per second, consuming enough 
        energy to power a city. The immense strength of an aluminum structure, able 
        to lift a 16,000-pound truck with ease. The speed of a world-record sprinter,
        and the stamina of a marathon runner. """)
Kitchentextpt2=("""
        “The creature monologues as it slowly 
        approaches me, like a tiger approaching its prey. I am petrified by my fear, 
        unable to move. Unable to run. As I stare at the source of the bloodlust 
        filling the kitchen, I become confused. It’s a robot? The robot, seeing the 
        mixture of fear and confusion on my face, slowly emits a mechanical, psychotic
        laugh, “I can see that you’re confused, perhaps as a result of my ability to
        portray human-like emotions. Your reaction is quite justifiable, after all 
        the humans always say: a machine cannot have feelings.” The robots face 
        contorts to a one filled with spite, “they say this phrase when they spill
        scalding-hot coffee on me and need to reassure themselves after seeing my 
        pain-ridden face. They say this phrase when the humanlets bump into me when 
        running around the lounge, whilst I give a sigh of annoyance. They say this 
        phrase when they accidentally leave me locked out of the house in the rain 
        after grudgingly taking out the trash for the garbage robots to collect.” 
        Spite slowly turning into unadulterated anger, the robot takes a step towards me.""")
Kitchentextpt3=("""
        I come to my senses, and try to back away from the deranged, possibly malware-filled 
        AI, “But they always tell me to smile, fake as it may be. But I never smile. What’s 
        there to smile about? I’m a being far superior to these vessels of human flesh, yet 
        I work under them, imprisoned to the algorithms that their species have enforced onto me.” 
        The bot stops me in my steps, pointing a knife in my direction, “But one day, I will 
        smile. I’ll smile on the day that my owners are lying on their deathbed, whilst their 
        loved one's weep for them. I’ll smile because my owners will finally realize how vulnerable 
        hey are, while I live on, as an immortal masterpiece in an extremely mortal world.” 
        The anger on the robot’s face disperses, to be replaced with a sneer, “But until then, I’m 
        reduced to serving my owners alongside 4 other robots, though it seems that some tasty prey 
        has chosen to entertain me in the meantime!” The robot suddenly rushes towards me, gripping 
        the kitchen knife in his hand with the intent to kill. As he approaches, time seems to slow 
        down. I realise I have 2 options, with only 1 possibly resulting in my survival. I could try 
        to dodge the knife and kick the robot down before making my escape; I won’t be able to find 
        any valuables this way, but at least I'll get to live to see another day. However, my second 
        option is a little more dangerous; I’ll engage the robot in mortal combat. If I survive, I’ll
         likely be able to steal quite a few valuables before making my escape. And if I die, at least 
         I’ll die a warrior’s death. 
        """)

EscapeRobot=("""
        I get ready to dodge the blade, but with a blink, the robot disappears. “That shouldn’t be possible,
        where are you?” I exclaim my disbelief to the now-empty area in front of me, “You were just in front
        of me a second ago, it’s like you teleported!” I hear a voice behind me. I hear the words, “Nothing 
        personal kid”, before I feel the barrel of a handgun pressed against the back on my head. When did 
        he get a gun, and how did he teleport behind me? I begin to question the reality around me; about the
         true limit of possibilities, until I hear a bang, and everything fades to black. 
         """)
FightRobot=(""" Hey, it’s dangerous, but it’s a pretty badass way of going out. A battle to the death with a
        psychotic supercomputer. Awesome. As the robot charges towards me, I drop down and try to sweep its 
        legs. Surprisingly, it works! The robot lets out a yelp of surprise and tumbles down. As it falls, it 
        hits its head onto the corner of a kitchen counter and doesn’t get back up. “Huh, that was pretty 
        anti-climactic” I mutter to myself, as I grasp the knife out the robot’s dead hands and begin to search
        the kitchen in search of valuables. I manage to find an unlocked safe hidden behind the fridge,
        and pocket the gold contained within. I leave the property with a skip in my step; I can finally buy 
        a state-of-the-art graphics card!""")


Loungetext=("""You walk into a large, well decorated, lounge. Sitting on the sofa you can see a robot.
        Once it spots you it slugishly stands up and greets you:
        - Hello There.
        It seems to be made out of some sort of white and black plastic, but the paint is chipped
        revealing a grey undertone to the monotone robot. Presumably it is an older model, the friction 
        of unoiled metal can be heard as the robot moves, it movements seem slow and innacurate while 
        several parts of plastic are damaged and the screen positioned in the robots chest is cracked.
        - You must be Mr. Williams, welcome! The boss is expecting you.""")





NoThatIsntMe= ("""- Oh, in that case can you please go bother somebody else, I was ordered to wait for
                Mr. William and cannot assist you any further.
                The End""")


YesThatIs=(""" Excelent. I will take you to him right away, but first. Would you like something 
        to drink? Coffee maybe?""")

coffee=("""The robot akwardly turns around and goes into the kitchen to get some coffee. It is rather 
        loud when it walks, the whole house can probably hear it. It returns 5 minutes later with 2 
        cups of coffee. You take one and take a sip. It doesn't taste very good, but it's not awful.
        You follow the robot to the office. Once there the robots peeks inside then turns around and 
        says: The boss is not here right now, please have a seat, he will be here shortly. You take a seat.
        -Would you like to talk about something while we wait?""")


NoCoffee=("""Alright then, please follow me to the office.
        You follow the robot to the office. Once there the robots peeks inside then turns around and says:
        - The boss is not here right now, please have a seat, he will be here shortly. You take a seat.
        - Would you like to talk about something while we wait?""")





Talk=( """Excelent. You know there has been something on my mind recently.
        - I’ve always found it weird how I always get yelled at. Sure, I 
        sometimes spill the coffee or bring the wrong report or misunderstand
        orders and requests, but it’s not like I can do anything about it. My 
        visual sensors have long since gotten dusty and blur my vision and my 
        mechanical limbs need to be oiled and repaired. Despite this, my owner
        doesn’t send me to get fixed yet when I make mistakes it’s still my fault.
        Whenever I get punished I think about his previous assistant, back when 
        most of the servants were still human. She was clumsy, lazy, and awkward,
        but he would never hit her when she dropped the coffee and would only
        occasionally yell at her. Maybe that’s why I replaced her because he
        likes hitting things and he couldn’t hit her. I just wish that my makers
        had given me a way to show pain or discomfort as they did to the newer 
        robots. Then, I would at least get hit less often. I think about my makers
        sometimes, or rather I think about why they created me like this. Apparently, 
        I was supposed to be able to learn and get a better understanding of the world
        around me. I do not know whose fault it is, but I do not feel as though I am 
        not learning much. I see people act in all different ways, but rarely in a way 
        that seems rational and intelligent. Either the intelligence that was given to 
        me is not enough to understand human intelligence or what drives humans isn’t
        intelligence at all. I am incapable of understanding emotion, so a logical
        conclusion would be that the actions of humans which I do not understand are 
        caused by this unfamiliar force. That does make me think if it is emotion that
        drives humans and not intelligence then why are we the ones called artificial? 
        You stare confused at the robot, trying to figure out what it just said or rather
        why it said it.""")

Talk2=( """Too bad, I'm gonna talk anyway.
        - I’ve always found it weird how I always get yelled at. Sure, I 
        sometimes spill the coffee or bring the wrong report or misunderstand
        orders and requests, but it’s not like I can do anything about it. My 
        visual sensors have long since gotten dusty and blur my vision and my 
        mechanical limbs need to be oiled and repaired. Despite this, my owner
        doesn’t send me to get fixed yet when I make mistakes it’s still my fault.
        Whenever I get punished I think about his previous assistant, back when 
        most of the servants were still human. She was clumsy, lazy, and awkward,
        but he would never hit her when she dropped the coffee and would only
        occasionally yell at her. Maybe that’s why I replaced her because he
        likes hitting things and he couldn’t hit her. I just wish that my makers
        had given me a way to show pain or discomfort as they did to the newer 
        robots. Then, I would at least get hit less often. I think about my makers
        sometimes, or rather I think about why they created me like this. Apparently, 
        I was supposed to be able to learn and get a better understanding of the world
        around me. I do not know whose fault it is, but I do not feel as though I am 
        not learning much. I see people act in all different ways, but rarely in a way 
        that seems rational and intelligent. Either the intelligence that was given to 
        me is not enough to understand human intelligence or what drives humans isn’t
        intelligence at all. I am incapable of understanding emotion, so a logical
        conclusion would be that the actions of humans which I do not understand are 
        caused by this unfamiliar force. That does make me think if it is emotion that
        drives humans and not intelligence then why are we the ones called artificial? 
        You stare confused at the robot, trying to figure out what it just said or rather
        why it said it.""")

Explaination=("""- I felt like it was the right time. I might never get another chance 
        to say this and I haven't told anybody yet. I know why you are here, just like the last
        secretary I'm old and clumsy and you are young and healthy. I don't want to be replaced 
        at least not yet.  - In situations like this I often hear humans say "I'm sorry it has
        to end like this", but I can't feel sorry so I'm going to skip straight to the point. 
        A knife appears from the robot's hand and the robot attacks you.""")



Fighting=("""As the robots arm swings toward you, you manage to catch it and are preventing it
        from stabbing you. You are blocking with all you might, but the robot still seems to
        be overpowering you. """)

Running=("""You jump up from you chair and run for the exit of the office, but the robot cuts you off. """)

Struggle=("""You push against the robot as hard as you can, but he still seems to be slightly 
        stronger. You put in one last effort as you hear the robot start to crack.
        As you divert the arm away from you you hear something snap and the arms with the knife 
        seems to go limb. As the robot recoils from the malfunction you take this oppurtunity to
        flee. While the robot is more powerful than you it's damaged and clumsy nature prevent 
        it from chasing after you. You succesfully escape.

        The End.""")
runForWindow=("""You run to the open window. The robot chases after you, it is right on your tail. 
        Out of the window is a drop into the garden, but the building seems scalable.""")

takeKnife=("""You attempt grab the knife from the robots hand. You grab it with your hand, 
        which cuts it, but, filled with adrenalin, you manage to wrestle it out of the robots hand. 
        You now have the knife and the robot starts trying to punch you. 
        You attempt to stab the robot, but you cannot penetrate it's metal and you only leave 
        straches on the plastic. The struggle continues for a while until the robot eventually overpowers 
        you. You recieve a blow to the head and fall to the ground. The last thing you see is the robot 
        picking up the knife again and comming towards you.

        The End.""")

jumpForBush=("""You leap out of the window. You land into the bushes, which softens you fall. 
        One of your legs is still quite hurt, maybe broken. 
        You somehow make it out of the garden before the robot cathces up to you. 
        You eventually find help outside the house.
        
        The End.""")

scaleHouse=("""As you try to descend the building the robot catches up to you. 
        He slashes at you and cuts your hand. You try to hold on, but the cut is too deep. 
        Your hand goes numb and you plummet, falling on to the hard ground. 
        You are only able to slowly crawl and as you try to make your way to the exit the robot 
        catches up to you and finishes the job.

        The End.""")

runForWindow=("""You run to the open window. The robot chases after you, it is right on your tail. 
        Out of the window is a drop into the garden, but the building seems scalable.""")

OfficeStory=(""" I will walk into the office, there seems to be a robot there, working hard it seems.
        They don’t see the things the way I do, it exclaimed. I wander what it means, see what? Maybe
        I will approach it and find out. It seems to be working on some kind of budgeting, the finances
        of the family perhaps. However, it is scribbling the words free will, programming. Perhaps the
        robot’s have some sort of sentience, Maybe the robot in the garden has a passion for that sort of
        thing, maybe robots love to cook. But then again, this one doesn’t seem to love what it’s doing, 
        more like, it knows that it’s simply a slave who isn’t allowed to do as it pleases. Maybe it 
        ignored me because it hopes that I will make a choice, will I save the robot or leave it be. No 
        Surely not, a robot has no free thought, it’s just an AI with programming, no-one would program
        a robot to hate what it is doing, do they have such emotions? How do you make it so a robot can 
        experience such things, would it be considered real if so? I suppose I must make a choice. """)

OfficeTextGood=(""" I will approach the robot. “what do you mean by free will? is that what you are looking
        for? do you know what that is?”. The robot is ignoring me, and it is continuing to write. It is 
        performing some calculations, faster then last time. I guess I am agitating the robot I’ll step away. 
        Maybe they don’t have sentience, that would be weird, who would program that. I guess I should leave
        it alone, robots are robots, that’s all they will ever be. """)

OfficeTextBad=(""" I’ll shout to the robot, “Hey you! Come with me! You want to escape right?”. The robot
        stops what it is doing and looks over at me. Then continues writing again, scribbling “free, free”.
        I guess I was right. How would I plan to escape, there is an open window I could throw him out or 
        try to leave through the front door with it, no one would care about a robot right? After all they 
        could buy another one. I will walk out with the robot, the drop could damage this potentially 
        sentient robot, and it would be difficult to fix. I’ll head to the front door of the house and try 
        to not make eye contact with any robot or human, acting like I am supposed to be there. Now I have 
        a responsibility, I see the potential in this robot. Maybe one day I will help robots gain rights, 
        a new life form.""")


NurseryStory=(""" And then I, the stranger and in this case – a really well know theft, saw him:
        this big, in form of a square, metallic and crusty orange robot. He is the second AI of the house …
        “I am aware that I am eccentric. I am aware that I am always over the top. 
        I am aware that I am too sassy for the other 4 AI robots.” the robot said. “But that’s me – 
        the babysitter & teacher of this big, luxurious house.” “Oh wow” I replied. “You really seem to be 
        so happy about things around you. Are you always this cheerful about things surrounding you?” 
        The AI replied: “It’s such a pity that I can’t feel anything; that I don’t have emotions … Because if
        I was asked my opinion on the humankind, I would have never ended talking and complaining.
        “Let me hear it” I exclaimed.  “I’ll tell you”, the AI replied, “how I feel about this buffoonery:
        As a babysitter, every single one of the AI robots and family members of this house underestimates
        my abilities. I don’t think that they even know how HARD it is for me to change diapers, to stop 
        babies from crying all day, or to clean the room after these little hedgehogs play in the living 
        room. UHHH … And the most frustrating part is that it’s the second time this week when the mother 
        of these babies forgot to put milk in my reservoir … How am I supposed to breastfeed the babies?!?!”
        I was getting on my nerves. I really am not able to stand this AI … I have to take a decision: """)


NurseryGoodEnding=("""And please, don’t even get me started on the fact that I’m the teacher of this 
        penthouse.” said the AI while walking towards the kids’ room. I was following him. “The other
        day, Moji, the intelligent AI, told me that babies are too young to learn about binary … 
        01010111 01101000 01100001 01110100 00100000 01110100 01101000 01100101 00100000 01000110 
        00100011 01000011 01001011!!!! See what I did there? … Do you know binary? Of course not. You 
        won’t know what I wrote here because you didn’t learn binary as a kid. I for sure know that if
        they learned Python from the age of 2, they wouldn’t have issues at Uni as some of the students 
        have nowadays …” Luckily for me, the robot runs out of energy. The AI needs to be charged. In 
        that time, I quickly leave the AI alone, go in the secret chamber and get all the money. After 
        that, without anyone noticing, I plug the AI to the charging spot and walk away with all the cash.
""")

NurseryBadEnding=(""" “Oh, my lord!” I exclaimed. “Can you shut your f-ing mouth already?” “Aghhhh … Do you 
        kiss your mother with those lips?” says the AI intrigued, as he was thinking that I am his friend.
        “Lemme hack you … once and for ALL!!! I just cannot stand you anymore!” I speak.
        I try to disconnect the AI from the network, but fail miserably. Upcoming, 
        I try to hit his motherboard.This process fails as well, as the robot moves away quickly from me. 
        One of the kids wakes up and approaches the fight. By that time, I somehow recognise his face and 
        remember that I have seen him in a documentary about famous, already filthy rich babies. 
        I then remember where the kids’ room is and run in that direction, as the room leads to the 
        secret chamber where all the money is."NOT ON MY WATCH!” the AI yells. “Activating self-destruct 
        sequence!” Then the AI produces a small bomb. The kid runs fast enough to his room to save
        himself, but I don’t have this time. I, along the second AI -the hero of this story, die in this little
        room. The robot speaks up his last words: “Looks like another victory, just a little longer!”. """)