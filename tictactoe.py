#Kelia Morrah
print("*+*+*+* WELCOME TO TIC-TAC-TOE!*+*+*+* \n")
print("In this game, X goes first and O will go second. You can choose which one you want to be among yourselves. \n")
print("The rules are simple: \n")
print("1) You each make a move one after the other! No double turns!\n")
print("2) You cannot pick the same place twice. \n")
print("3) The winner is declared by getting 3 in a row or column \n")
print("4) The spaces are filled by using the corresponding numbers on the board.See below as reference: \n")

print("7  | 8 | 9 ")
print("-----------")
print("4  | 5 | 6 ")
print("-----------")
print("1  | 2 | 3 \n")
print("Let us begin!\n")

Boardlayout = {'7': ' ' , '8': ' ' , '9': ' ' ,
              '4': ' ' , '5': ' ' , '6': ' ' ,
              '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in Boardlayout:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(Boardlayout)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if Boardlayout[move] == ' ':
            Boardlayout[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if Boardlayout['7'] == Boardlayout['8'] == Boardlayout['9'] != ' ': # across the top
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif Boardlayout['4'] == Boardlayout['5'] == Boardlayout['6'] != ' ': # across the middle
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Boardlayout['1'] == Boardlayout['2'] == Boardlayout['3'] != ' ': # across the bottom
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Boardlayout['1'] == Boardlayout['4'] == Boardlayout['7'] != ' ': # down the left side
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Boardlayout['2'] == Boardlayout['5'] == Boardlayout['8'] != ' ': # down the middle
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Boardlayout['3'] == Boardlayout['6'] == Boardlayout['9'] != ' ': # down the right side
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif Boardlayout['7'] == Boardlayout['5'] == Boardlayout['3'] != ' ': # diagonal
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Boardlayout['1'] == Boardlayout['5'] == Boardlayout['9'] != ' ': # diagonal
                printBoard(Boardlayout)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            Boardlayout[key] = " "

        game()

if __name__ == "__main__":
    game()