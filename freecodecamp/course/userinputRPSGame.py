import sys
import random
from enum import Enum
from operator import contains


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    # print(RPS.ROCK)
    # print(RPS(2))
    # print(RPS['PAPER'])
    # print(RPS.SCISSOR.value)

    # rock paper scissors game!
    playerchoice = input("enter.....\n1 for rock \nand 2 for scissor or\n3 paper:\n")

    if playerchoice not in ["1", "2", "3"]:
        print("entered wrong choice")
        return play_rps()
    player = int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("")
    print("u choose :" + str(RPS(player)).replace("RPS.", "") + ".")
    print("computer choose :" + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print("u win")
    elif player == computer:
        print("draw")
    else:
        print("computer win")

    print("\n play Again? ")
    while True:
        playagain = input("\n Y for yes or \nQ to quit?\n\n")
        if playagain.lower() not in ['y', 'q']:
            continue
        else:
            break

    if playagain.lower() == 'y':
        return play_rps()
    else:
        print("\n see u")
        sys.exit()


play_rps()
