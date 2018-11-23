class Controller:
    @staticmethod
    def getRawPosition():
        x = input()
        ch = 'qweasdzxc'
        x = ch.find(x)
        return x

    @staticmethod
    def getPosition(gameManager):
        while True:
            print("Player %s, please enter your move : " % (gameManager.move % 2))
            position = Controller.getRawPosition()
            if gameManager.boardManager.board[position] is None and position != -1:
                return position
            print("Input failed, try again.")
