from random import *

names=['Dirty Joe', 'Big Jack', 'Miserable Dave']
playerTurn = True
alive=True
opponent = ""

def shoot():
    return(randint(0, 1))

def play():
    global playerTurn
    global names
    global opponent
    global alive
    opponent=str(names[randint(0,len(names)-1)])
    print('Welcome to a good ol\' game of russian roulette!\n\nYou and {0} are up!\n'.format(opponent))
    for x in range(0, 7):
        if alive:
            h=shoot()
            if playerTurn:
                print("You: {0};".format(h))
            else:
                print("{0}: {1};".format(opponent, h))
            if h==1 and playerTurn:
                print("BANG! You Lose")
                alive=False
            if h==1 and not playerTurn:
                print("BANG! {0} Loses!".format(opponent))
                alive=False
            playerTurn ^= True
play()
