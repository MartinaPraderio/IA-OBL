from GameBoard import GameBoard
import numpy as np

board: GameBoard
board = GameBoard()

board.render()
board.grid = np.square(board.grid)
board.render()
print(np.sum(board.grid))

weights = [
  [1, 2, 3, 4],
  [2, 3, 4, 5],
  [3, 4, 5, 6],
  [4, 5, 6, 7]
]

print(weights[1][3])
print("caca",np.sqrt(np.sqrt(4)))
