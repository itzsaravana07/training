# rock paper scissor game
from random import choice
choices = ["scissor", "rock", "paper"]
computer_choice = choice(choices)
player_choice = input("Enter your choice (scissor, rock, paper): ").lower()
if player_choice not in choices:
    print("Invalid choice! Please choose scissor, rock, or paper.")
else:
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "scissor" and computer_choice == "paper")or (player_choice == "rock" and computer_choice == "scissor") or(player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins .Better luck next time!")
print("Thanks for playing!")