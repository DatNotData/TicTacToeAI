import MatchManager
import AIPlayer
import Controller

gamePlayed = 0
humanWin = 0
aiWin = 0

print('Enter: 0 if human start, 1 if computer start, 2 if alternate')
starter = int(input())

while True:
    print('\nNEW GAME\n')
    matchManager = MatchManager.GameManager()

    if starter == 0 or (starter == 2 and gamePlayed % 2 == 0):
        while True:
            HUMAN = 0
            AI = 1
            ai = AIPlayer.AIPlayer(AI, HUMAN)
            position = Controller.Controller.getPosition(matchManager)
            matchManager.update(position)

            if matchManager.winner is not None or matchManager.move == 9:
                break

            print('AI\' turn')
            aiMove = ai.update(matchManager.move, matchManager.boardManager.board)
            matchManager.update(aiMove)

            if matchManager.winner is not None or matchManager.move == 9:
                break

    elif starter == 1 or (starter == 2 and gamePlayed % 2 == 1):
        while True:
            HUMAN = 1
            AI = 0
            ai = AIPlayer.AIPlayer(AI, HUMAN)
            print('AI\' turn')
            aiMove = ai.update(matchManager.move, matchManager.boardManager.board)
            matchManager.update(aiMove)

            if matchManager.winner is not None or matchManager.move == 9:
                break

            position = Controller.Controller.getPosition(matchManager)
            matchManager.update(position)

            if matchManager.winner is not None or matchManager.move == 9:
                break

    gamePlayed += 1
    winner = matchManager.winner
    if winner == HUMAN:
        winner = 'HUMAN'
        humanWin += 1
    elif winner == AI:
        winner = 'COMPUTER'
        aiWin += 1
    else:
        winner = 'nobody'
    print('Winner is %s.' % winner)

    print('%s game played, human won %s times and computer won %s times.' % (gamePlayed, humanWin, aiWin))

    input('Press ENTER to start new game')

    print('\n---------------------------------')
    print('-END-END-END-END-END-END-END-END-')
    print('---------------------------------\n')
