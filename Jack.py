# Entering the Basement
def basement():
  print("""
        I will walk into the basement, there seems to be a robot there, working hard it seems. They don’t see the things the way I do, it exclaimed. 
        I wander what it means, see what? Maybe I will approach it and find out. It seems to be working on some kind of budgeting, the finances of the family perhaps. 
        However, it is scribbling the words free will, programming. Perhaps the robot’s have some sort of sentience, 
        Maybe the robot in the garden has a passion for that sort of thing, maybe robots love to cook. But then again, this one doesn’t seem to love what it’s doing, 
        more like, it knows that it’s simply a slave who isn’t allowed to do as it pleases. Maybe it ignored me because it hopes that I will make a choice, 
        will I save the robot or leave it be. No surely not, a robot has no free thought, it’s just an AI with programming, 
        no-one would program a robot to hate what it is doing, do they have such emotions? How do you make it so a robot can experience such things, 
        would it be considered real if so? I suppose I must make a choice.
        """)
  
  print("1: Unplug the robot")
  print("2: Leave the robot to suffer")
  
  choice = int(input("Which option will you choose? "))
  if choice == 1:
    unplugRobot()
  elif choice == 2:
    robotSuffer()
  
# Unplug the robot
def unplugRobot():
  print("""
      I ponder the overall necessity for the robot and weight in the possible consequences that could unravel if it was no longer active. 
      None surpassed a high enough level of degree to garner concern, I lay my finger upon a circular button illuminated by a warm white led, 
      I press it and enjoy a moment of silence as its internal components hum until still. 
      I then unplug the robot and take the power cord with me in hope of the robot never being activated again.  
      """)
  
# Let the robot suffer
def robotSuffer():
  print("""
      I notice the robot in despair and locate the unorganized box of components and stripped wires, I turn of the robot and begin swapping out parts, 
      refitting incorrect capacitors and resistors, mismatch the organized wiring with a mesh of unsafe wires and leave the existing body panels in front of 
      its visual sensor to gaze upon until next reset. 
      """)