name = input("What is your name? ")
age = 6
season = ["spring","summer","fall", "winter"]
i = 0

def mainStoryLineSports():
  print("Welcome to Athletes")
  print("Pick your sport:")
  print("1 = Basketball\n2 = Soccer\n3 = Football\n4 = Baseball\n5 = Hockey\n6 = Golf\n7 = Tennis\n8 = Swimming\n9 = Track and Field\n10 = Volleyball\n11 = Rugby\n12 =  Gymnastics\n13 = Boxing")
  sport = int(input("Enter the number that corispnds to your sport.: "))
  return sport
def basketBallStoryLine(user, age, season,i=0):
  print(f"Hello {user}! You are {age} years old and you have a dream. You want to be a professional basketball player.")
  print(f"What wil you spend the{season[i]} doing?")
  print("1 = Play basketball\n2 = Watch basketball\n3 = Play basketball with friends\n4 = Nothing")
  choice = int(input("Enter the number that corispnds to your choice.: "))
mainStoryLineSports()