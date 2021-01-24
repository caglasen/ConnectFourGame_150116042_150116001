from ai import *

board = []
for i in range(6):
    board.append([])
    for j in range(7):
        board[i].append(' ')

a = AI(board, 1, "x", 4)

state = [
    [" ", "x", "x", " ", " ", " ", " "],
    [" ", " ", "o", "x", " ", " ", " "],
    [" ", " ", "x", "o", " ", " ", " "],
    [" ", " ", " ", " ", "o", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
]

print(a.check_all(2, state, "o"))
