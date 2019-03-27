import player as P
import sys

def main(av):
    nxtP = ''
    inFile = ''
    outFile = ''
    gMode = av[1]

    if gMode == 'interactive':
        inFile = av[2]
        nxtP = av[3]
        initnxtP=nxtP
        player = P.player()
        player.d_limit = int(av[4])
        initstate = player.setInitState(inFile,gMode,nxtP)
        while True:
            count = initstate.chkPCount()
            if count == 42 and initnxtP=='computer-next':
                initstate.scoreCount()
                print 'Computers Score: ', initstate.player1score
                print 'players core:', initstate.player2score
                initstate.printGameBoard()
                break
            elif count==42 and initnxtP=='human-next':
                initstate.scoreCount()
                print 'Computers Score: ', initstate.player2score
                print 'players Score:', initstate.player1score
                initstate.printGameBoard()
                break

            elif nxtP == 'computer-next':
                initstate, move, score = player.minimaxDecision(initstate)
                initstate.scoreCount()
                print 'Computer Score: ', initstate.player1score
                print 'players Scores:', initstate.player2score
                initstate.printBoardToFile('computer.txt')
                nxtP = 'human-next'

            elif nxtP == 'human-next':
                initstate.scoreCount()
                initstate.printGameBoard()
                print 'Computer Score:', initstate.player2score
                print 'players Score: ', initstate.player1score
                print "Enter column between 1-7:"
                H_Move = int(raw_input())
                while H_Move<1 or H_Move>7:
                    print "Enter column between 1-7:"
                    H_Move = int(raw_input())
                isValid, initstate = initstate.playPiece(H_Move-1)
                while not isValid:
                    print "Enter column between 1-7:"
                    H_Move = int(raw_input())
                    isValid, initstate = initstate.playPiece(H_Move-1)
                initstate.printBoardToFile('human.txt')
                nxtP = 'computer-next'

    elif gMode == 'one-move':
        inFile = av[2]
        outFile = av[3]
        player = P.player()
        player.d_limit = int(av[4])
        initstate = player.setInitState(inFile,gMode,nxtP)
        temp, move, score = player.minimaxDecision(initstate)
        print 'Move : Column', move+1
        print 'Score:', score
        print 'GameBoard after column',move+1,'move:'
        temp.printGameBoard()
        temp.printBoardToFile(outFile)

if __name__ == '__main__':
    main(sys.av)
