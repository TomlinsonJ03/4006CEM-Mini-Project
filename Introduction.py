import Zaakir
import Jack
import Ramba
import Kay
import Filip

def introduction(): 
  print ("""
        As I finish scouting out the area, I breathe a sigh of relief. The homeowners are out right now, probably out playing golf or something; rich people stuff. I stealthily walk towards the front door, 
        making sure to block the camera signals watching the front entrance using my makeshift jamming device. I lockpick the front door, and with a soft ‘click’, I open the door and enter the house. 
        Damn, the exterior of the house looked impressive, but it simply paled in comparison to the interior. The place was *huge*. 
        As I gape in awe at the impressive indoor architecture, I hear a gentle hum; The sound of online robots, it seems. 
        I’m torn between which room to enter first; I need to take what I can and leave as soon as possible, I can’t risk getting caught. I simply have too much to lose. 
        """)
  
  print("1: Enter the office")
  print("2: Enter the basement")
  print("3: Enter the nursery")
  print("4: Enter the kitchen")
  print("5: Enter the lounge")
  
  choice = int(input("Which option will you choose? "))
  if choice == 1:
    Zaakir.office()
  elif choice == 2:
    Jack.basement()
  elif choice == 3:
    Ramba.nursery()
  elif choice == 4:
    Kay.kitchen()
  elif choice == 5:
    Filip.Lounge()
    
introduction()