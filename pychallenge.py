def py_challenge():

  print("Welcome to Python Challenge!\n" )
  print("We will start with 100 points. Answer a few Python questions.\nMinus 10 for every wrong answer, and 0 points deducted if you\nare correct. Game over if you only have 20 points left.\n")

  start= int(input("Ready? Enter 1 for yes and 0 for no: "))
  points= 100

  if start==1:
    print("\nWho named the language python?\n 1. Guido van Rossum\n 2. Monty Python\n")
    start= int(input("1 or 2: "))
    if start==2:
      points -=10
      print("Oh no, bad choice! Current points: " + str(points) +"\n")
    else:
      print("Correct! On to next question!\n")

    print("In python, we need to specify variable type when declaring it. \n 1. True \n 2. False\n")
    start= int(input("1 or 2: "))
    if start==1:
      points -=10
      print("Oh no, bad choice! Current points: " + str(points) +"\n" )
    else:
      print("Correct! On to next question!\n")

    print(" Socks= ('Dino', 'Panda', 'Kitty', 'Ducky' is an exampe of?1 \n 1. String list \n 2. Tuple\n")
    start= int(input("1 or 2: "))
    if start==1:
      points -=10
      print("Oh no, bad choice! Current points: " + str(points) + "\nThis is a tuple, a datatype in python used for storing multiple values in one variable." +"\n")
    else:
      print("Correct! On to next question!\n")
    
    print("\nBinary and set are built in data types for python. \n 1. True\n 2. False\n")
    start= int(input("1 or 2: "))
    if start==2:
      points -=10
      print("Oh no, bad choice! Current points: " + str(points) +"\n")
    else:
      print("Correct! On to next question!\n")

    print("\nWhat is (((2**1)**3)**2)? \n 1. 64\n 2. 8\n")
    start= int(input("1 or 2: "))
    if start==2:
      points -=10
      print("Oh no, bad choice! Current points: " + str(points) +"\n")
    else:
      print("Correct! On to next question!\n")

    print("\nx = lambda a : a + 10 \nprint(x(400))\nWhat does this code print?\n 1 lambda 410. \n 2. 410\n")
    start= int(input("1 or 2: "))
    if start==1:
      points -=10
      print("Oh no, bad choice! Current points: " + str(points) +"\n")
    else:
      print("Correct! On to next question!\n")
  else:
    print("Aww, oky! Maybe next time.")

py_challenge()