class BoardManager:
    def __init__(self):
        self.board = [None] * 9

    @staticmethod
    def rotateBoard(board):
        rotated = [0] * 9
        val = -1
        for i in range(9):
            if val <= 1:
                val += 10
            val -= 3
            rotated[i] = board[val]
        return rotated

    def printBoard(self):
        output = ''
        for i in range(3):
            output += '|'
            for j in range(3):
                x = self.board[i * 3 + j]
                if x is None:
                    x = ' '
                elif x == 0:
                    x = 'x'
                elif x == 1:
                    x = 'o'
                output += x
                output += '|'
            output += '\n'
        print(output)

    def setMove(self, player, position):
        self.board[position] = player

    def getWin(self):
        bufferBoard = self.board
        for i in range(4):
            if bufferBoard[0] == bufferBoard[1] == bufferBoard[2] or \
                    bufferBoard[0] == bufferBoard[4] == bufferBoard[8] \
                    and bufferBoard[0] is not None:
                return bufferBoard[0]
            if bufferBoard[3] == bufferBoard[4] == bufferBoard[5] and bufferBoard[3] is not None:
                return bufferBoard[3]
            bufferBoard = BoardManager.rotateBoard(bufferBoard)
        print("no winner yet")
        return None
