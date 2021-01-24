from ai import *

board = []
for i in range(6):
    board.append([])
    for j in range(7):
        board[i].append(' ')

a = AI(board, 1, "x", 4)

state = [
    [" ", " ", " ", "x", "x", "x", "x"],
    [" ", " ", " ", "x", "x", " ", " "],
    [" ", " ", " ", "x", " ", "x", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
]

ai = AI(state, 1, "x", 4)

print(a.is_game_over(state))
