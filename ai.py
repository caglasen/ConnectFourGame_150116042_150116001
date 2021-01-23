class AI:
    board = None
    colors = ["x", "o"]

    def __init__(self, board, heuristic, player):
        self.board = [x[:] for x in board]
        self.heuristic = heuristic  # int value to determine heuristic value
        self.player = player  # this field indicates the sign of the player

    def minimax(self, maximum, depth, state):
        possibleMoves = self.get_possible_moves(state)

        if depth == 0 or len(possibleMoves) == 0:
            return self.h1(state)
        if maximum:
            for move in possibleMoves:
                self.minimax(False, depth-1, move)

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

    def h1(self, state):
        return 0
