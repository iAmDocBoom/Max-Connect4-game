from copy import deepcopy

class MaxConnect4Game:

    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.player1 = 0
        self.player2 = 0
        self.pieceCount = 0

    def chkPcount(self):
        self.pieceCount = 0
        for row in self.gameBoard:
            for piece in row:
                if piece != 0:
                    self.pieceCount+=1
        return self.pieceCount

    def isvalidMove(self,position):
        row = self.gameBoard[0]
        if row[position] == 0:
            return True
        else:
            return False

    def noofposscols(self):
        return [i for i, x in enumerate(self.gameBoard[0]) if x == 0]

    def printGameBoard(self):
        print ' -----------------'
        for i in range(0,6):
            print ' |',
            for j in range(0,7):
                print('%d' % self.gameBoard[i][j]),
            print '| '
        print ' -----------------'

    def printBoardToFile(self,outFile):
        fp = open(outFile, 'wb')
        for row in self.gameBoard:
            for piece in row:
                fp.write(str(piece))
            fp.write('\n')
        fp.write(str(self.currentTurn))
        fp.close()

    def setBoardFromFile(self,inFile,gMode,nxtP):
        count = 0
        fi=open(inFile).readlines()
        for li in fi:
            if count == 6:
                self.currentTurn = int(li)
                if gMode =='one-move':
                    self.player1 = self.currentTurn
                    if self.player1 == 1:
                        self.player2 = 2
                    else:
                        self.player2 = 1
                elif gMode == 'interactive':
                    if nxtP == 'human-next':
                        self.player1 = self.currentTurn
                        self.player2 = 3 - self.player1
                    elif nxtP=='computer-next':
                        self.player2 = self.currentTurn
                        self.player1 = 3 - self.player2

            else:
                self.gameBoard[count] = map(int, list(li.rstrip()))
            count+=1

    def playPiece(self,column):
        temp = deepcopy(self)
        if temp.isvalidMove(column):
            for row in range(5,-1, -1):
                if temp.gameBoard[row][column] == 0:
                    temp.gameBoard[row][column] = temp.currentTurn
                    if temp.currentTurn == temp.player1:
                        temp.currentTurn = temp.player2
                    else:
                        temp.currentTurn = temp.player1
                    break
        else:
            print "Invalid move"
            return False, self
        return True, temp

    def utility(self):
        self.countScore()
        return self.player1score - self.player2score

    def evaluation(self):
        self.countScoreDepthLimit()
        return self.player1score - self.player2score


    def countScore(self):
        self.player1score = 0;
        self.player2score = 0;

        #Horizontal Check
        for row in self.gameBoard:
            # Checking for Player 1
            if row[0:4] == [self.player1]*4:
                self.player1score += 1
            if row[1:5] == [self.player1]*4:
                self.player1score += 1
            if row[2:6] == [self.player1]*4:
                self.player1score += 1
            if row[3:7] == [self.player1]*4:
                self.player1score += 1
            # Checking for player 2
            if row[0:4] == [self.player2]*4:
                self.player2score += 1
            if row[1:5] == [self.player2]*4:
                self.player2score += 1
            if row[2:6] == [self.player2]*4:
                self.player2score += 1
            if row[3:7] == [self.player2]*4:
                self.player2score += 1

        # Vertical Check
        for j in range(7):
            # Checking for player 1
            if (self.gameBoard[0][j] == self.player1 and self.gameBoard[1][j] == self.player1 and
                   self.gameBoard[2][j] == self.player1 and self.gameBoard[3][j] == self.player1):
                self.player1score += 1
            if (self.gameBoard[1][j] == self.player1 and self.gameBoard[2][j] == self.player1 and
                   self.gameBoard[3][j] == self.player1 and self.gameBoard[4][j] == self.player1):
                self.player1score += 1
            if (self.gameBoard[2][j] == self.player1 and self.gameBoard[3][j] == self.player1 and
                   self.gameBoard[4][j] == self.player1 and self.gameBoard[5][j] == self.player1):
                self.player1score += 1
            # Checking for player 2
            if (self.gameBoard[0][j] == self.player2 and self.gameBoard[1][j] == self.player2 and
                   self.gameBoard[2][j] == self.player2 and self.gameBoard[3][j] == self.player2):
                self.player2score += 1
            if (self.gameBoard[1][j] == self.player2 and self.gameBoard[2][j] == self.player2 and
                   self.gameBoard[3][j] == self.player2 and self.gameBoard[4][j] == self.player2):
                self.player2score += 1
            if (self.gameBoard[2][j] == self.player2 and self.gameBoard[3][j] == self.player2 and
                   self.gameBoard[4][j] == self.player2 and self.gameBoard[5][j] == self.player2):
                self.player2score += 1

        # Checking diagonally

        # Checking for player 1
        if (self.gameBoard[2][0] == self.player1 and self.gameBoard[3][1] == self.player1 and
               self.gameBoard[4][2] == self.player1 and self.gameBoard[5][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][0] == self.player1 and self.gameBoard[2][1] == self.player1 and
               self.gameBoard[3][2] == self.player1 and self.gameBoard[4][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][1] == self.player1 and self.gameBoard[3][2] == self.player1 and
               self.gameBoard[4][3] == self.player1 and self.gameBoard[5][4] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][0] == self.player1 and self.gameBoard[1][1] == self.player1 and
               self.gameBoard[2][2] == self.player1 and self.gameBoard[3][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][1] == self.player1 and self.gameBoard[2][2] == self.player1 and
               self.gameBoard[3][3] == self.player1 and self.gameBoard[4][4] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][2] == self.player1 and self.gameBoard[3][3] == self.player1 and
               self.gameBoard[4][4] == self.player1 and self.gameBoard[5][5] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][1] == self.player1 and self.gameBoard[1][2] == self.player1 and
               self.gameBoard[2][3] == self.player1 and self.gameBoard[3][4] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][2] == self.player1 and self.gameBoard[2][3] == self.player1 and
               self.gameBoard[3][4] == self.player1 and self.gameBoard[4][5] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][3] == self.player1 and self.gameBoard[3][4] == self.player1 and
               self.gameBoard[4][5] == self.player1 and self.gameBoard[5][6] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][2] == self.player1 and self.gameBoard[1][3] == self.player1 and
               self.gameBoard[2][4] == self.player1 and self.gameBoard[3][5] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][3] == self.player1 and self.gameBoard[2][4] == self.player1 and
               self.gameBoard[3][5] == self.player1 and self.gameBoard[4][6] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][3] == self.player1 and self.gameBoard[1][4] == self.player1 and
               self.gameBoard[2][5] == self.player1 and self.gameBoard[3][6] == self.player1):
            self.player1score += 1

        if (self.gameBoard[0][3] == self.player1 and self.gameBoard[1][2] == self.player1 and
               self.gameBoard[2][1] == self.player1 and self.gameBoard[3][0] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][4] == self.player1 and self.gameBoard[1][3] == self.player1 and
               self.gameBoard[2][2] == self.player1 and self.gameBoard[3][1] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][3] == self.player1 and self.gameBoard[2][2] == self.player1 and
               self.gameBoard[3][1] == self.player1 and self.gameBoard[4][0] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][5] == self.player1 and self.gameBoard[1][4] == self.player1 and
               self.gameBoard[2][3] == self.player1 and self.gameBoard[3][2] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][4] == self.player1 and self.gameBoard[2][3] == self.player1 and
               self.gameBoard[3][2] == self.player1 and self.gameBoard[4][1] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][3] == self.player1 and self.gameBoard[3][2] == self.player1 and
               self.gameBoard[4][1] == self.player1 and self.gameBoard[5][0] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][6] == self.player1 and self.gameBoard[1][5] == self.player1 and
               self.gameBoard[2][4] == self.player1 and self.gameBoard[3][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][5] == self.player1 and self.gameBoard[2][4] == self.player1 and
               self.gameBoard[3][3] == self.player1 and self.gameBoard[4][2] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][4] == self.player1 and self.gameBoard[3][3] == self.player1 and
               self.gameBoard[4][2] == self.player1 and self.gameBoard[5][1] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][6] == self.player1 and self.gameBoard[2][5] == self.player1 and
               self.gameBoard[3][4] == self.player1 and self.gameBoard[4][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][5] == self.player1 and self.gameBoard[3][4] == self.player1 and
               self.gameBoard[4][3] == self.player1 and self.gameBoard[5][2] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][6] == self.player1 and self.gameBoard[3][5] == self.player1 and
               self.gameBoard[4][4] == self.player1 and self.gameBoard[5][3] == self.player1):
            self.player1score += 1

        # Checking for player 2
        if (self.gameBoard[2][0] == self.player2 and self.gameBoard[3][1] == self.player2 and
               self.gameBoard[4][2] == self.player2 and self.gameBoard[5][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][0] == self.player2 and self.gameBoard[2][1] == self.player2 and
               self.gameBoard[3][2] == self.player2 and self.gameBoard[4][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][1] == self.player2 and self.gameBoard[3][2] == self.player2 and
               self.gameBoard[4][3] == self.player2 and self.gameBoard[5][4] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][0] == self.player2 and self.gameBoard[1][1] == self.player2 and
               self.gameBoard[2][2] == self.player2 and self.gameBoard[3][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][1] == self.player2 and self.gameBoard[2][2] == self.player2 and
               self.gameBoard[3][3] == self.player2 and self.gameBoard[4][4] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][2] == self.player2 and self.gameBoard[3][3] == self.player2 and
               self.gameBoard[4][4] == self.player2 and self.gameBoard[5][5] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][1] == self.player2 and self.gameBoard[1][2] == self.player2 and
               self.gameBoard[2][3] == self.player2 and self.gameBoard[3][4] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][2] == self.player2 and self.gameBoard[2][3] == self.player2 and
               self.gameBoard[3][4] == self.player2 and self.gameBoard[4][5] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][3] == self.player2 and self.gameBoard[3][4] == self.player2 and
               self.gameBoard[4][5] == self.player2 and self.gameBoard[5][6] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][2] == self.player2 and self.gameBoard[1][3] == self.player2 and
               self.gameBoard[2][4] == self.player2 and self.gameBoard[3][5] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][3] == self.player2 and self.gameBoard[2][4] == self.player2 and
               self.gameBoard[3][5] == self.player2 and self.gameBoard[4][6] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][3] == self.player2 and self.gameBoard[1][4] == self.player2 and
               self.gameBoard[2][5] == self.player2 and self.gameBoard[3][6] == self.player2):
            self.player2score += 1

        if (self.gameBoard[0][3] == self.player2 and self.gameBoard[1][2] == self.player2 and
               self.gameBoard[2][1] == self.player2 and self.gameBoard[3][0] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][4] == self.player2 and self.gameBoard[1][3] == self.player2 and
               self.gameBoard[2][2] == self.player2 and self.gameBoard[3][1] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][3] == self.player2 and self.gameBoard[2][2] == self.player2 and
               self.gameBoard[3][1] == self.player2 and self.gameBoard[4][0] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][5] == self.player2 and self.gameBoard[1][4] == self.player2 and
               self.gameBoard[2][3] == self.player2 and self.gameBoard[3][2] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][4] == self.player2 and self.gameBoard[2][3] == self.player2 and
               self.gameBoard[3][2] == self.player2 and self.gameBoard[4][1] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][3] == self.player2 and self.gameBoard[3][2] == self.player2 and
               self.gameBoard[4][1] == self.player2 and self.gameBoard[5][0] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][6] == self.player2 and self.gameBoard[1][5] == self.player2 and
               self.gameBoard[2][4] == self.player2 and self.gameBoard[3][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][5] == self.player2 and self.gameBoard[2][4] == self.player2 and
               self.gameBoard[3][3] == self.player2 and self.gameBoard[4][2] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][4] == self.player2 and self.gameBoard[3][3] == self.player2 and
               self.gameBoard[4][2] == self.player2 and self.gameBoard[5][1] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][6] == self.player2 and self.gameBoard[2][5] == self.player2 and
               self.gameBoard[3][4] == self.player2 and self.gameBoard[4][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][5] == self.player2 and self.gameBoard[3][4] == self.player2 and
               self.gameBoard[4][3] == self.player2 and self.gameBoard[5][2] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][6] == self.player2 and self.gameBoard[3][5] == self.player2 and
               self.gameBoard[4][4] == self.player2 and self.gameBoard[5][3] == self.player2):
            self.player2score += 1

    def countScoreDepthLimit(self): #for evaluation
        self.player1score = 0;
        self.player2score = 0;

        # Checking horizontally
        for row in self.gameBoard:
            # Checking for player 1
            if row[0:4] == [self.player1]*4:
                self.player1score += 1
            if row[1:5] == [self.player1]*4:
                self.player1score += 1
            if row[2:6] == [self.player1]*4:
                self.player1score += 1
            if row[3:7] == [self.player1]*4:
                self.player1score += 1

            if row[0:3] == [self.player1]*3:
                self.player1score += 0.75
            if row[1:4] == [self.player1]*3:
                self.player1score += 0.75
            if row[2:5] == [self.player1]*3:
                self.player1score += 0.75
            if row[3:6] == [self.player1]*3:
                self.player1score += 0.75

            # Checking for player 2
            if row[0:4] == [self.player2]*4:
                self.player2score += 1
            if row[1:5] == [self.player2]*4:
                self.player2score += 1
            if row[2:6] == [self.player2]*4:
                self.player2score += 1
            if row[3:7] == [self.player2]*4:
                self.player2score += 1

            if row[0:3] == [self.player2]*3:
                self.player2score += 0.75
            if row[1:4] == [self.player2]*3:
                self.player2score += 0.75
            if row[2:4] == [self.player2]*3:
                self.player2score += 0.75
            if row[3:5] == [self.player2]*3:
                self.player2score += 0.75

        # Checking vertically
        for j in range(7):
            # Checking for player 1
            if (self.gameBoard[0][j] == self.player1 and self.gameBoard[1][j] == self.player1 and
                   self.gameBoard[2][j] == self.player1 and self.gameBoard[3][j] == self.player1):
                self.player1score += 1
            if (self.gameBoard[1][j] == self.player1 and self.gameBoard[2][j] == self.player1 and
                   self.gameBoard[3][j] == self.player1 and self.gameBoard[4][j] == self.player1):
                self.player1score += 1
            if (self.gameBoard[2][j] == self.player1 and self.gameBoard[3][j] == self.player1 and
                   self.gameBoard[4][j] == self.player1 and self.gameBoard[5][j] == self.player1):
                self.player1score += 1

            if (self.gameBoard[0][j] == self.player1 and self.gameBoard[1][j] == self.player1 and
                   self.gameBoard[2][j] == self.player1):
                self.player1score += 0.75
            if (self.gameBoard[1][j] == self.player1 and self.gameBoard[2][j] == self.player1 and
                   self.gameBoard[3][j] == self.player1):
                self.player1score += 0.75
            if (self.gameBoard[2][j] == self.player1 and self.gameBoard[3][j] == self.player1 and
                   self.gameBoard[4][j] == self.player1):
                self.player1score += 0.75
            if (self.gameBoard[3][j] == self.player1 and self.gameBoard[4][j] == self.player1 and
                   self.gameBoard[5][j] == self.player1):
                self.player1score += 0.75
            # Checking for player 2
            if (self.gameBoard[0][j] == self.player2 and self.gameBoard[1][j] == self.player2 and
                   self.gameBoard[2][j] == self.player2 and self.gameBoard[3][j] == self.player2):
                self.player2score += 1
            if (self.gameBoard[1][j] == self.player2 and self.gameBoard[2][j] == self.player2 and
                   self.gameBoard[3][j] == self.player2 and self.gameBoard[4][j] == self.player2):
                self.player2score += 1
            if (self.gameBoard[2][j] == self.player2 and self.gameBoard[3][j] == self.player2 and
                   self.gameBoard[4][j] == self.player2 and self.gameBoard[5][j] == self.player2):
                self.player2score += 1

            if (self.gameBoard[0][j] == self.player2 and self.gameBoard[1][j] == self.player2 and
                   self.gameBoard[2][j] == self.player2):
                self.player2score += 0.75
            if (self.gameBoard[1][j] == self.player2 and self.gameBoard[2][j] == self.player2 and
                   self.gameBoard[3][j] == self.player2):
                self.player2score += 0.75
            if (self.gameBoard[2][j] == self.player2 and self.gameBoard[3][j] == self.player2 and
                   self.gameBoard[4][j] == self.player2):
                self.player2score += 0.75
            if (self.gameBoard[3][j] == self.player2 and self.gameBoard[4][j] == self.player2 and
                   self.gameBoard[5][j] == self.player2):
                self.player2score += 0.75

        # Checking diagonally

        # Checking for player 1
        if (self.gameBoard[2][0] == self.player1 and self.gameBoard[3][1] == self.player1 and
               self.gameBoard[4][2] == self.player1 and self.gameBoard[5][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][0] == self.player1 and self.gameBoard[2][1] == self.player1 and
               self.gameBoard[3][2] == self.player1 and self.gameBoard[4][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][1] == self.player1 and self.gameBoard[3][2] == self.player1 and
               self.gameBoard[4][3] == self.player1 and self.gameBoard[5][4] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][0] == self.player1 and self.gameBoard[1][1] == self.player1 and
               self.gameBoard[2][2] == self.player1 and self.gameBoard[3][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][1] == self.player1 and self.gameBoard[2][2] == self.player1 and
               self.gameBoard[3][3] == self.player1 and self.gameBoard[4][4] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][2] == self.player1 and self.gameBoard[3][3] == self.player1 and
               self.gameBoard[4][4] == self.player1 and self.gameBoard[5][5] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][1] == self.player1 and self.gameBoard[1][2] == self.player1 and
               self.gameBoard[2][3] == self.player1 and self.gameBoard[3][4] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][2] == self.player1 and self.gameBoard[2][3] == self.player1 and
               self.gameBoard[3][4] == self.player1 and self.gameBoard[4][5] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][3] == self.player1 and self.gameBoard[3][4] == self.player1 and
               self.gameBoard[4][5] == self.player1 and self.gameBoard[5][6] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][2] == self.player1 and self.gameBoard[1][3] == self.player1 and
               self.gameBoard[2][4] == self.player1 and self.gameBoard[3][5] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][3] == self.player1 and self.gameBoard[2][4] == self.player1 and
               self.gameBoard[3][5] == self.player1 and self.gameBoard[4][6] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][3] == self.player1 and self.gameBoard[1][4] == self.player1 and
               self.gameBoard[2][5] == self.player1 and self.gameBoard[3][6] == self.player1):
            self.player1score += 1

        if (self.gameBoard[0][3] == self.player1 and self.gameBoard[1][2] == self.player1 and
               self.gameBoard[2][1] == self.player1 and self.gameBoard[3][0] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][4] == self.player1 and self.gameBoard[1][3] == self.player1 and
               self.gameBoard[2][2] == self.player1 and self.gameBoard[3][1] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][3] == self.player1 and self.gameBoard[2][2] == self.player1 and
               self.gameBoard[3][1] == self.player1 and self.gameBoard[4][0] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][5] == self.player1 and self.gameBoard[1][4] == self.player1 and
               self.gameBoard[2][3] == self.player1 and self.gameBoard[3][2] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][4] == self.player1 and self.gameBoard[2][3] == self.player1 and
               self.gameBoard[3][2] == self.player1 and self.gameBoard[4][1] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][3] == self.player1 and self.gameBoard[3][2] == self.player1 and
               self.gameBoard[4][1] == self.player1 and self.gameBoard[5][0] == self.player1):
            self.player1score += 1
        if (self.gameBoard[0][6] == self.player1 and self.gameBoard[1][5] == self.player1 and
               self.gameBoard[2][4] == self.player1 and self.gameBoard[3][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][5] == self.player1 and self.gameBoard[2][4] == self.player1 and
               self.gameBoard[3][3] == self.player1 and self.gameBoard[4][2] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][4] == self.player1 and self.gameBoard[3][3] == self.player1 and
               self.gameBoard[4][2] == self.player1 and self.gameBoard[5][1] == self.player1):
            self.player1score += 1
        if (self.gameBoard[1][6] == self.player1 and self.gameBoard[2][5] == self.player1 and
               self.gameBoard[3][4] == self.player1 and self.gameBoard[4][3] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][5] == self.player1 and self.gameBoard[3][4] == self.player1 and
               self.gameBoard[4][3] == self.player1 and self.gameBoard[5][2] == self.player1):
            self.player1score += 1
        if (self.gameBoard[2][6] == self.player1 and self.gameBoard[3][5] == self.player1 and
               self.gameBoard[4][4] == self.player1 and self.gameBoard[5][3] == self.player1):
            self.player1score += 1

        if (self.gameBoard[3][0] == self.player1 and self.gameBoard[4][1] == self.player1 and
               self.gameBoard[5][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][0] == self.player1 and self.gameBoard[3][1] == self.player1 and
               self.gameBoard[4][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][1] == self.player1 and self.gameBoard[4][2] == self.player1 and
                     self.gameBoard[5][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][0] == self.player1 and self.gameBoard[2][1] == self.player1 and
               self.gameBoard[3][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][1] == self.player1 and self.gameBoard[3][2] == self.player1 and
               self.gameBoard[4][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][2] == self.player1 and self.gameBoard[4][3] == self.player1 and
            self.gameBoard[5][4] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[0][0] == self.player1 and self.gameBoard[1][1] == self.player1 and
               self.gameBoard[2][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][1] == self.player1 and self.gameBoard[2][2] == self.player1 and
               self.gameBoard[3][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][2] == self.player1 and self.gameBoard[3][3] == self.player1 and
               self.gameBoard[4][4] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][3] == self.player1 and self.gameBoard[4][4] == self.player1 and
            self.gameBoard[5][5] == self.player1 ):
            self.player1score += 0.75
        if (self.gameBoard[0][1] == self.player1 and self.gameBoard[1][2] == self.player1 and
               self.gameBoard[2][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][2] == self.player1 and self.gameBoard[2][3] == self.player1 and
               self.gameBoard[3][4] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][3] == self.player1 and self.gameBoard[3][4] == self.player1 and
               self.gameBoard[4][5] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][4] == self.player1 and self.gameBoard[4][5] == self.player1 and
            self.gameBoard[5][6] == self.player1 ):
            self.player1score += 0.75
        if (self.gameBoard[0][2] == self.player1 and self.gameBoard[1][3] == self.player1 and
               self.gameBoard[2][4] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][3] == self.player1 and self.gameBoard[2][4] == self.player1 and
               self.gameBoard[3][5] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][4] == self.player1 and self.gameBoard[3][5] == self.player1 and
            self.gameBoard[4][6] == self.player1 ):
            self.player1score += 0.75
        if (self.gameBoard[0][3] == self.player1 and self.gameBoard[1][4] == self.player1 and
               self.gameBoard[2][5] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][4] == self.player1 and self.gameBoard[2][5] == self.player1 and
            self.gameBoard[3][6] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[0][4] == self.player1 and self.gameBoard[1][5] == self.player1 and
            self.gameBoard[2][6] == self.player1):
            self.player1score += 0.75

        if (self.gameBoard[0][2] == self.player1 and self.gameBoard[1][1] == self.player1 and
               self.gameBoard[2][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[0][3] == self.player1 and self.gameBoard[1][2] == self.player1 and
               self.gameBoard[2][1] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][2] == self.player1 and self.gameBoard[2][1] == self.player1 and
            self.gameBoard[3][0] == self.player1 ):
            self.player1score += 0.75
        if (self.gameBoard[0][4] == self.player1 and self.gameBoard[1][3] == self.player1 and
               self.gameBoard[2][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][3] == self.player1 and self.gameBoard[2][2] == self.player1 and
               self.gameBoard[3][1] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][2] == self.player1 and self.gameBoard[3][1] == self.player1 and
            self.gameBoard[4][0] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[0][5] == self.player1 and self.gameBoard[1][4] == self.player1 and
               self.gameBoard[2][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][4] == self.player1 and self.gameBoard[2][3] == self.player1 and
               self.gameBoard[3][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][3] == self.player1 and self.gameBoard[3][2] == self.player1 and
               self.gameBoard[4][1] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][2] == self.player1 and self.gameBoard[4][1] == self.player1 and
            self.gameBoard[5][0] == self.player1 ):
            self.player1score += 0.75
        if (self.gameBoard[0][6] == self.player1 and self.gameBoard[1][5] == self.player1 and
               self.gameBoard[2][4] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][5] == self.player1 and self.gameBoard[2][4] == self.player1 and
               self.gameBoard[3][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][4] == self.player1 and self.gameBoard[3][3] == self.player1 and
               self.gameBoard[4][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][3] == self.player1 and self.gameBoard[4][2] == self.player1 and
            self.gameBoard[5][1] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[1][6] == self.player1 and self.gameBoard[2][5] == self.player1 and
               self.gameBoard[3][4] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][5] == self.player1 and self.gameBoard[3][4] == self.player1 and
               self.gameBoard[4][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][4] == self.player1 and self.gameBoard[4][3] == self.player1 and
               self.gameBoard[5][2] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[2][6] == self.player1 and self.gameBoard[3][5] == self.player1 and
               self.gameBoard[4][4] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][5] == self.player1 and self.gameBoard[4][4] == self.player1 and
            self.gameBoard[5][3] == self.player1):
            self.player1score += 0.75
        if (self.gameBoard[3][6] == self.player1 and self.gameBoard[4][5] == self.player1 and
               self.gameBoard[5][4] == self.player1):
            self.player1score += 0.75

        # Checking for player 2
        if (self.gameBoard[2][0] == self.player2 and self.gameBoard[3][1] == self.player2 and
               self.gameBoard[4][2] == self.player2 and self.gameBoard[5][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][0] == self.player2 and self.gameBoard[2][1] == self.player2 and
               self.gameBoard[3][2] == self.player2 and self.gameBoard[4][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][1] == self.player2 and self.gameBoard[3][2] == self.player2 and
               self.gameBoard[4][3] == self.player2 and self.gameBoard[5][4] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][0] == self.player2 and self.gameBoard[1][1] == self.player2 and
               self.gameBoard[2][2] == self.player2 and self.gameBoard[3][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][1] == self.player2 and self.gameBoard[2][2] == self.player2 and
               self.gameBoard[3][3] == self.player2 and self.gameBoard[4][4] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][2] == self.player2 and self.gameBoard[3][3] == self.player2 and
               self.gameBoard[4][4] == self.player2 and self.gameBoard[5][5] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][1] == self.player2 and self.gameBoard[1][2] == self.player2 and
               self.gameBoard[2][3] == self.player2 and self.gameBoard[3][4] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][2] == self.player2 and self.gameBoard[2][3] == self.player2 and
               self.gameBoard[3][4] == self.player2 and self.gameBoard[4][5] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][3] == self.player2 and self.gameBoard[3][4] == self.player2 and
               self.gameBoard[4][5] == self.player2 and self.gameBoard[5][6] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][2] == self.player2 and self.gameBoard[1][3] == self.player2 and
               self.gameBoard[2][4] == self.player2 and self.gameBoard[3][5] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][3] == self.player2 and self.gameBoard[2][4] == self.player2 and
               self.gameBoard[3][5] == self.player2 and self.gameBoard[4][6] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][3] == self.player2 and self.gameBoard[1][4] == self.player2 and
               self.gameBoard[2][5] == self.player2 and self.gameBoard[3][6] == self.player2):
            self.player2score += 1

        if (self.gameBoard[0][3] == self.player2 and self.gameBoard[1][2] == self.player2 and
               self.gameBoard[2][1] == self.player2 and self.gameBoard[3][0] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][4] == self.player2 and self.gameBoard[1][3] == self.player2 and
               self.gameBoard[2][2] == self.player2 and self.gameBoard[3][1] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][3] == self.player2 and self.gameBoard[2][2] == self.player2 and
               self.gameBoard[3][1] == self.player2 and self.gameBoard[4][0] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][5] == self.player2 and self.gameBoard[1][4] == self.player2 and
               self.gameBoard[2][3] == self.player2 and self.gameBoard[3][2] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][4] == self.player2 and self.gameBoard[2][3] == self.player2 and
               self.gameBoard[3][2] == self.player2 and self.gameBoard[4][1] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][3] == self.player2 and self.gameBoard[3][2] == self.player2 and
               self.gameBoard[4][1] == self.player2 and self.gameBoard[5][0] == self.player2):
            self.player2score += 1
        if (self.gameBoard[0][6] == self.player2 and self.gameBoard[1][5] == self.player2 and
               self.gameBoard[2][4] == self.player2 and self.gameBoard[3][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][5] == self.player2 and self.gameBoard[2][4] == self.player2 and
               self.gameBoard[3][3] == self.player2 and self.gameBoard[4][2] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][4] == self.player2 and self.gameBoard[3][3] == self.player2 and
               self.gameBoard[4][2] == self.player2 and self.gameBoard[5][1] == self.player2):
            self.player2score += 1
        if (self.gameBoard[1][6] == self.player2 and self.gameBoard[2][5] == self.player2 and
               self.gameBoard[3][4] == self.player2 and self.gameBoard[4][3] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][5] == self.player2 and self.gameBoard[3][4] == self.player2 and
               self.gameBoard[4][3] == self.player2 and self.gameBoard[5][2] == self.player2):
            self.player2score += 1
        if (self.gameBoard[2][6] == self.player2 and self.gameBoard[3][5] == self.player2 and
               self.gameBoard[4][4] == self.player2 and self.gameBoard[5][3] == self.player2):
            self.player2score += 1

        if (self.gameBoard[3][0] == self.player2 and self.gameBoard[4][1] == self.player2 and
               self.gameBoard[5][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][0] == self.player2 and self.gameBoard[3][1] == self.player2 and
               self.gameBoard[4][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][1] == self.player2 and self.gameBoard[4][2] == self.player2 and
                     self.gameBoard[5][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][0] == self.player2 and self.gameBoard[2][1] == self.player2 and
               self.gameBoard[3][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][1] == self.player2 and self.gameBoard[3][2] == self.player2 and
               self.gameBoard[4][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][2] == self.player2 and self.gameBoard[4][3] == self.player2 and
            self.gameBoard[5][4] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][0] == self.player2 and self.gameBoard[1][1] == self.player2 and
               self.gameBoard[2][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][1] == self.player2 and self.gameBoard[2][2] == self.player2 and
               self.gameBoard[3][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][2] == self.player2 and self.gameBoard[3][3] == self.player2 and
               self.gameBoard[4][4] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][3] == self.player2 and self.gameBoard[4][4] == self.player2 and
            self.gameBoard[5][5] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][1] == self.player2 and self.gameBoard[1][2] == self.player2 and
               self.gameBoard[2][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][2] == self.player2 and self.gameBoard[2][3] == self.player2 and
               self.gameBoard[3][4] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][3] == self.player2 and self.gameBoard[3][4] == self.player2 and
               self.gameBoard[4][5] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][4] == self.player2 and self.gameBoard[4][5] == self.player2 and
            self.gameBoard[5][6] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][2] == self.player2 and self.gameBoard[1][3] == self.player2 and
               self.gameBoard[2][4] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][3] == self.player2 and self.gameBoard[2][4] == self.player2 and
               self.gameBoard[3][5] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][4] == self.player2 and self.gameBoard[3][5] == self.player2 and
            self.gameBoard[4][6] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][3] == self.player2 and self.gameBoard[1][4] == self.player2 and
               self.gameBoard[2][5] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][4] == self.player2 and self.gameBoard[2][5] == self.player2 and
            self.gameBoard[3][6] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][4] == self.player2 and self.gameBoard[1][5] == self.player2 and
            self.gameBoard[2][6] == self.player2):
            self.player2score += 0.75

        if (self.gameBoard[0][2] == self.player2 and self.gameBoard[1][1] == self.player2 and
               self.gameBoard[2][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][3] == self.player2 and self.gameBoard[1][2] == self.player2 and
               self.gameBoard[2][1] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][2] == self.player2 and self.gameBoard[2][1] == self.player2 and
            self.gameBoard[3][0] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][4] == self.player2 and self.gameBoard[1][3] == self.player2 and
               self.gameBoard[2][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][3] == self.player2 and self.gameBoard[2][2] == self.player2 and
               self.gameBoard[3][1] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][2] == self.player2 and self.gameBoard[3][1] == self.player2 and
            self.gameBoard[4][0] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][5] == self.player2 and self.gameBoard[1][4] == self.player2 and
               self.gameBoard[2][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][4] == self.player2 and self.gameBoard[2][3] == self.player2 and
               self.gameBoard[3][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][3] == self.player2 and self.gameBoard[3][2] == self.player2 and
               self.gameBoard[4][1] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][2] == self.player2 and self.gameBoard[4][1] == self.player2 and
            self.gameBoard[5][0] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[0][6] == self.player2 and self.gameBoard[1][5] == self.player2 and
               self.gameBoard[2][4] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][5] == self.player2 and self.gameBoard[2][4] == self.player2 and
               self.gameBoard[3][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][4] == self.player2 and self.gameBoard[3][3] == self.player2 and
               self.gameBoard[4][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][3] == self.player2 and self.gameBoard[4][2] == self.player2 and
            self.gameBoard[5][1] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[1][6] == self.player2 and self.gameBoard[2][5] == self.player2 and
               self.gameBoard[3][4] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][5] == self.player2 and self.gameBoard[3][4] == self.player2 and
               self.gameBoard[4][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][5] == self.player2 and self.gameBoard[3][4] == self.player2 and
               self.gameBoard[5][2] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[2][6] == self.player2 and self.gameBoard[3][5] == self.player2 and
               self.gameBoard[4][4] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][5] == self.player2 and self.gameBoard[4][4] == self.player2 and
            self.gameBoard[5][3] == self.player2):
            self.player2score += 0.75
        if (self.gameBoard[3][6] == self.player2 and self.gameBoard[4][5] == self.player2 and
               self.gameBoard[5][4] == self.player2):
            self.player2score += 0.75
