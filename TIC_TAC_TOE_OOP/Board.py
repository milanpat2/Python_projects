class BOARD:
    board = ["-"] * 9

    def __init__(self, plyr, ai):
        self.player = plyr
        self.ai = ai

    def printBoard(self):
        print(BOARD.board[0] + "|" + BOARD.board[1] + "|" + BOARD.board[2] + "   123")
        print(BOARD.board[3] + "|" + BOARD.board[4] + "|" + BOARD.board[5] + "   456")
        print(BOARD.board[6] + "|" + BOARD.board[7] + "|" + BOARD.board[8] + "   789")

    def playerMoveCheck(self):
        if self.player.move in range(0, 9):
            pass
        else:
            while True:
                if self.player.move in range(0, 9):
                    break
                else:
                    self.player.playerMove()

        if BOARD.board[self.player.move] == "-":
            BOARD.board[self.player.move] = "X"
            BOARD.printBoard(self)
        else:
            x = True
            while x:
                self.player.playerMove()
                if self.player.move in range(0, 9):
                    pass
                else:
                    self.player.playerMove()
                    while True:
                        if self.player.move in range(0, 9):
                            break
                        else:
                            self.player.playerMove()

                if BOARD.board[self.player.move] == "-":
                    x = False
                else:
                    x = True
            BOARD.board[self.player.move] = "X"
            BOARD.printBoard(self)
