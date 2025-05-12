from enum import Enum
import random
import sys


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        playerchoice = input("{name} enter.....\n1 for rock \nand 2 for scissor or\n3 paper:\n")

        if playerchoice not in ['1', '2', '3']:
            print("please enter correct choice")
            return rps()

        player = int(playerchoice)
        computerchoice = random.choice('123')
        computer = int(computerchoice)
        print("")
        print(f"\n {name}, choose " + str(RPS(player)).replace("RPS", "").title() + ".")
        print(f"Computer choose " + str(RPS(computer)).replace("RPS", "").title() + ".")

        def decide_winer(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
                player_wins += 1
                return "{name} win"
            elif player == computer:
                return "draw"
            else:
                python_wins += 1
                return "computer win"

        result = decide_winer(player, computer)
        print(result)
        nonlocal game_count
        game_count += 1
        print("")
        print(f"\n game_count:{game_count}")
        print(f"\n {name} wins: {player_wins}")
        print(f"\n pyhton wins: {python_wins}")

        print("Play Again!!!")
        while True:
            playagain = input("\n Y for yes or \nQ to quit?\n\n")
            if playagain.lower() not in ['y', 'q']:
                continue
            else:
                break

        if playagain.lower() == 'y':
            return play_rps()
        else:
            print("bYe!!!!")
            sys.exit()

    return play_rps


rock_paper_scsissors = rps()

if __name__ == "__main__":
    import argparse

    # as the name says, its command line args
    # required means mandatory =true

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="the name of person to greet in game"
    )

    args = parser.parse_args()
    rock_paper_scsissors = rps(args.name)
    rock_paper_scsissors()
