import random
def mainStoryLine():
  print("You are an exploror who is convinced that atlantis is real.\nYou are on a mission to find the lost treasure of Atlantis.")
def cave1():
  print("You enter the cave on the left and see the other side of the cave.\n")
def cave2():
  print("You enter the cave on the right and see the other side of the cave.\n")
def shark():
  print("You swim in to the cave and see a shark \n")
  num = random.randint(1,2)
  if num == 1:
    print("You get eaten by the shark.\n")
    print("Game over.")
    return 1
def eels():
  print("You swim in to the cave and see an electric eels.\n")
  num = random.randint(1,2)
  if num == 1:
    print("You get electrocuted by the eels.\n")
    print("Game over.")
    return 1
  elif num == 2:
    print("The eels ignore you.\n")
    return 2

def treasure():
  print("CONGRATULATIONS! You found the lost treasure of Atlantis.")
def run():
  print("You run away from the eel.\n")
'''
def game():
  print("Game over.")
'''