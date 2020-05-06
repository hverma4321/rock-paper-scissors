from random import randint
from playsound import playsound
loop = raw_input("How many times would you like to play?")
rawloop = int(loop)
summary = ["SUMMARY"]

win = 0
lose = 0

while rawloop != 0:

    game = randint(1, 3)

    player = raw_input('Rock, Paper, or Scissors?')


    if player == 'rock':
        player = 1
    elif player == 'paper':
        player = 2
    elif player == 'scissors':
        player = 3
    else:
        print("Try something else.")



    if player == 1:
        if game == 1:
            print("computer chose rock. tie")
            summary.append('rock-rock')
        elif game == 2:
            print("computer chose paper. lose")
            lose = lose + 1
            playsound('lose.mp3')
            summary.append('rock-paper')
        elif game == 3:
            print("computer chose scissors. win")
            win = win + 1
            playsound('win.mp3')
            summary.append('rock-scissors')
    elif player == 2:
        if game == 1:
            print("computer chose rock. win")
            win = win + 1
            playsound('win.mp3')
            summary.append('paper-rock')
        elif game == 2:
            print("computer chose paper. tie")
            summary.append('paper-paper')
        elif game == 3:
            print("computer chose scissors. lose")
            summary.append('paper-scissors')
            lose = lose + 1
            playsound('lose.mp3')
    elif player == 3:
        if game == 1:
            print("computer chose rock. lose")
            summary.append('scissors-rock')
            lose = lose + 1
            playsound('lose.mp3')
        elif game == 2:
            print("computer chose paper. win")
            win = win + 1
            playsound('win.mp3')
            summary.append('scissors-paper')
        elif game == 3:
                print("computer chose scissors. tie")
                summary.append('scissors-scissors')


    rawloop = rawloop-1

if win > lose:
    print("You win this round!")
    playsound('win.mp3')
elif win < lose:
    print("You lost this round...")
    playsound('lose.mp3')
else:
    print("You tied.")

print("The summary is read like this: player-computer")
print(summary)
