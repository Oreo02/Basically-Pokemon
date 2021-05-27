#function for fighting 
  #announce who fights who, do description
  #ask user for input 
    #ask what pokemon to send first
  #ask the move they want to use
  #resolution order: priority, speed, etc
    #idea: alternate these questions and prompt players 1 and 2 for what they want
  #resolve damage, run damage calc formula, compare attks and defs, check moods, stats, and status affects
  #check if combatant has fainted then move on to next round
  #also check if the battle is over - all of one teams pkmn have fainted
  #announce which team won

import random
from nomi import *
from DaFish import DaFish
from Gibson import Gibson
from Dog import Dog

playerHP = 0
enemy = 0

def attackAction(myNomi, enemyNomi, enemyMove):
  prompt = True
  while prompt:
    print("Available moves: \n")
    i = 1
    for move in myNomi.moveSet:
     print("{}: {}".format(i, myNomi.moveSet[i]))
     i += 1
    action = input("Choose a move number:")

    if action == 1:
      myMove = myNomi.moveSet[0]
      prompt = False
    elif action == 2:
      myMove = nomi.moveSet[1]
      prompt = False
    elif action == 3:
      myMove == nomi.moveSet[2]
      prompt = False
    elif  action == 4:
      myMove.nomi.moveSet[3]
      prompt = False
    else:
      print("Invalid input")

  #calculating who goes first
  if myMove.priority > enemyPriority:
    enemyNomi.calculateDamage(myMove, myNomi.attack)
    if enemyNomi.hp != 0:
      myNomi.calculateDamage(enemyMove, enemyNomi.attack)


  elif myMove.priority < enemyPriority:
    myNomi.calculateDamage(enemyMove, enemyNomi.attack)
    if myNomi.hp != 0:
      enemyNomi.calculateDamage(myMove, myNomi.attack)


  elif myMove.priority == enemyMove.priority:
    if myNomi.att_speed > enemyNomi.att_speed:
      enemyNomi.calculateDamage(myMove, myNomi.attack)
      if enemyNomi.hp != 0:
        myNomi.calculateDamage(enemyMove, enemyNomi.attack)


    elif  myNomi.att_speeed < enemyNomi.att_speed:
      myNomi.calculateDamage(enemyMove, enemyNomi.attack)
      if myNomi.hp != 0:
        enemyNomi.calculateDamage(myMove, myNomi.attack)

    #if both priority and speed are same (yo what) do a coin toss

    elif myNomi.att_speed == enemyNomi.att_speed:
      toss = random.randint(1,2)


      if toss == 1:
        enemyNomi.calculateDamage(myMove, myNomi.attack)
        if myNomi.hp != 0:
          enemyNomi.calculateDamage(myMove, myNomi.attack)


      else:
        myNomi.calculateDamage(enemyMove, enemyNomi.attack)
        if myNomi.hp != 0:
          enemyNomi.calculateDamage(myMove, myNomi.attack)
  print(" { } has { } HP left".format(myNomi.name, myNomi.hp))
  print("The enemy has { } HP left".format(enemyNomi.hp))

  moodChance = random.randint(1, 10):
  if moodchance == 1:
    myNomi.mood == "Angry"
  elif moodChance == 2 or moodChance == 3:
    myNomi.mood == "Afraid"
  elif moodChance == 4 or moodChance == 3:
    myNomi.mood == "Hyper"
  elif moodChance == 6 or moodChance = 7:
    myNomi.mood == "Cautious"
  elif moodChance == 8 or moodChance = 9 or moodChance == 10:
    myNomi.mood == "Neutral"


  if myNomi.hp ==0:
    print("Your { } has been defeated!".format(myNomi.name))
    return False
  if enemyNomi.hp == 0:
    print("You have defeated your enemy!")
    return False
  print("-------Next Round-------")
  return True
      
def main():
  global playerHP, enemyHP
  play = True
  while play:
    team = [DaFish("LeFishe"), Gibson("Gibson"), Dog("Cat")]
    enemy = DaFish("CEO of FishCarp Inc")
    prompt = True
    while prompt = int(input("Choose Nomi: [1) DaFish, 2) Gibson, 3) Dog]"))
    if response == 1:
      chooseNomi = team[0]
      prompt = False
    elif response == 2:
      chooseNomi = team[1]
      prompt = False
    elif response == 3:
      chooseNomi = team[2]
      prompt = False
    else:
      print("Invalid Input! Enter a number 1-3.")

  fight = True
  while fight:
    moveNum = rndom randint(0, 3)
    fight = attackAction(chosenNomi, enemy, enemy.moveSet[moveNum])

  prompt = True
  while prompt:
    response = Input ("Fight another battle? (y/n)")
    if response.lower == "y":
      play = True
    elif response.lower =="n":
      play = False
    else:
      print("Please enter a valid input. (y/n)")
  print("----------------------------------")

if __name__ == "__main__":
  main()
