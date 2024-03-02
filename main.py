#cyber space imports
from cyberspace import cyberSpace
import cyberspace
#prison break imports
#Door
from prisonBreak import prisonBreakMainStoyLine, prisonBreakFirstChoiceDoor, prisonBreakAfterDoorChoiceSteal,
prisonBreakLeftHallway,
prisionBreakRightHallway,
prisionBreakBoat,
prisionBreakHelicoptor,
prisonBreakElevator,
prisonBreakAfterDoorChoiceAsk
#window
from prisonBreak import prisonFirstChoiceWindow,
prisonBreakSecondChoiceClimb,
prisionBreakThirdChoiceIsland,
prisonBreakThirdChoiceCity
import prisonBreak


prisonBreakMainStoyLine() #imported
dOW = input("Do you want to go through the door or the window?(door/window): ")
if dOW == "door":
  prisonBreakFirstChoiceDoor() #imported
  oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
  if oOT == "steal":
prisonBreakAfterDoorChoiceSteal() #imported
    if prisonBreakAfterDoorChoiceSteal() == True: #imported
      lOR = input("Do you go left or right?(left/right): ")
      if lOR == "left":
        prisonBreakLeftHallway() #imported
      elif lOR == "right":
        prisionBreakRightHallway() #imported
        sOE = input("Do you take the stairs or the elevator (stairs/elevator): ")
        if sOE == "stairs":
          bOH = input("At the bottem of the stairs you see a boat and a helicoptor. Which one do you take?(boat/helicop")
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
        prisonBreakSide()
  elif cOD == "door":
    prisonBreakFirstChoiceDoor()
    oOT = input("Do you want to try to steal the gaurd's keys or ask where you are?(steal/ask): ")
    if oOT == "steal":
      prisonBreakAfterDoorChoiceSteal()
    elif oOT == "ask":
      prisonBreakAfterDoorChoiceAsk()
      
