from random import randrange as rr
import pdb

def show(game_board):
    print("\n")
    print game_board[0], "|", game_board[1], "|", game_board[2]
    print("__________")
    print game_board[3], "|", game_board[4], "|", game_board[5]
    print("__________")
    print game_board[6], "|", game_board[7], "|", game_board[8]


def check_uwin(game_board):
    if game_board[0] == "X" and game_board[1] == "X" and game_board[2] == "X":
        return True
    elif game_board[3] == "X" and game_board[4] == "X" and game_board[5] == "X":
        return True
    elif game_board[6] == "X" and game_board[7] == "X" and game_board[8] == "X":
        return True
    elif game_board[0] == "X" and game_board[4] == "X" and game_board[8] == "X":
        return True
    elif game_board[6] == "X" and game_board[4] == "X" and game_board[2] == "X":
        return True
    elif game_board[0] == "X" and game_board[3] == "X" and game_board[6] == "X":
        return True
    elif game_board[1] == "X" and game_board[4] == "X" and game_board[7] == "X":
        return True
    elif game_board[2] == "X" and game_board[5] == "X" and game_board[8] == "X":
        return True
    else:
        return False

def check_win(game_board):
    if game_board[0] == "O" and game_board[1] == "O" and game_board[2] == "O":
        return True
    elif game_board[3] == "O" and game_board[4] == "O" and game_board[5] == "O":
        return True
    elif game_board[6] == "O" and game_board[7] == "O" and game_board[8] == "O":
        return True
    elif game_board[0] == "O" and game_board[4] == "O" and game_board[8] == "O":
        return True
    elif game_board[6] == "O" and game_board[4] == "O" and game_board[2] == "O":
        return True
    elif game_board[0] == "O" and game_board[3] == "O" and game_board[6] == "O":
        return True
    elif game_board[1] == "O" and game_board[4] == "O" and game_board[7] == "O":
        return True
    elif game_board[2] == "O" and game_board[5] == "O" and game_board[8] == "O":
        return True
    else:
        return False

def play(game_board):
    total = 9
    while total > 0:
        inptu = False
        while inptu == False:
            print("Enter position to mark it 'X'.")
            inpt = int(raw_input())
            if game_board[inpt] != "X" and game_board[inpt] != "O":
                game_board[inpt] = "X"
                show(game_board)
                if check_uwin(game_board):
                    print("You win!")
                    return
                inptu = True
                total -= 1
            else:
                print("Choose another position, this one is already taken.")
                continue
        if total == 0:
            break
        inptr = False
        while inptr == False:
            sys_inpt = rr(0, 8)
            if game_board[sys_inpt] != "X" and game_board[sys_inpt] != "O":
                game_board[sys_inpt] = "O"
                show(game_board)
                if check_win(game_board):
                    print("System win!")
                total -= 1
                inptr = True
    print("It is a draw!")

def create_setup():
    game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    show(game_board)
    play(game_board)
    pass


def game():
    create_setup()

if __name__ == "__main__":
    game()
