#cyber space imports
from cyberspace import cyberSpace
import cyberspace
#prison break imports
#Door
from prisonBreak import prisonBreakMainStoyLine
from prisonBreak import prisonBreakFirstChoiceDoor
from prisonBreak import prisonBreakAfterDoorChoiceSteal
from prisonBreak import prisonBreakLeftHallway
from prisonBreak import prisionBreakRightHallway
from prisonBreak import prisionBreakBoat
from prisonBreak import prisionBreakHelicoptor
from prisonBreak import prisonBreakElevator
from prisonBreak import prisonBreakAfterDoorChoiceAsk
#window
from prisonBreak import prisonFirstChoiceWindow
from prisonBreak import prisonBreakSecondChoiceClimb
from prisonBreak import prisionBreakThirdChoiceIsland
from prisonBreak import prisonBreakThirdChoiceCity
from prisonBreak import prisionBreakRunAway
from prisonBreak import prisonBreakFrezze
from prisonBreak import prisionBreakMiddle
from prisonBreak import prisionBreakSide

import prisonBreak

#atlantis imports
from Atlantis import mainStoryLine
from Atlantis import cave1
from Atlantis import cave2
from Atlantis import shark
from Atlantis import eels
from Atlantis import treasure
from Atlantis import run
#Sports imports
from extremSports import mainStoryLineSports

'''
game = input('What game do you want to play? (Prison Break of Atlantis): ')

if game == "Prison Break":
  
  #prison break
  prisonBreakMainStoyLine() #imported
  dOW = input("Do you want to go through the door or the   window?(door/window): ")
  if dOW == "door":
    prisonBreakFirstChoiceDoor() #imported
    oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
    if oOT == "steal":
      if prisonBreakAfterDoorChoiceSteal() == 2: #imported
        lOR = input("Do you go left or right?(left/right): ")
        if lOR == "left":
          prisonBreakLeftHallway() #imported
          wOO = input("Do you go ou the window or try and find another way out?(window/find): ")
          if wOO == "window":
            prisonBreakSecondChoiceClimb()
            iOC = input("Do swim back to the island or ty and swim to the city on the horizon?(island/city): ")
            if iOC == "island":
              prisionBreakThirdChoiceIsland()
              rOF = input("Do you want to run away from the spotlight or stay where you are. (run/frezze): ")
              if rOF == "run":
                prisionBreakRunAway()

prisonBreakMainStoyLine() #imported
dOW = input("Do you want to go through the door or the window?(door/window): ")
if dOW == "door":
  prisonBreakFirstChoiceDoor() #imported
  oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
  if oOT == "steal":
    #prisonBreakAfterDoorChoiceSteal() #imported
    if prisonBreakAfterDoorChoiceSteal() == 2: #imported
      lOR = input("Do you go left or right?(left/right): ")
      if lOR == "left":
        prisonBreakLeftHallway() #imported
        wOO = input("Do you go ou the window or try and find another way out?(window/find): ")
        if wOO == "window":
          prisonBreakSecondChoiceClimb()
        elif wOO == "find":
          print("You can't find another way out so you use the window.")
          prisonBreakSecondChoiceClimb()
          iOC = input("Do swim back to the island or ty and swim to the city on the horizon?(island/city): ")
            if iOC == "island":
              prisionBreakThirdChoiceIsland()
              rOF == input("Do you want to run away from the spotlight or stay where you are. (run/frezze): ")
              if rOF == "run":
                prisonBreakRunAway()
            elif iOC == "city":
              prisonBreakThirdChoiceCity()
              eOM = input("Do you want to enter the city in the middle of the shore or on the side of the shore. (middle/side): ")
              if eOM == "middle":
                prisionBreakMiddle()
              elif eOM == "side":
                prisionBreakSide()
          elif wOO == "find":
            print("You can't find another way out so you use the window.")
            prisonBreakSecondChoiceClimb()
            iOC = input("Do swim back to the island or ty and swim to the city on the horizon?(island/city): ")
            if iOC == "island":
              prisionBreakThirdChoiceIsland()
              rOF = input("Do you want to run away from the spotlight or stay where you are. (run/frezze): ")
              if rOF == "run":
                prisionBreakRunAway()
              elif iOC == "city":
                prisonBreakThirdChoiceCity()
                eOM = input("Do you want to enter the city in the middle of the shore or on the side of the shore. (middle/side): ")
                if eOM == "middle":
                  prisionBreakMiddle()
                elif eOM == "side":
                  prisionBreakSide()
        elif lOR == "right":
                prisonBreakSide()
          elif cOD == "door":
            prisonBreakFirstChoiceDoor()
            oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
            if oOT == "steal":
              prisonBreakAfterDoorChoiceSteal()
            elif oOT == "ask":
              prisonBreakAfterDoorChoiceAsk()
      elif lOR == "right":
        prisionBreakRightHallway() #imported
        sOE = input("Do you take the stairs or the elevator (stairs/elevator): ")
        if sOE == "stairs":
          bOH = input("At the bottem of the stairs you see a boat and a helicoptor. Which one do you take?(boat/helicoptor): ")
          if bOH == "boat":
            prisionBreakBoat() #imported
          elif bOH == "helicoptor":
            prisionBreakHelicoptor() #imported
        elif sOE == "elevator":
          prisonBreakElevator() #imported
      elif oOT == "ask":
        prisonBreakAfterDoorChoiceAsk() #imported
        prisonFirstChoiceWindow() #imported
        cOD = input("Do you want to climb out the window or go try the door?(climb/door): ")
        if cOD == "climb":
          prisonBreakSecondChoiceClimb() #imported
          iOC = input("Do swim back to the island or ty and swim to the city on the horizon?(island/city): ")
          if iOC == "island":
            prisionBreakThirdChoiceIsland() #imported
          elif iOC == "city":
            prisonBreakThirdChoiceCity()
        elif cOD == "door":
          prisonBreakFirstChoiceDoor()
          oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
          if oOT == "steal":
            prisonBreakAfterDoorChoiceSteal()
          elif oOT == "ask":
            prisonBreakAfterDoorChoiceAsk()
  elif dOW == "window":
    prisonFirstChoiceWindow()
    cOD = input("Do you want to climb out the window or go try the door?(climb/door): ")
    if cOD == "climb":
      prisonBreakSecondChoiceClimb()
      prisonBreakSecondChoiceClimb() #imported
      iOC = input("Do swim back to the island or ty and swim to the city on the horizon?(island/city): ")
      if iOC == "island":
        prisionBreakThirdChoiceIsland()
        rOF = input("Do you want to run away from the spotlight or stay where you are. (run/frezze): ")
        if rOF == "run":
          prisionBreakRunAway()
      elif iOC == "city":
        prisonBreakThirdChoiceCity()
        eOM = input("Do you want to enter the city in the middle of the shore or on the side of the shore. (middle/side): ")
        if eOM == "middle":
          prisionBreakMiddle()
        elif eOM == "side":
          prisionBreakSide()
    elif cOD == "door":
      prisonBreakFirstChoiceDoor()
      oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
      if oOT == "steal":
        prisonBreakAfterDoorChoiceSteal()
        if prisonBreakAfterDoorChoiceSteal() == 2: #imported
          lOR = input("Do you go left or right?(left/right): ")
          if lOR == "left":
            prisonBreakLeftHallway() #imported
            wOO = input("Do you go ou the window or try and find another way out?(window/find): ")
            if wOO == "window":
              prisonBreakSecondChoiceClimb()
              iOC = input("Do swim back to the island or ty and swim to the city on the horizon?(island/city): ")
              if iOC == "island":
                prisionBreakThirdChoiceIsland()
                rOF = input("Do you want to run away from the spotlight or stay where you are. (run/frezze): ")
                if rOF == "run":
                  prisionBreakRunAway()
              elif iOC == "city":
                prisonBreakThirdChoiceCity()
                eOM = input("Do you want to enter the city in the middle of the shore or on the side of the shore. (middle/side): ")
                if eOM == "middle":
                  prisionBreakMiddle()
                elif eOM == "side":
                  prisionBreakSide()
      elif oOT == "ask":
        prisonBreakAfterDoorChoiceAsk()
        prisonBreakAfterDoorChoiceAsk() #imported
        prisonFirstChoiceWindow() #imported
        cOD = input("Do you want to climb out the window or go try the door?(climb/door): ")
        if cOD == "climb":
          prisonBreakSecondChoiceClimb() #imported
          iOC = input("Do swim back to the island or ty and swim to the city on the horizon?(island/city): ")
          if iOC == "island":
            prisionBreakThirdChoiceIsland() #imported
          elif iOC == "city":
            prisonBreakThirdChoiceCity()
        elif cOD == "door":
          prisonBreakFirstChoiceDoor()
          oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
          if oOT == "steal":
            prisonBreakAfterDoorChoiceSteal()
          elif oOT == "ask":


#Atlantis
elif game == "Atlantis":
  mainStoryLine() #imported
  oNT = input("Do you want to go through the cave on the left or the right?(left/right): ")
  if oNT == "left":
    cave1()
    oNT = input("Do you want to go through the cave on the left or the right?(left/right): ")
    if oNT == "left":
      cave1()
      shark()
    elif oNT == "right":
      cave2()
      eOS = input("There is an eel in one cave and a shark in the other. Do you want to swim to the eel or the shark?(eel/shark):")
      if eOS == "eel":
        eels()
        if eels() == 1:
          oNT = input("Do you want to go through the cave on the left or the right?(left/right): ")
          treasure()
      elif eOS == "shark":
        shark()
  elif oNT == "right":
    cave2()
    oNT = input("Do you want to go through the cave on the left or the right?(left/right): ")
    if oNT == "left":
      cave1()
      oNT = input("Do you want to go through the cave on the left or the right?(left/right): ")
      if oNT == "left":
        cave1()
        if eels() == 2:
          oNT = input("Do you want to go through the cave on the left or the right?(left/right): ")
          treasure()
    elif oNT == "right":
      cave2()
      eels()
    elif oNT == "right":
      cave2()
    if oNT == "left":
      cave1()
      shark()
    elif oNT == "right":
      cave2()
      shark()
'''
