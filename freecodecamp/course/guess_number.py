import sys
import random


def guess_number(name: 'PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guessnumber():
        nonlocal game_count
        nonlocal player_wins

        playerchoice = input(f"\n {name} ,guess number im thinking 1,2 or 3")
        if playerchoice not in ['1', '2', '3']:
            print(f"{name} : please enter 1,2 or 3")
            return play_guessnumber()

        computerchoicer = random.choice('123')
        print(f"\n {name}: u chose {playerchoice}")
        print(f"\n computerchoice : {computerchoicer}")

        player = int(playerchoice)
        computerchoice = int(computerchoicer)

        def decide_winner(player, computerchoice):
            nonlocal name
            nonlocal player_wins
            if player == computerchoice:
                player_wins += 1
                return f"{name}, U win"
            else:
                return f"sorry {name}, Better luck next time!!"

        game_result = decide_winner(player, computerchoice)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n GameCount:{game_count}")
        print(f"\n {name}'s wins:{player_wins}")
        print(f" \n {name} ur winning percentage is :{player_wins / game_count:.2%}")

        print(f"\n play again")
        while True:
            playagain = input(f"\n Y for yes or \n q to quit")
            if playagain.lower() == 'y':
                return play_guessnumber()
            else:
                print(f"Thank u BYE!!")
                if __name__ == "__main__":
                    sys.exit("bye")
                else:
                    return

    return play_guessnumber


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="game experience"
    )
    parser.add_argument(
        '-n', '--name', metavar="name",
        required=True, help="the name of person playing"

    )

    args = parser.parse_args()
    guess_number = guess_number(args.name)
    guess_number()
