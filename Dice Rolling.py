#dice rolling_kartk
import random


num_dice = 2
num_sides = 6


def roll_dice():
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
        print("Die", i+1, "rolled :", roll)
    print("Total score:", total)
    return total


def play_game():
    score = roll_dice()
    pile = []
    
    while True:
        choice = input("Do you want to keep this score? (y/n): ")
        if choice.lower() == 'y':
            pile.append(score)
            print("Score added to pile!")
            break
        elif choice.lower() == 'n':
            print("Rolling again...")
            score = roll_dice()
        else:
            print("Invalid choice, please enter 'y' or 'n'")
            
    print("Pile:", pile)
    print("Game over!")
    
    
play_game()
