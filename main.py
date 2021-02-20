# Import Game modules
import pychallenge
import tictactoe
import typing

#Main Menu

print ("""Hello, welcome to our arcade! Which of the following games would you like to play?

    1. Python Challenge
    2. Text Adventure
    3. Guess my Color
    4. Tic Tac Toe
    5.Exit/Quit

    """)

ans=int(input("What would you like to do? ")) 
if ans==1: 
  print("\n Python Quiz it is!")
  pychallenge.py_challenge()
  
elif ans==2:
  print("\n Text Adventure it is!") 
  typing.tyingClub()
  
elif ans==3:
  print("\nGuess my Color it is!") 
  from random import randint
      
  colors = ['red', 'blue', 'yellow', 'purple', 'green', 'orange']
  generator = randint(0,len(colors)-1)
      
  guess = input("Please guess a color from the color wheel: ")
      
  while True: #you want to keep guessing until you actually get it
    if guess != colors[generator]:
      print("Incorrect. Please try again.")
      guess = input("Please guess a color: ").strip()
    elif guess == colors[generator]:
      break
      
  print("Correct!  The color is " + colors[generator] + ".")

elif ans==4:
  tictactoe.game()

elif ans==5:
  print("\n Goodbye!") 
elif ans !="":
  print("\n Not Valid Choice Try again") 