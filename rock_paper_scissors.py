import random

computer_wins = 0
player_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Would you like to choose 'Rock', 'Paper', or 'Scissors', or 'q' to quit ".lower())
    if user_input == "q":
        break
    elif user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        player_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won")
        player_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        player_wins += 1
    else:
        print("You lost")
        computer_wins += 1

if player_wins > computer_wins:
    print("You won wiht", player_wins, "wins")

