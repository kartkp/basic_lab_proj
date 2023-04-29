#guess the no._kartk
import random


num = random.randint(1, 100)


num_guesses = 0
while True:
    
    guess = int(input("Guess the number between 1 and 100: "))
    
    
    num_guesses = 1 + num_guesses
    
   
    if guess == num:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.""And your score will becomes", num_guesses)
        break
    elif guess < num:
        print("The number is higher than your guess. Try again bro..")
    else:
        print("The number is lower than your guess. Try again bro..")
