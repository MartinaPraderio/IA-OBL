from Agent import Agent
from GameBoard import GameBoard
import numpy as np
import random

WEIGHT_MATRIX = np.array([[1,  1,  2,    4], 
                          [1,  2,  8,    256],
                          [2,  16, 128,  512],
                          [32, 64, 1024, 2048]])
                 

class AgenteMiniMax(Agent):
    def __init__(self, player=1, max_depth: int=4):
        self.max_depth = max_depth
        self.player = player
        self.other_player = (player % 2) + 1
    
    
    def play(self, board:GameBoard):
        self.idx = 0
        accion, value = self.minimax(board, self.player, self.max_depth)
        return accion

    def heuristic_pos_corner(self, board: GameBoard):
        MAX_H = 50
        idx = np.unravel_index(np.argmax(board.grid), board.grid.shape)
        if idx == [3,3]:
            return MAX_H
        else: 
            return - MAX_H

    def heuristic_weighted_sum(self, board: GameBoard):
        return np.sum(board.grid * WEIGHT_MATRIX)

    def heuristic_utility(self, board: GameBoard):
        h_available_cell = len(board.get_available_cells()) 
        h_available_moves = len(board.get_available_moves())
        h_get_max = board.get_max_tile()
        h_weighted_sum = self.heuristic_weighted_sum(board)
        h_pos_corner = self.heuristic_pos_corner(board)
        heuristic = h_available_cell + h_available_moves + 0.05 * h_get_max + 0.0001 * h_weighted_sum + h_pos_corner
        return heuristic


    def minimax(self, board: GameBoard, player: int,  depth: int):    
        #Animación para que se vea lindo
        #print(animation[int(self.idx/300) % len(animation)], end="\r")
        #self.idx += 1   

        #TODO: Completar
        #Caso base
        # es final
        finished, win = board.is_end()
        if finished:
            #print("hola, mica no queria dejarlo")
            if win :
                return None, 1
            else:
                return None, -1
        if  depth == 0:
            eval_res = self.heuristic_utility(board)
            return None, eval_res 

        #Casos no base
        actions = board.get_available_moves()
        random.shuffle(actions)
        action_nodes = []
        if self.player == player:
            for action in actions:
                child_node = board.clone()
                child_node.move(action)
                action_nodes.append((action, child_node))
        else:
            for c in board.get_available_cells():
                for v in [2, 4]:
                    child_node = board.clone()
                    child_node.insert_tile(c, v)
                    action_nodes.append((None,child_node))

        value = 0
        chosen_action = None  

        if player != self.player: # mini
            minimax_list = [(action, self.minimax(child_node, self.player, depth-1)[1]) for (action, child_node) in action_nodes]
            chosen_action, value = min(minimax_list, key=lambda x: x[1])
            #Buscar acción que minimiza el valor  
            # print("min", chosen_action, value)

        else: #max (player == self.player)
            #Buscar acción que maximiza el valor 
            minimax_list = [(action, self.minimax(child_node, self.other_player, depth-1)[1]) for (action, child_node) in action_nodes]
            chosen_action, value = max(minimax_list, key=lambda x: x[1])  

            # print("max", chosen_action, value)


        return chosen_action, value
        