import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "tie"
    
    winning_combos = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combos[player] == computer:
        return "player"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    player_score = 0
    computer_score = 0
    rounds = 5
    
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        player_choice = input("Choose rock, paper, or scissors: ").lower().strip()
        
        while player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            player_choice = input("Choose rock, paper, or scissors: ").lower().strip()
        
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"Score - You: {player_score} | Computer: {computer_score}")
    
    print("\n--- Final Results ---")
    if player_score > computer_score:
        print(f"You win the game {player_score}-{computer_score}!")
    elif computer_score > player_score:
        print(f"Computer wins the game {computer_score}-{player_score}!")
    else:
        print("The game ends in a tie!")

if __name__ == "__main__":
    play_game()
  "Initial commit"
