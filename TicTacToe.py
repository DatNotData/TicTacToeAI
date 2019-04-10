from MatchManager import *
from BoardManager import *
from AIPlayer import *
from Controller import *

gamePlayed = 0
humanWin = 0
aiWin = 0

HUMAN = 0
AI = 1

starter = int(input('Enter: 0 if human start, 1 if computer start, 2 if alternate >>> '))

def humanRoutine():
    move = 'qweasdzxc'.index(input('ENTER MOVE >>> '))
    matchManager.update(HUMAN, move)

def aiRoutine():
    print('AI\' turn')
    aiMove = ai.update(matchManager.move, matchManager.boardManager.board)
    matchManager.update(AI, aiMove)



while True:
    print('\nNEW GAME\n')
    matchManager = GameManager()

    if starter == 0 or (starter == 2 and gamePlayed % 2 == 0):
        ai = AIPlayer(AI, HUMAN)
        while True:
            humanRoutine()
            if matchManager.isEnd():
                break

            aiRoutine()
            if matchManager.isEnd():
                break

    elif starter == 1 or (starter == 2 and gamePlayed % 2 == 1):
        ai = AIPlayer(AI, HUMAN)
        while True:
            aiRoutine()
            if matchManager.isEnd():
                break

            humanRoutine()
            if matchManager.isEnd():
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

    input(' Reset board and press ENTER to start new game')

    print('\n---------------------------------')
    print('-END-END-END-END-END-END-END-END-')
    print('---------------------------------\n')
