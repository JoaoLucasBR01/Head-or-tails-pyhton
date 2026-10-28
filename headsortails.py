
# Heads or Tails game using Python
# The player chooses heads (0) or tails (1).
# At the end, the game shows who won more rounds.

import random

wins = 0
losses = 0

# Asks how many games will be played
games = int(input("How many games do you want to play?: "))

# Repeats the game for the chosen number of rounds
for round in range(games):

    print("\nRound", round + 1)

    option = input("Choose 0:Heads or 1:Tails: ")

    # Checks if the choice is valid
    while option != "0" and option != "1":
        option = input("Invalid option! Choose 0 or 1: ")

    option = int(option)

    # Randomly chooses 0 (Heads) or 1 (Tails)
    rand = random.randint(0, 1)

    if rand == option:
        wins += 1
        print("You won this round!")
    else:
        losses += 1
        print("You lost this round!")

    if rand == 0:
        print("Result: HEADS")
    else:
        print("Result: TAILS")

# Final report
print("\nFinal Report:")
print("Number of rounds won:", wins)
print("Number of rounds lost:", losses)

if wins > losses:
    print("Congratulations! You beat the computer!")
elif losses > wins:
    print("The computer won!")
else:
    print("The game ended in a tie!")
