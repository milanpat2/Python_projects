import random
import time
from Board import BOARD
from Player import PLAYER
from AI import AI


class SYSTEM:
    participants = ["You", "AI"]
    CP = random.choice(participants)
    print(CP + " will start the game")

    def __init__(self):
        self.player = PLAYER(BOARD)
        self.ai = AI(BOARD)
        self.board = BOARD(self.player, self.ai)
        self.x = True
        self.winner = False
        self.currentPlayer = SYSTEM.CP

    def checkWin(self):  # Check if win
        row1 = BOARD.board[0] == BOARD.board[1] == BOARD.board[2] != "-"
        row2 = BOARD.board[3] == BOARD.board[4] == BOARD.board[5] != "-"
        row3 = BOARD.board[6] == BOARD.board[7] == BOARD.board[8] != "-"
        col1 = BOARD.board[0] == BOARD.board[3] == BOARD.board[6] != "-"
        col2 = BOARD.board[1] == BOARD.board[4] == BOARD.board[7] != "-"
        col3 = BOARD.board[2] == BOARD.board[5] == BOARD.board[8] != "-"
        diag1 = BOARD.board[0] == BOARD.board[4] == BOARD.board[8] != "-"
        diag2 = BOARD.board[6] == BOARD.board[4] == BOARD.board[2] != "-"
        if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
            print(self.currentPlayer, "WON")
            self.x = False
            self.winner = True
        else:
            self.x = True
            self.winner = False
            print("")

    def checkTie(self):  # Check if tie
        if (BOARD.board[0] != "-" and BOARD.board[1] != "-" and BOARD.board[2] != "-"
            and BOARD.board[3] != "-" and BOARD.board[4] != "-" and BOARD.board[5] != "-"
            and BOARD.board[6] != "-" and BOARD.board[7] != "-" and BOARD.board[8] != "-") \
                and (self.winner == False):
            print("It is a draw game")
            self.x = False

    def switchTurn(self):
        if self.currentPlayer == "You":
            self.currentPlayer = "AI"
        elif self.currentPlayer == "AI":
            self.currentPlayer = "You"

    def playGame(self):
        while self.x:
            if self.currentPlayer == "You":
                self.player.playerMove()
                self.board.playerMoveCheck()
                SYSTEM.checkWin(self)
                SYSTEM.checkTie(self)
                SYSTEM.switchTurn(self)
                time.sleep(1)
            else:
                self.ai.aiMove()
                SYSTEM.checkWin(self)
                SYSTEM.checkTie(self)
                SYSTEM.switchTurn(self)
                time.sleep(1)


a = SYSTEM()
a.playGame()
