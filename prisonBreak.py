def prisonBreak():
  #variables 
  dOW = ""
  cOD = ""
  iOC = ""
  #background story
  print("You wake up in a dark one window room with a bared door.")
  print("your head aches and you feel like you have been knocked out for a while.")
  print("You go and look out the window and endless ocean.")
  print("You seem to be mulitple stories up.")
  #first choice
  dOW = input("Do you want to go through the door or the window?")
  if dOW == "door":
    print("You try to open the door but it is locked.\nYou try to break it down but it is too strong.")
    print("A guard hear's you and rushes to your cell.")
    print("Guard: You are going to be in a cell for a long time. So don't even think of trying to escape.")
  elif dOW == "window":
    print("You look out the window and see an other window a few feet away.")
    #second choice
    cOD = input("Do you want to climb out the window or go try the door?")
    if cOD == "climb":
      print("You climb out the window and fall into the ocean.")
      print("You are now in the middle of the ocean and you can't see anything.")
    elif cOD == "door":
      print("You try to open the door but it is locked.\nYou try to break it down but it is too strong.")
      print("A guard hear's you and rushes to your cell.")
      print("Guard: You are going to be in a cell for a long time. So don't even think of trying to escape.")
      #third choice
      iOC = input("Do swim back to the island or ty and swim to the city on the horizon.")
      if iOC == "city":
        print("You swim towards the city.\nThen you see skyscrapers.\nWith the city now in veiw you being to swim faster.")
prisonBreak()
  