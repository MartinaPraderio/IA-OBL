from Agent import Agent
from GameBoard import GameBoard
import numpy as np

class ExpectiMaxAgent(Agent):
    def init(self):
        pass

    def play(self, board:GameBoard)->int:
        return self.expecti_max(board)[1]

    def heuristic_utility(self, board: GameBoard)->int:
        return 0 #Retorna un numero que calculamos en base al board con la heuristica q elijamos

    def expecti_max(self, board_state: GameBoard, player = True, max_depth = 4):
        if board_state.get_available_moves() == [] or board_state.get_max_tile() >= 2048 or max_depth == 0:
            return self.heuristic_utility(board_state)

        value = 0
        selected_action = None
        if player: # MAX
            max = 0
            for moveAction_board_successor in self.get_moves_successors(board_state): #(action, board)
                successor_value = self.expecti_max(moveAction_board_successor[1], not player, max_depth - 1)[0]
                if successor_value > max:
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
