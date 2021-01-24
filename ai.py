import math


class AI:
    board = None
    colors = ["x", "o"]

    def __init__(self, board, heuristic, player, depth):
        self.board = [x[:] for x in board]
        self.heuristic = heuristic  # int value to determine heuristic value
        self.player = player  # this field indicates the sign of the player
        self.depth = depth
        if self.player.lower() == "o":
            self.opponent = "x"
        else:
            self.opponent = "o"

    def get_best_move(self):
        children = self.get_possible_moves(self.board, self.player)
        best_val = -math.inf
        best_move = children

        for child in children:
            child_val = self.minimax(False, self.depth - 1, child[0])
            if child_val > best_val:
                best_move = child
                best_val = child_val
        return best_move[1]

    def minimax(self, is_max_player, depth, state):
        if is_max_player:
            player = self.player
        else:
            player = self.opponent
        possibleMoves = self.get_possible_moves(state, player)

        if depth == 0 or len(possibleMoves) == 0:
            return self.h1(state)
        if is_max_player:
            value = -math.inf
            for child in possibleMoves:
                value = max(value, self.minimax(False, depth - 1, child[0]))
            return value
        else:
            value = math.inf
            for child in possibleMoves:
                value = min(value, self.minimax(True, depth - 1, child[0]))
            return value

    def get_possible_moves(self, state, player):  # this function returns the possible
        # moves of the given state as a list
        possible_moves = []
        for column in range(7):
            for i in range(6):
                if state[i][column] == ' ':
                    # once we find the first empty, we know it's a legal move
                    possible_moves.append([self.move(state, column, player), column])
                    break

        return possible_moves

    def move(self, state, column, player):  # this function makes the move and returns different object
        temp = [x[:] for x in state]
        for i in range(6):
            if temp[i][column] == ' ':
                temp[i][column] = player
                return temp

    def check_all(self, check_number, state, player):
        count = 0
        # for each piece in the board...
        for i in range(6):
            for j in range(7):
                # ...that is of the color we're looking for...
                if state[i][j].lower() == player.lower():
                    # check if a vertical streak starts at (i, j)
                    count += self.vertical_check(i, j, state, check_number)

                    # check if a horizontal four-in-a-row starts at (i, j)
                    count += self.horizontal_check(i, j, state, check_number)

                    # check if a diagonal (either way) four-in-a-row starts at (i, j)
                    count += self.diagonal_check(i, j, state, check_number)
        # return the sum of streaks of length 'streak'
        return count

    def horizontal_check(self, x, y, state, check_number):
        consecutiveCount = 0
        for i in range(x, 6):
            if state[i][y].lower() == state[x][y].lower():
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= check_number:
            return 1
        else:
            return 0

    def vertical_check(self, row, col, state, check_number):
        consecutiveCount = 0
        for i in range(row, 6):
            if state[i][col].lower() == state[row][col].lower():
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= check_number:
            return 1
        else:
            return 0

    def diagonal_check(self, x, y, state, check_number):
        total = 0
        # check for diagonals with positive slope
        consecutiveCount = 0
        j = y
        for i in range(x, 6):
            if j > 6:
                break
            elif state[i][j].lower() == state[x][y].lower():
                consecutiveCount += 1
            else:
                break
            j += 1  # increment column when row is incremented

        if consecutiveCount >= check_number:
            total += 1

        # check for diagonals with negative slope
        consecutiveCount = 0
        j = y
        for i in range(x, -1, -1):
            if j > 6:
                break
            elif state[i][j].lower() == state[x][y].lower():
                consecutiveCount += 1
            else:
                break
            j += 1  # increment column when row is incremented

        if consecutiveCount >= check_number:
            total += 1

        return total

    def h1(self, state):  # first heuristic value is calculated as 4 in a row * inf
        # + 3 in a row * 999 + 2 in a row * 99 - opponent  in a row * 9999 - 2 in a row * 99
        value = 0
        value = value + self.check_all(3, state, self.player) * 999  # add 999 for player's 3 in a row
        value = value + self.check_all(2, state, self.player) * 9  # add 99 for player's 2 in a row
        value = value - self.check_all(3, state, self.player) * 999  # subtract 9999 for opponent's 3 in a row
        value = value - self.check_all(2, state, self.player) * 9
        # subtract 99 for opponent's 2 in row

        if self.check_all(4, state, self.player):
            value = math.inf  # if player wins the game in this state then value is infinite

        return value
