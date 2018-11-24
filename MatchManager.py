import BoardManager


class GameManager:
    def __init__(self):
        self.move = 0
        self.boardManager = BoardManager.BoardManager()
        self.startingPlayer = 0
        self.winner = None

    def update(self, position):
        if self.move < 9:
            if position is not None:
                self.boardManager.setMove(self.move % 2, position)
            self.boardManager.printBoard()
            self.move += 1
            self.winner = self.boardManager.getWin()
            print('-------\n')
