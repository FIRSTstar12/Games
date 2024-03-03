import random
#Main Story Line
def prisonBreakMainStoyLine():
  #background story
  print("You wake up in a dark one window room with a bared door.")
  print("your head aches and you feel like you have been knocked out for a while.")
  print("You go and look out the window and endless ocean.")
  print("You seem to be mulitple stories up.\n")
#door
def prisonBreakFirstChoiceDoor():
  #first choice
    print("You try to open the door but it is locked.\nYou try to break it down but it is too strong.")
    print("A guard hear's you and rushes to your cell.")
    print("Guard: You are going to be in a cell for a long time.\n So don't even think of trying to escape.")
    print("The way you see it you have 2 options: \n1) try to steal the gaurd's keys or \n2) ask where you are.\n")
def prisonBreakAfterDoorChoiceSteal():
  num = random.randint(1,2)
  if num == 1:
    print("You try to steal the gaurd's keys but he catches you and you are sent to solitary confinement.")
    print("Game over.")
    return 1
  else:
    print("You try to steal the gaurd's keys and you succeed.")
    print("You carefully open the door and shut it behind you as quitly as you can.")
    print("Your in the middle of a short hallway with a door on the left and a door on the right.\n")
    return 2
def prisonBreakLeftHallway():
  print("You go through the door on the left and don't see anyone, just a window.\n")
def prisionBreakRightHallway():
  print("You go through the door on the right and you see 2 doors. \nOne leads to the stairs and the other leads to the eleivator.")
def prisionBreakBoat():
  print("You jump on the boat and you spead off into the ocean. \nYou are never seen again.")
  print("You Win!")
def prisionBreakHelicoptor():
  print("You get in the helicoptor and rember that you can't fly a helicoptor. \nGuards surround you and you are sent to solitary confinement.")
  print("Game over.")
def prisonBreakAfterDoorChoiceAsk():
  print("Decide that the best course of action is to ask where you are.")
  print("Guard: Welcome to Grayscape Prison. \nYou'll be here for a long l-o-n-g time.")
  print("Before you can ask anything eles the guard rushes off.")
def prisonBreakElevator():
  print("You go to the elevator and you see a button that says 'emergency exit'. \nYou press it. \nYou wake up in solitary confinement.")
  print("Game over.")
#window
def prisonFirstChoiceWindow():
    print("You look out the window and see an other window a few feet away.")
def prisonBreakSecondChoiceClimb():
      print("You climb out the window and fall into the ocean.")
      print("You are now in the middle of the ocean and you can't see anything.")
#for the other side of this coin use FirstChoiceDoor
def prisonBreakThirdChoiceCity():
  print("You swim towards the city.\nThen you see skyscrapers.\nWith the city now in veiw you being to swim faster.")
  print("When you arrive at the shore of the city you can ether crawl up the middle of the shore or you can crawl up the side of the shore.")
def prisionBreakThirdChoiceIsland():
  print("You can't see any land besides the island that the prison is on so you decide to swim back.")
  print("As you are swimming back you see a sign that says 'Welcom to Grayscape Prison and Correction faciity'.")
  print("Suddenly a big spotlight hits you. A loudspeaker says 'FREZE WE ARE COMING TO GET YOU.'")
def prisionBreakRunAway():
  print("You don't want to get sent back to jall so you try and swim for it.")
  print("You make it all the way to the city where you are now free.")
  print("YOU WIN!")
def prisonBreakFrezze():
  print("You don't want to risk getting lost so you decide to stay put.")
  print("When they come to get you they send you back to your cell.")
#back to main story line
def prisionBreakMiddle():
  print("You crawled up the middle of the shore and a uniformed man sees you. \nHe sprays you with something and you wake up in solitary confinement.")
  print("Game over.")
def prisionBreakSide():
  print("You crawl up the side of the shore and hid behind a rock and wait for dark. \nJust then all of your memories come back to you.")
  name = input("What is your name?: ")
  age = int(input("How old are you?: "))
  print("You are " + name + " and you are " + str(age) + " years old.")
  print("CONGARDULATIONS!" + name + "YOU WIN!")