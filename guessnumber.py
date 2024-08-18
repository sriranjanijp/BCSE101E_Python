#You will write a program that randomly generates an integer between 0 and 100, inclusive. 
#The program prompts the user to enter numbers continuously until it matches the randomly generated number. 
#For each user input, the program reports whether it is too low or too high, so the user can choose the next input intelligently.

import random
num = random.randint(1,100)
print("Welcome to the guessing game. Enter a number between 0 and 100")
guess = int(input())
while guess != num:
    if guess>num:
        print("Your guess is too high! Try again")
        guess = int(input())
    elif guess<num:
        print("Your guess is too low!. Try again")
        guess = int(input())
print("You're right!", num," is the right number!")
