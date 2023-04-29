#rock paper scissors_kartk
import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    print("Choose an option:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    player_choice = int(input()) - 1
    
    if player_choice not in [0, 1, 2]:
        print("Invalid choice, please try again.")
        continue
    
    computer_choice = random.randint(0, 2)
    
    print(f"You chose {options[player_choice]}")
    print(f"The computer chose {options[computer_choice]}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
        player_score += 1
    elif player_choice == 1 and computer_choice == 0:
        print("You win!")
        player_score += 1
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
        
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "n":
        break
    
print(f"Final score: Player {player_score}, Computer {computer_score}")
