#dice rolling with names_kartk
import random

num_dice = 2
num_sides = 6


num_players = int(input("Enter the number of players: "))
player_names = []
for i in range(num_players):
    name = input("Enter player " + str(i+1) + "'s name: ")
    player_names.append(name)


def roll_dice():
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
        print("Die", i+1, "rolled:", roll)
    print("Total score:", total)
    return total

def play_game():
    player_scores = [0] * num_players
    
    while True:
        for i in range(num_players):
            print("Player", player_names[i] + "'s turn:")
            score = roll_dice()
            choice = input("Do you want to keep this score? (y/n): ")
            if choice.lower() == 'y':
                player_scores[i] += score
                print("Score added to", player_names[i] + "'s total score!")
            elif choice.lower() == 'n':
                print("Rolling again...")
                continue
            else:
                print("Invalid choice, please enter 'y' or 'n'")
        
        print("Current scores:")
        for i in range(num_players):
            print(player_names[i] + ": " + str(player_scores[i]))
        
        max_score = max(player_scores)
        if max_score >= 100:
            winner_index = player_scores.index(max_score)
            print("Congratulations, " + player_names[winner_index] + " wins!")
            break
        
    print("Game over!")
    

play_game()
