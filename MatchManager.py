import BoardManager


class GameManager:
    def __init__(self):
        self.move = 0
        self.boardManager = BoardManager.BoardManager()
        self.startingPlayer = 0
        self.winner = None

    def update(self, player, position):
        if self.move < 9:
            if position is not None:
                self.boardManager.setMove(player, position)
            self.boardManager.print()
            self.move += 1
            self.winner = self.boardManager.getWin()
            print('-------\n')

    def isEnd(self):
        return self.winner is not None or self.move == 9
