name = input("What is your name? ")
age = 6
season = ["spring","summer","fall", "winter"]
i = 0
Y6C = ["Playing Basketball By Your Self", "Watch Basketball","Playing Basketball With Friends", "Lazing around doing nothing"]
choices = []
skill = 0
know = 0
friend = 0
giveUp = False

def mainStoryLineSports():
  print("Welcome to Athletes")
  print("Pick your sport:")
  print("1 = Basketball\n2 = Soccer\n3 = Football\n4 = Baseball\n5 = Hockey\n6 = Golf\n7 = Tennis\n8 = Swimming\n9 = Track and Field\n10 = Volleyball\n11 = Rugby\n12 =  Gymnastics\n13 = Boxing")
  sport = int(input("Enter the number that corispnds to your sport.: "))
  return sport
def basketBallStoryLine1(user, age, season,i):
  print(f"Hello {user}! You are {age} years old and you have a dream. You want to be a professional basketball player.")
  print(f"What wil you spend the{season[i]} doing?")
  print("1 = Play basketball\n2 = Watch basketball\n3 = Play basketball with friends\n4 = Nothing")
  choice = int(input("Enter the number that corresponds to your choice.: "))
  choices.append(choice)
  return choice
i += 1
def basketBallStoryLine2(user, age, season):
  print(f"{user}, you spent {season[0]} {Y6C[basketBallStoryLine1(name, age, season,i=0)]}")

def stats(skill, know, friend):
  return f"Current Stats: \nSkill: {skill}\nKnowlege: {know} \nFriendship: {friend}"
while giveUp != True:
  if mainStoryLineSports() =="1":
    while i < 4:
      print(stats(skill,know,friend))
      print(f"You spend all {season[i]}{Y6C[basketBallStoryLine1(name, age, season, i) - 1]}")
      if basketBallStoryLine1(name, age, season, i) == 1:
        skill += 1
        know += 1
        friend += 0
      elif basketBallStoryLine1(name, age, season, i) == 2:
        skill += 0
        know += 2
        friend += 0
      elif basketBallStoryLine1(name, age, season, i) == 3:
        skill += 2
        know += 1
        friend += 3
      else:
        skill += 0
        know += 0
        friend += 0
    i += 1
    if sum(choices) == 16:
      print("You have given up on your dream of becoming a pro Basketball player.")
      giveUp = True
    else:
      print(f"It's been a whole year and you refuse to give up on your dream of becoming a pro Basketball player.")
      age += 1
      choices.clear
      i = 0