board = []

for x in range(1,8):
  board.append(["0"] * 8)

#define functions

def print_board(board):
  for row in board:
    print(" ".join(row))




#function calls
print_board(board)

