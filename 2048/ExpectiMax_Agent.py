from Agent import Agent
from GameBoard import GameBoard
import numpy as np

class ExpectiMaxAgent(Agent):
    def init(self):
        pass

    def play(self, board:GameBoard)->int:
        return self.expecti_max(board)[1]

    def heuristic_utility(self, board: GameBoard)->int:
        #return self.available_cells(board) * self.monotonic_board_down(board) # best 1024 y 512 y 256
        #return self.board_smoothness(board)
        return ((self.available_cells(board)+1)/2) * (self.monotonic_board_down(board)*1.5) * (self.biggest_tile_down(board)) # con /16 en av cells llego a 512 y 256

    def available_cells(self, board):
        return len(board.get_available_cells())

    def monotonic_board_down(self, board): # retorna 2 si es monotona hacia abajo. De lo contrario, 1.
        for i in range(4):
            for j in range(4):
                if (i + 1 < 3):
                    if(board.grid[i][j] > board.grid[i + 1][j]):
                        return 1
                # if (j + 1 < 3): se puede usar para probar la monotonia en dos sentidos
                #     monotonic += abs(sqrt_grid[i][j] - sqrt_grid[i][j + 1])
        return 2

    def biggest_tile_down(self, board: GameBoard):
        max_tile = board.get_max_tile()
        for i in range(4):
            if(board.grid[3][i] == max_tile):
                return 2
        return 1

    def board_smoothness(self, board: GameBoard):
        smoothness_weight = 10
        smoothness = 0
        sqrt_grid = np.sqrt(board.grid)
        for i in range(4):
            for j in range(4):
                if (i + 1 <= 3):
                    smoothness += abs(sqrt_grid[i][j] - sqrt_grid[i + 1][j])
                if (j + 1 <= 3):
                    smoothness += abs(sqrt_grid[i][j] - sqrt_grid[i][j + 1])
        return (smoothness ** smoothness_weight) * (-1)

    def expecti_max(self, board_state: GameBoard, player = True, max_depth = 4): # retorna (valor, accion)
        if board_state.get_available_moves() == [] or board_state.get_max_tile() >= 2048 or max_depth == 0:
            return self.heuristic_utility(board_state), None

        value = 0
        selected_action = None
        if player: # MAX
            max = 0
            for moveAction_board_successor in self.get_moves_successors(board_state): #(action, board)
                successor_value = self.expecti_max(moveAction_board_successor[1], not player, max_depth - 1)[0]
                if successor_value >= max:
                    max = successor_value
                    selected_action = moveAction_board_successor[0]
            value = max
        else:
            sum = 0 # oponent EXPECTI
            for insertAction_board_successor in self.get_insert_successors(board_state):
                p = 0.9 if insertAction_board_successor[0] == 2 else 0.1
                u = self.expecti_max(insertAction_board_successor[1], not player, max_depth - 1)[0]
                sum += p * u
            value = sum

        return value, selected_action

    def get_moves_successors(self, board: GameBoard): # retorna [ movimiento (1, 2, 3 o 4), board ] #ver si los moves empiezan de 1 o de 0
        action_nodes = []
        for action in board.get_available_moves():
            child_node = board.clone()
            child_node.move(action)
            action_nodes.append((action, child_node))
        return action_nodes

    def get_insert_successors(self, board: GameBoard): # retorna [ numero_insertado (2 o 4), board ]
        action_nodes = []
        for action in  board.get_available_cells():
            child_node_2 = board.clone()
            child_node_4 = board.clone()
            child_node_2.insert_tile(action, 2)
            child_node_4.insert_tile(action, 4)
            action_nodes.append((2, child_node_2))
            action_nodes.append((4, child_node_4))
        return action_nodes
