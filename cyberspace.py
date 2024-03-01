def cyberSpace():
#setting variables
  fight = False
  fOR = ""
  lOR = ""
  inOIg = ""
  sOE = ""
  home = ""
  finalResult = ""
#start of the story
  print("Welcom to Cyber Space")
  print("You don't rember who you are but you do know where you are and where your from. You are a user traped in a cyber space and you need to get out. You are in some kind of cyber jall.")
  print("There is a door and a window.\n")
  print("You can either go through the door or out the window.")

  #first choice
  dOW = input("The choice is your's: Do you want to go through the door or the window?")
  if dOW == "door": #1
    print("You go know that the door is locked, so you ram it with all of your strenght.\n")
    print('You break the door down and see a guard at the end of the hallway.\n')
    print("You can either fight the guard or run away.\n")
    fOR = input("Do you want to fight the guard or run away?")
  elif dOW == 'window': #1
    print("With out thinking you jump sensly out the window and fall into a bottemless pit.\n")
    finalResult = 'Game over'

    #second choice
    if fOR == "fight": #2
      print("You fight the guard and you win, however you don't think that you will be able to that again.\n")
      print("You enter a hallway and you see a door on the left and another one on the right.\n")
      lOR = input("Do you want to go through the door on the LEFT or the door on the RIGHT?")
      fight = True
    elif fOR == "run": #2
      print('\nYou turn the other way and run as fast as you can.')
      print('You run straight into another guard and he sprays you with knockout gas.')
      print('You wake up back in your cell')
      finalResult = 'Game over'

      #third choice
      if lOR == "LEFT": #3
        print("You go through the door on the left and you see a fellow inmate. You and the inmate lock eyes for just a moment.")
        print("You can either ignore them and pretend that you didn't see them or you can go and speak to them.")
        inOIg = input("Do you ignore or speak?")
        left = True
        right = False
        #fourth choice
        if inOIg == "ignore": #4
          ignore = True
          speak = False
          print('You chose to ignore them and you pretend that you didn\'t see them. Just as you dash out of the room, you see a guard coming down the hallway. You run abandoing the inmate, who looks at you one last time. His eyes, will haunt you for the rest of your life.')
          finalResult = 'Through you esacape cyber space you are very unhappy.\n You win and lose.'
        elif inOIg == "speak": #4
          ignore = False
          speak = True
          print('You walk over to the inmate and you say that you are lost and you need help. The inmate says that he can help you. Just then a gaurd comes down the hallway and sees you. He yells at you to frezze.')
          fOR = input('Do you want to fight the guard or run away?')
      elif lOR == "RIGHT": #3
        print('You go through the door on the right and you see 2 doors. One leads to the stairs and the other leads to the eleivator.')
        #Fith choice
        sOE = input("Do you go to the stairs or the elevator?")
        if sOE == "stairs": #5
          print('You take the stairs and you find a portal to the users world. Your home. You can finaly go back home.')
          #sixth choice
          home = input('But will you have the corrage to return home?(y/n): ')
          if home == "y": #6
            print('You go back home and you are happy that you have finally escaped cyber space.')
            finalResult = 'You win!'
          elif home == "n": #6
            print('You decide that you don\'t want to go back to the user\'s and you stay in cyber space living the rest of your days happy with your life choices.')
            finalResult = 'You win!'
        elif sOE == "elevator": #5
          print('You go to the elevator and you see a button that says "emergency exit". You press it')
          print('You wake up back in your cell')
          finalResult = 'Game over!'
  return finalResult