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
    gameWinner = None
    gameFinished = False
    playerTurn = None
    round = 0

    # board dimensions
    m = 6
    n = 7

    def __init__(self):
        print("Welcome to Connect Four Game!")
        print("Will you play (1) Human to Human, (2) Human to Computer or, (3) Computer to Computer?")
        gameTypeChoice = int(input("Please type 1, 2 or 3: "))

        if (gameTypeChoice == 1):
            self.playerNames[0] = str(input("What is the name of player 1?"))
            self.playerNames[1] = str(input("What is the name of player 2?"))
            self.players[0] = HumanPlayer(self.playerNames[0], 'x')
            self.players[1] = HumanPlayer(self.playerNames[1], 'o')
        elif (gameTypeChoice == 2):
            difficulty = int(input("Please enter difficulty level. Type 1 , 2 or 3: "))
            if (difficulty != 1 or difficulty != 3 or difficulty != 3):
                difficulty = int(input("Please type a valid difficulty level. Type 1 , 2 or 3: "))
            self.players[0] = str(input("What is the name of human player?"))
            self.players[1] = "AI Player"
            humanStartsFirst = str(input("Will human start first? Type Y or N: "))
            if (humanStartsFirst == "Y"):
                self.players[0] = HumanPlayer(self.playerNames[0], 'x')
                self.players[1] = AIPlayer(self.playerNames[1], 'o', difficulty)
            else:
                self.players[0] = AIPlayer(self.playerNames[0], 'x', difficulty)
                self.players[1] = HumanPlayer(self.playerNames[1], 'o')

        elif (gameTypeChoice == 3):
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

        # a = [[0 for x in range(n)] for x in range(m)]

        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Check if there exist a horizontal four starting from x,y
    def checkHorizontalFour(self, x, y):

        existsHorizFour = False
        count = 0

        character = self.board[x][y]
        for i in range(y, self.n):
            if (character == self.board[x][i]):
                count += 1
            else:
                break
        if (count >= 4):
            existsHorizFour = True
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
        for i in range(x, self.m):
            if (character == self.board[i][y]):
                count += 1
            else:
                break
        if (count >= 4):
            existsVertFour = True
            if (character == self.players[0].letter):
                self.gameWinner = self.players[0]
            else:
                self.gameWinner = self.players[1]

        return existsVertFour

    # Check if there exist a diagonal four starting from x,y
    def checkDiagonalFour(self, x, y):

        existsDiagFour = False
        count = 0
        winCount = 0
        # check x=y diagonal
        character = self.board[x][y]
        diagDegree = -1

        j = y
        for i in range(x, self.m):
            for j in range(y, self.n):
                if (self.board[i][j] == character):
                    count += 1
                else:
                    break
            else:
                continue
            break

        if count >= 4:
            existsDiagFour = True
            winCount += 1
            diagDegree = 45  # indicating x=y has 45 degrees angle
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
            existsDiagFour = True
            winCount += 1
            diagDegree = 135  # indicating x=-y has 135 degrees angle
            if self.players[0].letter == self.board[x][y]:
                self.winner = self.players[0]
            else:
                self.winner = self.players[1]

        if (winCount == 2):
            diagDegree = 45135  # diagonel four both exists in 45 and 135 degrees

        return existsDiagFour, diagDegree

    """
    def checkFours(self):

        self.checkHorizontalFour()
        self.checkVerticalFour()
        self.checkDiagonalFour()
    """

    def showState(self):
        print("_____________________________")
        for i in range(len(self.board) - 1, -1, -1):
            # print("|\t", end="")
            for j in range(len(self.board[i])):
                print("| " + self.board[i][j], end=" ")
            print("|")
        print("-----------------------------")
        print("  1   2   3   4   5   6   7")

    def arbitrary(self):
        self.board = []
        for i in range(6):
            self.board.append([])
            for j in range(7):
                self.board[i].append('1')

    def makeAMove(self):
        currentPlayer = self.playerTurn

        if (self.checkGameIsOverWithDrawn() == True):
            print("Move is not valid. Error: Game ended with a drawn")
            return

        # If the player is a Human
        if (isinstance(currentPlayer, HumanPlayer)):
            playersColumnChoice = int(input("Enter a column number to make move: ")) - 1
            if (not (playersColumnChoice >= 0 and playersColumnChoice <= 6)):
                print("Move is not valid. Error: Choice is not valid")
                playersColumnChoice = -1
                while playersColumnChoice == -1:
                    playersColumnChoice = int(input("Enter a column number to make move: ")) - 1
                    if (playersColumnChoice >= 0 and playersColumnChoice <= 6):
                        break

        # If the player is an AI
        if (isinstance(currentPlayer, AIPlayer)):
            print()
            # BURAYA MINIMAXLI Bİ ŞEYLER GELECEK====================

        cellIndex = self.findTheEmptyCellInAColumn(playersColumnChoice)

        if (cellIndex == -1):
            print("Move is not valid. Error: Column is full")
            return

        self.board[cellIndex][playersColumnChoice] = currentPlayer.letter  # This is where we put the letter to board

        # Swap playerTurn with the other player for the next round
        if (self.playerTurn == self.players[0]):
            self.playerTurn = self.players[1]
        else:
            self.playerTurn = self.players[0]

        foursRowIndex = -1
        foursColumnIndex = -1

        for i in range(self.m):
            for j in range(self.n):
                if (self.board[i][j] != ' '):
                    a = self.checkVerticalFour(i, j)
                    b = self.checkHorizontalFour(i, j)
                    c, d = self.checkDiagonalFour(i, j)

                    if (a or b or c):
                        self.gameFinished = True
                        foursRowIndex = i
                        foursColumnIndex = j
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break

        self.round += 1

        if (foursRowIndex == -1 and foursColumnIndex == -1):
            self.showState()
        else:
            self.showTheWinnerFourState(foursRowIndex, foursColumnIndex, a, b, c)

        return foursRowIndex, foursColumnIndex

    def showTheWinnerFourState(self, row, col, vert, horiz, diagon):


        letter = self.board[row][col]

        foursCoordinates = [['', ''], ['', ''], ['', ''], ['', '']]

        foursCoordinates[0][0] = row
        foursCoordinates[0][1] = col

        if (self.checkVerticalFour(row, col)):
            for i in range(1, 4):
                foursCoordinates[i][0] = row + 1
                foursCoordinates[i][1] = col
                row += 1

        elif (self.checkHorizontalFour(row, col)):
            for i in range(1, 4):
                foursCoordinates[i][0] = row
                foursCoordinates[i][1] = col + 1
                col += 1

        elif (self.checkDiagonalFour(row, col)):
            for i in range(1, 4):
                foursCoordinates[i][0] = row + 1
                foursCoordinates[i][1] = col + 1
                row += 1
                col += 1

        for i in range(6):
            for j in range(7):
                for k in range(4):
                    if (i != foursCoordinates[k][0] and j != foursCoordinates[k][1]):
                        self.board[i][j] = ' '
        self.showState()
        print("The winner is ", self.gameWinner.name, " with the letter ", self.gameWinner.letter)
        return

    # If there is a drawn(if the board is already full) return true
    def checkGameIsOverWithDrawn(self):
        if (self.round > self.m * self.n):
            return True
        else:
            return False

    def findTheEmptyCellInAColumn(self, colNumber):
        for i in range(6):
            if self.board[i][colNumber] == ' ':
                return i
        return -1;


class HumanPlayer(object):
    type = None
    name = None
    letter = None

    def __init__(self, name, letter):
        self.name = name
        self.type = "Human"
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
    # game.arbitrary()
    game.showState()

    player1 = game.players[0]
    player2 = game.players[1]

    gameFinished = False

    while not gameFinished:
        game.makeAMove()
        gameFinished = game.gameFinished


if __name__ == '__main__':
    main()
