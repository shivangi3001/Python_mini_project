#random number guessing game in python

import random

print("\t\t--------Welcome to the Number Guessing Game------\n")
print("Initial score = 0 \nWrong guess -1 \nCorrect guess +50pints\n")
n = int(input("Enter the upper value of the number: "))

number = random.randrange(1,n)

print("\nGuess a number between 1 to ", n)
guess = int(input())

score = 0

while guess != number :
    score= score-1
    if guess < number:
        print("your score is: ", score)
        print("Oops! Guess a higher number:  Try again! ")
        
        #print("\nGuess a number between 1 to ", n)
        guess = int(input("guess: "))
    else:
        print("your score is: ", score)
        print("oops! Guess a lower number: Try again! ")
        
        #print("\nGuess a number between 1 to ", n)
        guess = int(input("Guess: "))

print("Congratulation you guessed correct number")
score=score+50
print("your final score is: ", score)
