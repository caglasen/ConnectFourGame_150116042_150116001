from ai import *

board = []
for i in range(6):
    board.append([])
    for j in range(7):
        board[i].append(' ')


a = AI(board, 1, "x")


for i in a.get_possible_moves(a.move(a.board, 2, "o")):
    for j in i:
        print(j)
    print("\n")