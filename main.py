# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Game(object):

    players = [None, None];
    playerNames = [None, None];
    board = None
    gameWinner= None
    gameFinished= False
    playerTurn = None

    #board dimensions
    m = 6
    n = 7

    def __init__(self):
        print("Welcome to Connect Four Game!")
        print("Will you play (1) Human to Human, (2) Human to Computer or, (3) Computer to Computer?")
        gameTypeChoice = int(input("Please type 1, 2 or 3: "))

        if(gameTypeChoice == 1 ):
            self.playerNames[0] = str(input("What is the name of player 1?"))
            self.playerNames[1] = str(input("What is the name of player 2?"))
            self.players[0] = HumanPlayer(self.playerNames[0], 'x')
            self.players[1] = HumanPlayer(self.playerNames[1], 'o')
        elif(gameTypeChoice == 2):
            difficulty = int(input("Please enter difficulty level. Type 1 , 2 or 3: "))
            if (difficulty != 1 or difficulty != 3 or difficulty != 3):
                difficulty = int(input("Please type a valid difficulty level. Type 1 , 2 or 3: "))
            self.players[0] = str(input("What is the name of human player?"))
            self.players[1] = "AI Player"
            humanStartsFirst = str(input("Will human start first? Type Y or N: "))
            if(humanStartsFirst == "Y"):
                self.players[0] = HumanPlayer(self.playerNames[0], 'x')
                self.players[1] = AIPlayer(self.playerNames[1], 'o', difficulty)
            else:
                self.players[0] = AIPlayer(self.playerNames[0], 'x', difficulty)
                self.players[1] = HumanPlayer(self.playerNames[1], 'o')

        elif(gameTypeChoice == 3):
            self.players[0] = "AI Player 1"
            self.players[1] = "AI Player 2"
            difficulty = int(input("Please enter a iq level for the first AI. Type 1 , 2 or 3: "))
            if (difficulty != 1 or difficulty != 3 or difficulty != 3):
                difficulty1 = int(input("Please type a valid iq level. Type 1 , 2 or 3: "))
            difficulty = int(input("Please enter a iq level for the first AI. Type 1 , 2 or 3: "))
            if (difficulty != 1 or difficulty != 3 or difficulty != 3):
                difficulty2 = int(input("Please type a valid iq level. Type 1 , 2 or 3: "))
            self.players[0] = AIPlayer(self.playerNames[0], 'x', difficulty1)
            self.players[1] = AIPlayer(self.playerNames[1], 'o', difficulty2)
        else:
            gameTypeChoice = str(input("Please type a valid input! 1, 2 or 3: "))

        """
        time.sleep(1)
        print("Game is starting...")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        """
    def initializeBoard(self):

        self.playerTurn = self.players[0]

        #a = [[0 for x in range(n)] for x in range(m)]

        board = [[' ', ' ', ' ', ' ', ' ', ' ',' '],
                 [' ', ' ', ' ', ' ', ' ', ' ',' '],
                 [' ', ' ', ' ', ' ', ' ', ' ',' '],
                 [' ', ' ', ' ', ' ', ' ', ' ',' '],
                 [' ', ' ', ' ', ' ', ' ', ' ',' '],
                 [' ', ' ', ' ', ' ', ' ', ' ',' ']]

    # Check if there exist a horizontal four starting from x,y
    def checkHorizontalFour(self, x, y):

        existsHorizFour=False
        count = 0

        character = self.board[x][y]
        for i in range(x,self.n):
            if(character == self.board[x][y]):
                count+=1
            else:
                break
        if(count>=4):
            existsHorizFour=True
            if (character == self.players[0].letter):
                self.gameWinner = self.players[0]
            else:
                self.gameWinner = self.gameWinner[1]
        return existsHorizFour

    # Check if there exist a vertical four starting from x,y
    def checkVerticalFour(self, x, y):

        existsVertFour = False
        count = 0

        character = self.board[x][y]
        for i in range(y, self.m):
            if (character == self.board[x][y]):
                count += 1
            else:
                break
        if (count >= 4):
            existsVertFour = True
            if(character == self.players[0].letter):
                self.gameWinner=self.players[0]
            else:
                self.gameWinner=self.gameWinner[1]


        return existsVertFour

    # Check if there exist a diagonal four starting from x,y
    def checkDiagonalFour(self, x, y):

        existsDiagFour = False
        count = 0
        winCount = 0
        #check x=y diagonal
        character = self.board[x][y]

        j = y
        for i in range(x, self.m):
            for j in range(y,self.n):
                if (self.board[i][j] == character):
                    count += 1
                else:
                    break

        if count >= 4:
            existsDiagFour=True
            winCount += 1
            diagDegree = 45 # indicating x=y has 45 degrees angle
            if self.players[0].letter == self.board[x][y]:
                self.winner = self.players[0]
            else:
                self.winner = self.players[1]
                
                
        # check x=-y diagonal
        count = 0
        j = y
        for i in range(x, -1, -1):
            for j in range(y, self.n):
                if (self.board[i][j] == character):
                    count += 1
                else:
                    break

        if count >= 4:
            existsDiagFour=True
            winCount += 1
            diagDegree = 135  # indicating x=-y has 135 degrees angle
            if self.players[0].letter == self.board[x][y]:
                self.winner = self.players[0]
            else:
                self.winner = self.players[1]

        if(winCount==2):
            diagDegree=45135 # diagonel four both exists in 45 and 135 degrees

        return existsDiagFour, diagDegree

    def checkFours(self):

        self.checkHorizontalFour()
        self.checkVerticalFour()
        self.checkDiagonalFour()

    def showState(self):
        print("_____________________________")
        for i in range(len(self.board)):
            #print("|\t", end="")
            for j in range(len(self.board[i])):
                print("| " +self.board[i][j], end=" ")
            print("|")
        print("-----------------------------")
        print("  1   2   3   4   5   6   7")

    def arbitrary(self):
        self.board=[]
        for i in range(6):
            self.board.append([])
            for j in range(7):
                self.board[i].append('1')

class HumanPlayer(object):

    type = None
    name = None
    letter = None

    def __init__(self, name, letter):
        self.name = name
        self.type ="Human"
        self.letter = letter



class AIPlayer(object):

    type = None
    name = None
    letter = None
    difficulty = None

    def __init__(self, name, letter, difficulty):
        self.difficulty = difficulty
        self.letter = letter
        self.name = name



def main():
    game = Game()
    game.initializeBoard()
    game.arbitrary()
    game.showState()


if __name__ == '__main__':
    main()


