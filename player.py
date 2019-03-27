import MaxConnect4Game as M
import time

class Player:
    def __init__(self):
        initGameBoard = M.MaxConnect4Game()
        d_limit=0

    def setInitState(self,inFile,gMode,nxtP):
        self.initGameBoard = M.MaxConnect4Game()
        self.initGameBoard.setBoardFromFile(inFile,gMode,nxtP)
        self.initGameBoard.printGameBoard()
        return self.initGameBoard

    def minimaxDecision(self, initGameBoard):
        score = 0
        move = -1
        S_Time = time.time()
        mx = self.successor(initGameBoard)
        v = float(-100000)
        for k in mx.iterkeys():
            temp = self.minValue(mx[k], alpha=-100000, beta=100000, depth=1)
            if temp >= v:
                v = temp
                move = k
        E_Time = time.time()
        print 'Time :', (E_Time-S_Time)
        isvalid, demo = initGameBoard.playPiece(move)
        return demo, move, v

    def successor(self, gameboard):
        mx = {}
        nCol = gameboard.numberofpossibleColumns()
        for i in range(len(nCol)):
            move = nCol.pop()
            isValid, newGameboard = gameboard.playPiece(move)
            mx[move] = newGameboard
        return mx

    def maxValue(self,currentGameboard, alpha, beta, depth):
        v = float(-100000)
        cnt = currentGameboard.chkPcount()
        if cnt == 42:
            util = currentGameboard.utility()
            return util
        elif depth == self.d_limit:
            score = currentGameboard.evaluation()
            return score
        else:
            depth = depth + 1
            mx = self.successor(currentGameboard)
            for k in mx.iterkeys():
                board = mx[k]
                temp = self.minValue(board, alpha, beta, depth)
                if temp >= v:
                    v = temp
                    move = k
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

    def minValue(self, currentGameboard, alpha, beta, depth):
        v = float(100000)
        cnt = currentGameboard.chkPcount()
        if cnt == 42:
            util = currentGameboard.utility()
            return util
        if depth == self.d_limit:
            score = currentGameboard.evaluation()
            return score
        else:
            depth = depth + 1
            mx = self.successor(currentGameboard)
            for k in mx.iterkeys():
                board = mx[k]
                temp = self.maxValue(board, alpha, beta, depth)
                if temp <= v:
                    v = temp
                    move = k
                if v <= alpha:
                    return  v
                beta = min(beta, v)
            return v
