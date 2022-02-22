import random
from pyfiglet import Figlet
custom_fig = Figlet(font='smkeyboard')
title = Figlet(font='digital')
print(title.renderText('Roshambo'))
print("Press 🠓 ")
print(custom_fig.renderText('N') + ("--------- Start ---------"))

Score = 0
Intro = True
N = input("| ")

while Intro == True:
 if N != "N":
   print("Oops! Something went wrong...")
   break;
 Game = random.choice(['Rock', 'Paper' , 'Scissors'])
 print("-")
 User = input(": ")
 if User == "Rock" and Game == "Rock":
   print("Tie!")
   Score=Score+1
 elif User == "Rock" and Game == "Paper":
   print("You Lose!")
   Score=Score+1
 elif User == "Rock" and Game == "Scissors":
   print("You Win!")
   Score=Score+1
 elif User == "Paper" and Game == "Paper":
   print("Tie!")
   Score=Score+1
 elif User == "Paper" and Game == "Rock":
   print("You Win!")
   Score=Score+1
 elif User == "Paper" and Game == "Scissors":
   print("You Lose!")
   Score=Score+1
 elif User == "Scissors" and Game == "Rock":
   print("You Lose!")
   Score=Score+1
 elif User == "Scissors" and Game == "Paper":
   print("You Win!")
   Score=Score+1
 elif User == "Scissors" and Game == "Scissors":
   print("Tie!")
   Score=Score+1
 if Score == 3:
  print("____________")
  Yes = input("Play Again?: ")
  if Yes == "Y":
    Intro = True
    Score = 0
  else:
    break;






  

  
 
   

