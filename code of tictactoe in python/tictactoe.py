#Hello there!!!....myself Rakesh pandey
#Student at NIT jalndhar(First year -CSE branch)
#And this is minor project!!!!
#Building a TicTacToe game!!!

import os
from time import sleep

#define board
board=[" "," "," "," "," "," "," "," "," "]
def printboard():
    print(" ---- " * 3)
    print("|", board[0], " ", "|", board[1], " ", "|", board[2], " ", "|")
    print(" ---- " * 3)

    print("|", board[3], " ", "|", board[4], " ", "|", board[5], " ", "|")
    print(" ---- " * 3)

    print("|", board[6], " ", "|", board[7], " ", "|", board[8], " ", "|")

    print(" ---- " * 3)
flag ="X"
count=0

while True:
  if flag=="X":
    os.system('cls')
    print("Tic-Tac-Toe game!!!!!")
    print("Made by RAKESH PANDEY")
    printboard()
    #Taking input from user for values of X
    try:
      choice = (int(input("enter the position to fill X \n"))-1)
    except ValueError:
        print("enter only integer values between 1-9")
        sleep(1)
        flag = "1"
    try:
       if flag=="1" :
          flag="X"
       elif board[choice]==" ":
          board[choice]="X"
          flag = "0"
          count = count+1

       else :
          print("position already occupied choose another")
          sleep(1)
          flag="X"
    except IndexError:
         print("pagal hai kya.....9 hi spaces hai....enter between 1-9")
         sleep(1)
         flag ='X'

    #Checking condition if X wins
    xwin = (board[0] == board[1] == board[2] == "X") \
         or (board[3] == board[4] == board[5] == "X") \
         or (board[6] == board[7] == board[8] == "X") \
         or (board[0] == board[3] == board[6] == "X") \
         or (board[1] == board[4] == board[7] == "X") \
         or (board[2] == board[5] == board[8] == "X") \
         or (board[0] == board[4] == board[8] == "X") \
         or (board[2] == board[4] == board[6] == "X")

    #IF x wins asking for playagain or exit !!!
    if (xwin):
      os.system('cls')
      print("Tic-Tac-Toe game!!!!!")
      print("Made by RAKESH PANDEY")
      printboard()
      print("X won....well played...although little advantage of being first turn !!!")
      sleep(3)
      play = input("wanna play again??..(yes/no)")
      if (play == "yes"):
          board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
          flag = "X"
          count = 0
      elif (play == "no"):
          print("Thanks for playing")
          sleep(2)
          break
      else:
          print("cant type properly.....u idiot!!!....play nextime!!! byee!!")
          sleep(2)
          break
  #Checking condition for Draw !!!!
  if (count == 9):
      os.system('cls')
      print("Tic-Tac-Toe game!!!!!")
      print("Made by RAKESH PANDEY")
      printboard()
      print("Match drawn....Both were Fantastic")
      sleep(2)
      play=input("wanna play again??..(yes/no)")
      if(play=="yes"):
          board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
          flag="X"
          count=0
      elif (play == "no"):
          print("Thanks for playing")
          sleep(2)
          break
      else:
          print("cant type properly.....u idiot!!!....play nextime!!! byee!!")
          sleep(2)
          break

  if flag=="0":
    os.system('cls')

    print("Tic-Tac-Toe game!!!!!")
    print("Made by RAKESH PANDEY")
    printboard()
    #Taking input for 0 user !!!
    try:
      choice = (int(input("enter the position to fill 0 \n"))-1)
    except ValueError:
        print("enter only integer values between 1-9")
        sleep(1)
        flag = "1"

    try:
      if flag=="1" :
         flag="0"
      elif board[choice]==" ":
         board[choice]="0"
         flag = "X"
         count=count+1

      else :
         print("position already occupied choose another")
         sleep(1)
         flag="0"
    except IndexError:
        print("pagal hai kya.....9 hi spaces hai....enter between 1-9")
        sleep(1)
        flag = '0'
    #Checking condition if 0 wins
    owin = (board[0] == board[1] == board[2] == "0") \
         or (board[3] == board[4] == board[5] == "0") \
         or (board[6] == board[7] == board[8] == "0") \
         or (board[0] == board[3] == board[6] == "0") \
         or (board[1] == board[4] == board[7] == "0") \
         or (board[2] == board[5] == board[8] == "0") \
         or (board[0] == board[4] == board[8] == "0") \
         or (board[2] == board[4] == board[6] == "0")

    # IF x wins asking for playagain or exit !!!
    if (owin):
        os.system('cls')
        print("Tic-Tac-Toe game!!!!!")
        print("Made by RAKESH PANDEY")
        printboard()
        print("0 won....well played 0 are not always loser")
        sleep(3)
        play = input("wanna play again??..(yes/no)")
        if (play == "yes"):
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            flag = "X"
            count = 0
        elif(play=="no"):
            print("Thanks for playing")
            sleep(2)
            break
        else:
            print("cant type properly.....u idiot!!!....play nextime!!! byee!!")
            sleep(2)
            break






