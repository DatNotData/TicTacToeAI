import GameManager
import AIPlayer
import Controller

gameManager = GameManager.GameManager()

HUMAN = 1
AI = 0

gamePlayed = 0
humanWin = 0
aiWin = 0

while True:
    print('\nNEW GAME\n')
    ai = AIPlayer.AIPlayer(AI, HUMAN)
    gameManager = GameManager.GameManager()

    while True:
        print('AI\' turn')
        aiMove = ai.update(gameManager.move, gameManager.boardManager.board)
        gameManager.update(aiMove)

        if gameManager.winner is not None or gameManager.move == 9:
            break

        position = Controller.Controller.getPosition(gameManager)
        gameManager.update(position)

        if gameManager.winner is not None or gameManager.move == 9:
            break

    gamePlayed += 1
    winner = gameManager.winner
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
