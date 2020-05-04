class PLAYER:

    def __init__(self, boardx):
        self.move = None
        self.board = boardx

    def playerMove(self):
        self.move = input("Enter a number from 1-9 for your next move: ")
        self.move = int(self.move) - 1
        return self.move
