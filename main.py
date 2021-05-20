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
import nomi import *

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
    elif action == 2:
      myMove = nomi.moveSet[1]
    elif action == 3:
      myMove == nomi.moveSet[2]
    elif  action == 4:
      myMove.nomi.moveSet[3]
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
      else:
        myNomi.calculateDamage(enemyMove, enemyNomi.attack)
    


