import math


class AI:
    board = None
    colors = ["x", "o"]

    def __init__(self, board, heuristic, player, depth):
        self.board = [x[:] for x in board]
        self.heuristic = heuristic  # int value to determine heuristic value
        self.player = player  # this field indicates the sign of the player
        self.depth = depth

    def get_best_move(self):
        childs = self.get_possible_moves(self.board)
        best_val = -math.inf
        best_move = childs[0]

        for child in childs:
            child_val = self.minimax(False, self.depth - 1, child)
            if child_val > best_val:
                best_move = child
                best_val = child_val
        return best_move

    def minimax(self, is_max_player, depth, state):
        possibleMoves = self.get_possible_moves(state)

        if depth == 0 or len(possibleMoves) == 0:
            return self.h1(state)
        if is_max_player:
            value = -math.inf
            for child in possibleMoves:
                value = max(value, self.minimax(False, depth - 1, child))
            return value
        else:
            value = math.inf
            for child in possibleMoves:
                value = min(value, self.minimax(True, depth - 1, child))
            return value

    def get_possible_moves(self, state):  # this function returns the possible
        # moves of the given state as a list
        possible_moves = []
        for column in range(7):
            for i in range(6):
                if state[i][column] == ' ':
                    # once we find the first empty, we know it's a legal move
                    possible_moves.append(self.move(state, column, self.player.upper()))
                    break

        return possible_moves

    def move(self, state, column, color):  # this function makes the move and returns different object
        temp = [x[:] for x in state]
        for i in range(6):
            if temp[i][column] == ' ':
                temp[i][column] = color
                return temp

    def h1(self, state):  # first heuristic value is players
        return 0
