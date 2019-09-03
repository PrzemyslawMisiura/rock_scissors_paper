# Prosta gra rock, scissors, paper
# Gracz decyduje ile chce zagrać rund
# Komputer podlicza punkty

from random import choice

name = input("What is your name player?\n")

print(f"Hello {name}! This is simple game called rock, scissors, paper.")

rounds = int(input("How many rounds you want to play?\n"))
i = 0

player_score = 0

computer_score = 0

hands = ('rock', 'scissors', 'paper')

while i < rounds:
    player_ch = input(
        f"{name} choose your hand rock, scissors or paper:\n").lower()
    if player_ch not in hands:
        raise ValueError("You must type rock, scissors or paper")
        break
    comp_ch = choice(hands)

    print(f"Computer hand: {comp_ch}")
    if player_ch == comp_ch:
        print("It's a draw!")
    elif player_ch == "rock" and comp_ch == "scissors":
        print(f"{name} wins!")
        player_score += 1
    elif (player_ch == "scissors" and comp_ch == "paper"):
        print(f"{name} wins!")
        player_score += 1
    elif (player_ch == "paper" and comp_ch == "rock"):
        print(f"{name} wins!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    i += 1
    print(f"Player: {player_score} vs Computer: {computer_score}")
