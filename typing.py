# Linxin Jiang
#A list: only add item here 
list1 = ["fjfj","dkdk","fjdk,fjdk","slsl","ghgh","ruru","eiei","ptpt","vmvm","bnbn"]

# checkd if user got right
def typing(li,score):
    print()
    letter = input("Enter the letter ' "+ li +" ': ")
    print("Your entered " + "'" +li + "'")
    if(letter == li):
        score = score + 1
        print("Good! \nYour score is " + str(score) )
    else:
        score = score - 1
        print("The letter was '"+ li +"' Score -1\nYour score is " + str(score) )
    return score

def li(score):
    for i in list1:
        roundscore = typing(i,score)
        score = roundscore


# Main bar
def tyingClub():
    score = 0
    print("Welcome to text adventure!")
    print("Put your hands on correct position...")
    print("Let start!\n")
    
    
    li(score)

#Start the game 
tyingClub()