import random
import time

# These are the global variables
game_status = True # game_status variable indicates current status of the game (game is running or ended)
yes_win = False # yes_win variable indicates if someone won or not
x = False # this variable is used in makeMove() function to make sure that user/computer is passing valid input
board = ["-"] * 9 # to create TIC TAC TOE game board
players = ["You", "Computer"]
CP = random.choice(players) # CP indicate the current player in the move

# Welcome message
print("X-O-X-O-X\nWELCOME TO TIC TAC TOE\nO-X-O-X-O")
print("You are X")
print("Computer is O")
print(CP, "will start the game")
time.sleep(1)


def play_board(): # Create a tic tac toe board
    print(board[0] + "|" + board[1] + "|" + board[2] + "   123")
    print(board[3] + "|" + board[4] + "|" + board[5] + "   456")
    print(board[6] + "|" + board[7] + "|" + board[8] + "   789")


play_board() # invoke the play_board()
print("")
time.sleep(1)


def makeMove(): # make a next move
    global board
    global CP
    global x
    if CP == "You":
        print("Your turn (X)")
        move = int(input("Enter number from 1 to 9 to place X: ")) - 1

        if move in range(0, 9):
            pass
        else:
            move = int(input("Invalid input, Enter number from 1 to 9: ")) - 1
            while True:
                if move in range(0, 9):
                    break
                else:
                    move = int(input("Invalid input again, Enter number from 1 to 9: ")) - 1

        if board[move] == "-":
            board[move] = "X"
            play_board()
        else:
            x = True
            while x:
                move = int(input("Invalid input, Please enter from 1 to 9 on empty spaces: ")) - 1

                if move in range(0, 9):
                    pass
                else:
                    move = int(input("Invalid input, Enter from 1 to 9: ")) - 1
                    while True:
                        if move in range(0, 9):
                            break
                        else:
                            move = int(input("Invalid input again, Enter from 1 to 9: ")) - 1

                if board[move] == "-":
                    x = False
                else:
                    x = True
            board[move] = "X"
            play_board()

    else:
        print("Computer's turn (O)")
        time.sleep(1)
        move = random.randrange(1, 10) - 1
        if board[move] == "-":
            board[move] = "O"
            play_board()
        else:
            x = True
            while x:
                move = random.randrange(1, 10) - 1
                if board[move] == "-":
                    x = False
                else:
                    x = True
            board[move] = "O"
            play_board()


def checkWin(): # Check if win
    global game_status
    global yes_win
    global CP
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[6] == board[4] == board[2] != "-"
    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        game_status = False
        yes_win = True
        print(CP, "WON")
    else:
        game_status = True
        yes_win = False
        print("")


def checkTie(): # Check if tie
    global game_status
    global yes_win
    if (board[0] != "-" and board[1] != "-" and board[2] != "-"
        and board[3] != "-" and board[4] != "-" and board[5] != "-"
        and board[6] != "-" and board[7] != "-" and board[8] != "-")\
            and (yes_win == False):
        print("TIE")
        game_status = False


def flipPlayer(): # To change the player's turn
    global CP
    if CP == "You":
        CP = "Computer"
    elif CP == "Computer":
        CP = "You"


def play_game(): # play_game is a main function to run the game
    global game_status
    while game_status: # If no win or tie(game_status: TRUE), loop is ON, keep playing
        makeMove() # Make a next move
        checkWin() # Check if win
        checkTie() # Check if tie
        flipPlayer() # To change the player's turn
        time.sleep(2)


play_game()
