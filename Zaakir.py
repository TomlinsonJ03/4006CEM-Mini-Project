# Entering the office
def office():
  print("""
        I will walk into the office, there seems to be a robot there, working hard it seems. They don’t see the things the way I do, it exclaimed. 
        I wander what it means, see what? Maybe I will approach it and find out. It seems to be working on some kind of budgeting, the finances of the family perhaps. 
        However, it is scribbling the words free will, programming. Perhaps the robot’s have some sort of sentience, 
        Maybe the robot in the garden has a passion for that sort of thing, maybe robots love to cook. But then again, this one doesn’t seem to love what it’s doing, 
        more like, it knows that it’s simply a slave who isn’t allowed to do as it pleases. Maybe it ignored me because it hopes that I will make a choice, 
        will I save the robot or leave it be. No surely not, a robot has no free thought, it’s just an AI with programming, 
        no-one would program a robot to hate what it is doing, do they have such emotions? How do you make it so a robot can experience such things, 
        would it be considered real if so? I suppose I must make a choice.
        """)
  
  print("1: Steal the robot")
  print("2: Talk to the robot")
  
  choice = int(input("Which option will you choose? "))
  if choice == 1:
    stealRobot()
  elif choice == 2:
    talkToRobot()
  
# Stealing the robot
def stealRobot():
  print("""
      I’ll shout to the robot, “Hey you! Come with me! You want to escape right?”. The robot stops what it is doing and looks over at me. 
      Then continues writing again, scribbling “free, free”. I guess I was right. 
      How would I plan to escape, there is an open window I could throw him out or try to leave through the front door with it, no one would care about a robot right? 
      After all they could buy another one. I will walk out with the robot, the drop could damage this potentially sentient robot, and it would be difficult to fix. 
      I’ll head to the front door of the house and try to not make eye contact with any robot or human, acting like I am supposed to be there. Now I have a responsibility, 
      I see the potential in this robot. Maybe one day I will help robots gain rights, a new life form. 
      """)
  
# Talking to the robot
def talkToRobot():
  print("""
      I will approach the robot. “what do you mean by free will? is that what you are looking for? do you know what that is?”. 
      The robot is ignoring me, and it is continuing to write. It is performing some calculations, faster then last time. I guess I am agitating the robot I’ll step away. 
      Maybe they don’t have sentience, that would be weird, who would program that. I guess I should leave it alone, robots are robots, that’s all they will ever be. 
      """)
  
  