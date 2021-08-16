import random

actions = ["ROCK", "PAPER", "SCISSORS"]
win = False

def play(player):
    computer = random.choice(actions)
    print(f"You chose {player} and computer chose {computer}...")
    if ((computer == "PAPER" and player == "SCISSORS") or
      (computer == "ROCK" and player == "PAPER") or
      (computer == "SCISSORS" and player == "ROCK")):
        print(f"{player} beats {computer}, you win!")
        return True
    elif (computer == player):
        print("Tie game, try again.")
    else:
        print(f"{computer} beats {player}, try again.")
    return False

while (win == False):
    choice = input("Enter rock, paper, or scissors: ").upper()
    win = play(choice)


