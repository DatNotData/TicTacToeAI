import random
from BoardManager import *


class AIPlayer:

    def __init__(self, playerNum, opponentNum):
        self.playerNum = playerNum
        self.opponentNum = opponentNum

    def update(self, move, board):
        # if computer is able to win asap, then do it. if opponent about to win, then block
        for playerPriority in [self.playerNum,
                               self.opponentNum]:  # attack first if possible (because we will win anyways
            _board = board
            for i in range(4):
                if _board[0] == _board[1] and _board[0] == playerPriority and _board[2] is None:  # side layer
                    return [2, 0, 6, 8][i]
                elif _board[1] == _board[2] and _board[1] == playerPriority and _board[0] is None:
                    return [0, 6, 8, 2][i]
                elif _board[2] == _board[0] and _board[2] == playerPriority and _board[1] is None:

                    return [1, 3, 7, 5][i]
                elif _board[3] == _board[4] and _board[3] == playerPriority and _board[5] is None:  # middle layer
                    return [5, 1, 3, 7][i]
                elif _board[4] == _board[5] and _board[4] == playerPriority and _board[3] is None:
                    return [3, 7, 5, 2][i]
                elif _board[5] == _board[3] and _board[5] == playerPriority and _board[4] is None:

                    return 4
                elif _board[0] == _board[4] and _board[0] == playerPriority and _board[8] is None:  # diagonal
                    return [8, 2, 0, 6][i]
                elif _board[8] == _board[0] and _board[8] == playerPriority and _board[4] is None:
                    return 4

                _board = BoardManager.rotateBoard(_board)

        # computers starts first
        if move == 0:  # place in corner
            # return 0
            return [0, 2, 6, 8][random.randint(0, 3)]

        elif move == 2:
            if board[4] == self.opponentNum:  # if opponent places in center
                x = [board.index(self.playerNum)][0]
                if x is not None:
                    return [8, 6, 2, 0][[0, 2, 6, 8].index(x)]  # place in opposite corner

            _board = board
            for i in range(4):
                if _board[0] == self.playerNum:
                    if _board[1] == self.opponentNum:
                        return [6, 8, 2, 0][i]
                    elif _board[5] == self.opponentNum:
                        return [2, 0, 6, 8][i]
                    elif _board[7] == self.opponentNum:
                        return [6, 8, 2, 0][i]
                    elif _board[3] == self.opponentNum:
                        return [2, 8, 6, 0][i]

                _board = BoardManager.rotateBoard(_board)

            _board = board
            for i in range(4):
                if _board[0] == self.playerNum:
                    if _board[1] is None and _board[2] is None:
                        return [2, 0, 6, 8][i]
                    if _board[3] is None and _board[6] is None:
                        return [6, 8, 2, 0][i]
                    if _board[4] is None and _board[8] is None:
                        return [8, 2, 0, 6][i]
                _board = BoardManager.rotateBoard(_board)

        elif move == 4:
            _board = board
            for i in range(4):
                if _board[0] == self.playerNum:
                    if _board[1] is None and _board[2] is None and _board[6] == self.playerNum:
                        return [2, 0, 6, 8][i]
                    if _board[2] == self.playerNum and _board[3] is None and _board[6] is None:
                        return [6, 8, 2, 0][i]
                    if _board[8] is None and _board[4] is None and (
                            (_board[1] is None and _board[2] == self.playerNum) or (
                            _board[3] is None and _board[6] == self.playerNum)):
                        return 4
                _board = BoardManager.rotateBoard(_board)

        # human starts first
        elif move == 1:
            if board[4] == self.opponentNum:  # if opponents places in center
                return [0, 2, 6, 8][random.randint(0, 3)]  # place in a corner

            return 4  # if opponents places in corner or edge, place in center



        elif move == 3:
            _board = board
            buffer = []
            for i in range(4):
                if _board[0] == self.opponentNum:
                    return [[1, 3], [3, 7], [7, 5], [5, 1]][i][random.randint(0, 1)]

                if _board[1] == self.opponentNum and _board[4] == self.playerNum and _board[7] == (
                        not self.playerNum):
                    return [0, 2, 6, 8][random.randint(0, 3)]

                _board = BoardManager.rotateBoard(_board)

        # if we don't know what to do, output a random move, it's better than nothing
        buffer = []
        for i in range(9):
            if board[i] is None:
                buffer.append(i)
        if len(buffer) > 0:
            return buffer[random.randint(0, len(buffer) - 1)]

        return None
