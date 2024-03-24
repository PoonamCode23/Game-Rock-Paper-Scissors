import random

options = ("rock", "paper", "scissors")
playing = True
player_score = 0
computer_score = 0

while playing:

    print("\nPlayer Score:", player_score, "Computer Score:", computer_score)

    player = input("Enter a choice (rock, paper, scissors) or 'q' to quit: ").lower()

    if player == 'q':
        break 

    if player not in options:
        print("Invalid choice. Please enter either 'rock', 'paper', 'scissors', or 'q' to quit.")
        continue  

    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win 🥳!")
    elif player == "paper" and computer == "rock":
        print("You win 🥳!")
    elif player == "scissors" and computer == "paper":
        print("You win 🥳!")
        player_score += 1
    else:
        print("You lose 😥!")
        computer_score += 1
        
print("\nFinal Scores= Player:", player_score, "Computer:", computer_score)
print("Thank you for playing!")


