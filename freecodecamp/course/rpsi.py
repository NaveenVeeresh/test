from enum import Enum
import random
import sys

game_count = 0


def rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    playerchoice = input("enter.....\n1 for rock \nand 2 for scissor or\n3 paper:\n")

    if playerchoice not in ['1', '2', '3']:
        print("please enter correct choice")
        return rps()

    player = int(playerchoice)
    computerchoice = random.choice('123')
    computer = int(computerchoice)
    print("")
    print(f"u choose " + str(RPS(player)).replace("RPS", "").title() + ".")
    print(f"Computer choose " + str(RPS(computer)).replace("RPS", "").title() + ".")

    def decide_winer(player, computer):
        if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
            return "u win"

        elif player == computer:
            return "draw"
        else:
            return "computer win"

    result = decide_winer(player, computer)
    print(result)
    global game_count
    game_count += 1
    print("")
    print(f"\n game_count:{game_count}")
    print("Play Again!!!")
    while True:
        playagain = input("\n Y for yes or \nQ to quit?\n\n")
        if playagain.lower() not in ['y', 'q']:
            continue
        else:
            break

    if playagain.lower() == 'y':
        rps()
    else:
        print("bYe!!!!")
        sys.exit()


rps()
