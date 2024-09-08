'''
(Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws.

Revise the program to let the user play continuously
until either the user or the computer wins more than two times.
'''

import random
user = 0
computer = 0
while (user<3 and computer<3):
    compchoice = random.randint(0,2)
    userchoice = random.randint(0,2)
    print("scissor(0), paper(1), rock(2): ",userchoice)
    if compchoice == 0:
        if userchoice == 1:
            print("The computer is scissor. You are rock. You win")
            user +=1
        elif userchoice == 2:
            print("The computer is scissor. You are paper. The computer wins")
            computer +=1
        else:
            print("The computer is scissor. You are scissor. It is a draw")
    elif compchoice == 1:
        if userchoice == 1:
            print("The computer is rock. You are rock. It is a draw")
        elif userchoice == 2:
            print("The computer is rock. You are paper. You win")
            user +=1
        else:
            print("The computer is rock. You are scissor. The computer wins")
            computer +=1
    else:
        if userchoice == 1:
            print("The computer is paper. You are rock. The computer wins")
            computer +=1
        elif userchoice == 2:
            print("The computer is paper. You are paper. It is a draw")
        else:
            print("The computer is paper. You are scissor. You win")
            user +=1