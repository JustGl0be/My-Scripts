# KINDA FUNCTIONAL BATTLESHIP!

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):

    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for go in board:

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            for turn in range(4):

                print("You missed my battleship!")

                board[guess_row][guess_col] = "X"

                real_turn = 0
                real_turn = real_turn + 1
                print(real_turn)
                if real_turn == 4:
                    print("Game Over")
                    break
    print_board(board)
