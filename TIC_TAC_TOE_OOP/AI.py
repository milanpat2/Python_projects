import random


class AI:

    def __init__(self, brdx):
        self.move = None
        self.board = brdx

    def aiMove(self):
        # attacking moves by AI
        print("AI's move")
        if self.board.board[0] == "O" and self.board.board[3] == "O" and self.board.board[6] == "-":
            self.board.board[6] = "O"
            self.board.printBoard(self)
        elif self.board.board[0] == "O" and self.board.board[6] == "O" and self.board.board[3] == "-":
            self.board.board[3] = "O"
            self.board.printBoard(self)
        elif self.board.board[3] == "O" and self.board.board[6] == "O" and self.board.board[0] == "-":
            self.board.board[0] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "O" and self.board.board[4] == "O" and self.board.board[7] == "-":
            self.board.board[7] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "O" and self.board.board[7] == "O" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "O" and self.board.board[7] == "O" and self.board.board[1] == "-":
            self.board.board[1] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "O" and self.board.board[5] == "O" and self.board.board[8] == "-":
            self.board.board[8] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "O" and self.board.board[8] == "O" and self.board.board[5] == "-":
            self.board.board[5] = "O"
            self.board.printBoard(self)
        elif self.board.board[5] == "O" and self.board.board[8] == "O" and self.board.board[2] == "-":
            self.board.board[2] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "O" and self.board.board[0] == "O" and self.board.board[2] == "-":
            self.board.board[2] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "O" and self.board.board[0] == "O" and self.board.board[1] == "-":
            self.board.board[1] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "O" and self.board.board[2] == "O" and self.board.board[0] == "-":
            self.board.board[0] = "O"
            self.board.printBoard(self)
        elif self.board.board[3] == "O" and self.board.board[5] == "O" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[3] == "O" and self.board.board[4] == "O" and self.board.board[5] == "-":
            self.board.board[5] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "O" and self.board.board[5] == "O" and self.board.board[3] == "-":
            self.board.board[3] = "O"
            self.board.printBoard(self)
        elif self.board.board[6] == "O" and self.board.board[7] == "O" and self.board.board[8] == "-":
            self.board.board[8] = "O"
            self.board.printBoard(self)
        elif self.board.board[6] == "O" and self.board.board[8] == "O" and self.board.board[7] == "-":
            self.board.board[7] = "O"
            self.board.printBoard(self)
        elif self.board.board[7] == "O" and self.board.board[8] == "O" and self.board.board[6] == "-":
            self.board.board[6] = "O"
            self.board.printBoard(self)
        elif self.board.board[0] == "O" and self.board.board[4] == "O" and self.board.board[8] == "-":
            self.board.board[8] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "O" and self.board.board[8] == "O" and self.board.board[0] == "-":
            self.board.board[0] = "O"
            self.board.printBoard(self)
        elif self.board.board[0] == "O" and self.board.board[8] == "O" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "O" and self.board.board[4] == "O" and self.board.board[6] == "-":
            self.board.board[6] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "O" and self.board.board[6] == "O" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "O" and self.board.board[6] == "O" and self.board.board[2] == "-":
            self.board.board[2] = "O"
            self.board.printBoard(self)

        # # defending moves by AI
        elif self.board.board[0] == "X" and self.board.board[3] == "X" and self.board.board[6] == "-":
            self.board.board[6] = "O"
            self.board.printBoard(self)
        elif self.board.board[0] == "X" and self.board.board[6] == "X" and self.board.board[3] == "-":
            self.board.board[3] = "O"
            self.board.printBoard(self)
        elif self.board.board[3] == "X" and self.board.board[6] == "X" and self.board.board[0] == "-":
            self.board.board[0] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "X" and self.board.board[4] == "X" and self.board.board[7] == "-":
            self.board.board[7] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "X" and self.board.board[7] == "X" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "X" and self.board.board[7] == "X" and self.board.board[1] == "-":
            self.board.board[1] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "X" and self.board.board[5] == "X" and self.board.board[8] == "-":
            self.board.board[8] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "X" and self.board.board[8] == "X" and self.board.board[5] == "-":
            self.board.board[5] = "O"
            self.board.printBoard(self)
        elif self.board.board[5] == "X" and self.board.board[8] == "X" and self.board.board[2] == "-":
            self.board.board[2] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "X" and self.board.board[0] == "X" and self.board.board[2] == "-":
            self.board.board[2] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "X" and self.board.board[0] == "X" and self.board.board[1] == "-":
            self.board.board[1] = "O"
            self.board.printBoard(self)
        elif self.board.board[1] == "X" and self.board.board[2] == "X" and self.board.board[0] == "-":
            self.board.board[0] = "O"
            self.board.printBoard(self)
        elif self.board.board[3] == "X" and self.board.board[5] == "X" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[3] == "X" and self.board.board[4] == "X" and self.board.board[5] == "-":
            self.board.board[5] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "X" and self.board.board[5] == "X" and self.board.board[3] == "-":
            self.board.board[3] = "O"
            self.board.printBoard(self)
        elif self.board.board[6] == "X" and self.board.board[7] == "X" and self.board.board[8] == "-":
            self.board.board[8] = "O"
            self.board.printBoard(self)
        elif self.board.board[6] == "X" and self.board.board[8] == "X" and self.board.board[7] == "-":
            self.board.board[7] = "O"
            self.board.printBoard(self)
        elif self.board.board[7] == "X" and self.board.board[8] == "X" and self.board.board[6] == "-":
            self.board.board[6] = "O"
            self.board.printBoard(self)
        elif self.board.board[0] == "X" and self.board.board[4] == "X" and self.board.board[8] == "-":
            self.board.board[8] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "X" and self.board.board[8] == "X" and self.board.board[0] == "-":
            self.board.board[0] = "O"
            self.board.printBoard(self)
        elif self.board.board[0] == "X" and self.board.board[8] == "X" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "X" and self.board.board[4] == "X" and self.board.board[6] == "-":
            self.board.board[6] = "O"
            self.board.printBoard(self)
        elif self.board.board[2] == "X" and self.board.board[6] == "X" and self.board.board[4] == "-":
            self.board.board[4] = "O"
            self.board.printBoard(self)
        elif self.board.board[4] == "X" and self.board.board[6] == "X" and self.board.board[2] == "-":
            self.board.board[2] = "O"
            self.board.printBoard(self)

        else:
            while True:
                self.move = random.randrange(1, 10) - 1
                if self.board.board[self.move] == "-":
                    self.board.board[self.move] = "O"
                    self.board.printBoard(self)
                    return False

