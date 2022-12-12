from Agent import Agent
from GameBoard import GameBoard
import numpy as np

class ExpectiMaxAgent(Agent):
    def init(self):
        pass

    def play(self, board:GameBoard)->int:
        return self.expecti_max(board)[1]

    def heuristic_utility(self, board: GameBoard)->int:
        return (self.cell_values(board) * self.moves_available(board) / self.only_up_available(board) + self.reached_2048(board))
    # PRUEBAS:
        #PROFUNDIDAD 2
        #return self.smoothness_pro(board) + (self.monotonic_board_down(board) + self.biggest_tile_down(board))/10 #llego a 512 cinco veces, cinco 256, tres 128
        #return self.smoothness_pro(board) #256 dos veces
        #return self.cell_values(board) # 256
        #return self.cell_values(board) * (self.available_cells(board)+1)/3 # 256

        #PROFUNDIDAD 3
        #return self.smoothness_pro(board) # 256
        #return self.smoothness_pro(board) + self.monotonic_board_down(board) #64 con *
        #return self.smoothness_pro(board) + (self.monotonic_board_down(board) + self.biggest_tile_down(board))/4 # 256
        #return self.smoothness_pro(board) + (self.monotonic_board_down(board) + self.biggest_tile_down(board))/10 #512 cuatro veces dio esto, una vez 256
        #return self.smoothness_pro(board) + (self.monotonic_board_down(board) * self.biggest_tile_down(board))/10 #512 dos veces dio esto, tres veces 256
        #return self.smoothness_pro(board) + (self.monotonic_board_down(board) + self.biggest_tile_down(board))/15 #256 128
        #return self.smoothness_pro(board) + (self.monotonic_board_down(board) + self.biggest_tile_down(board))/12 #128, otra vez 512, otra vez 256
        #return self.smoothness_pro(board) + (self.monotonic_board_down(board) + self.biggest_tile_down(board))/8 #128, 512 otra vez
        #return self.monotonic_board_down(board) + self.biggest_tile_down(board) # 256
        #return self.monotonic_board_down(board) + self.biggest_tile_down(board) + self.biggest_tile_down_right_corner(board) #256
        #return self.monotonic_board_down(board)*2 + self.biggest_tile_down(board) + self.biggest_tile_down_right_corner(board) #512
        #return self.monotonic_board_down(board)*1.5 + self.biggest_tile_down(board) + self.biggest_tile_down_right_corner(board) #256
        #return self.monotonic_board_down(board)*2 + self.biggest_tile_down(board) + self.biggest_tile_down_right_corner(board)*1.5 #256
        #return (self.board_value(board) + (self.monotonic_board_down(board) * ((self.available_cells(board)+1)/2))) #
        #return self.cell_values(board)
        #return self.cell_values(board) * (self.available_cells(board)+0.1)
        # weights = [ # 1024, dos veces 512
        # [1, 2, 3, 4],
        # [2, 3, 4, 5],
        # [3, 4, 5, 7],
        # [4, 5, 7, 10]
        # ]
        # weights = [ # 1024 dos veces, 512 tres
        # [0.5, 1, 2, 4],
        # [1, 2, 4, 7],
        # [2, 4, 7, 11],
        # [4, 7, 11, 15]
        # ]
        # weights = [ # dos veces 1024, una vez 128, cuatro veces 512
        # [0.5, 1, 2, 3],
        # [1, 1.5, 4, 5],
        # [1.5, 4, 7, 11],
        # [4, 7, 11, 15]
        # ]
        # weights = [ # 512, 256
        # [0.5, 1, 2, 3],
        # [1, 2, 3, 4],
        # [2, 4, 7, 8],
        # [4, 7, 11, 15]
        # ]
        #return self.cell_values(board) * self.available_moves(board) * self.monotonic_board_down(board) / ((self.biggest_neighbours_difference(board)+0.1)**2)
        # weights = [ # 512
        # [0.5, 1, 2, 4],
        # [1, 2, 4, 7],
        # [2, 4, 7, 11],
        # [4, 7, 11, 15]
        # ]
        #Ejecuntandolo 20 veces:
            #return self.cell_values(board) * self.moves_available(board) + self.reached_2048(board) # 6/20
            #return self.cell_values(board) * self.moves_available(board) + self.reached_2048(board)  #9/20 con el moves devolviendo -10000 si hay 0
            #return (self.cell_values(board) * self.moves_available(board) + self.reached_2048(board)) #10/20
            #return (self.cell_values(board) * self.moves_available(board)/ (self.only_up_available(board) * 2) + self.reached_2048(board)) #4/20
            #return self.cell_values(board) * self.moves_available(board) + self.reached_1024(board) + self.reached_2048(board) # 7/20
            #return self.cell_values(board) * self.moves_available(board) + self.times_reached_1024(board) + self.reached_2048(board) #8/20
            #return (self.cell_values(board) * self.moves_available(board) / self.only_up_available(board) + self.reached_2048(board)) # 9/20 con -100000, 11/20 con -10000
            #return (self.cell_values(board) * self.moves_available_v2(board)/ self.only_up_available(board) + self.reached_2048(board)) # 3/19
            #return (self.cell_values(board) * self.moves_available(board) * self.biggest_tile_down(board)/ self.only_up_available(board) + self.reached_2048(board)) # 6 /20
            #return self.cell_values(board) # 730 moves, 1024, 887 moves, 1024 y 512
            #return self.smoothness_pro(board) * self.cell_values(board) * self.moves_available(board) # 512
            #return self.smoothness_pro(board) * self.cell_values(board) * self.moves_available(board) #256

        #PROFUNDIDAD 4
            #return self.available_cells(board) * self.monotonic_board_down(board) # best 1024 y 512 y 256
            #return self.board_smoothness(board)
            #return ((self.available_cells(board)+1)/2) * (self.monotonic_board_down(board)*1.5) * (self.biggest_tile_down(board) * 4)
                # con /16 en av cells llego a 512 y 256
                # con +1)/2, 1, 1, llego a 1024, 512
                # con +1)/2, 1.5, 1, llego a 512, 25
                # con +1)/2, 1.5, 4, llego a 1024, 256
            #return ((self.available_cells(board)+1)/2) * (self.monotonic_board_down(board)*1.5) * (self.biggest_tile_down(board) * 4)
            #return self.board_value(board) #llego a 512
            #return self.board_value(board) + (self.monotonic_board_down(board) * ((self.available_cells(board)+1)/2)) # llego a 1024 512 256
            #return self.board_value(board) + (self.monotonic_board_down(board) * ((self.available_cells(board)+1)/2) * self.biggest_tile_down(board)) # llego a 1024 256
            # return self.board_value(board) + ((self.monotonic_board_down(board)) * ((self.available_cells(board)+1)/2) * (self.biggest_tile_down(board)*2)) # llego a 256
            #return self.board_value(board) + ((self.monotonic_board_down(board) * 1.5) * ((self.available_cells(board)+1)/2) * (self.biggest_tile_down(board)*4)) # llego a 1024
            #return np.sqrt(self.board_value(board)) * (self.monotonic_board_down(board) * 1.5) * ((self.available_cells(board)+1)/2) * (self.biggest_tile_down(board)*4) # llego a 512
            #return  self.board_smoothness(board) * self.monotonic_board_down(board) * ((self.available_cells(board)+1)/2) # llego a 64, otra vez a 128
            #return  (self.board_smoothness(board)*(-1)) * self.monotonic_board_down(board) * ((self.available_cells(board)+1)/2) # llego a 256
            #return self.my_smoothness(board) # 512 256
            #return self.my_smoothness_v2(board) # 128
            #return self.vertical_smoothness(board) # 1024, en otra dio 512
            #return self.smoothness_pro(board) # 1024 y 512. Dio esto 2 veces
            #return self.smoothness_pro(board) * self.available_cells(board) # 512
            #return self.smoothness_pro(board) * self.board_value(board) # 512 256
            #return self.board_value(board) + (self.smoothness_pro(board) * ((self.available_cells(board)+1)/2)) #512 256
            #return self.smoothness_pro(board) * self.monotonic_board_down(board) # 256
            #return self.cell_values(board) * (self.available_cells(board)+0.1) * self.smoothness_pro(board) * self.monotonic_board_down(board) # 512
            # weights = [
            # [0.5, 1, 2, 3],
            # [1, 1.5, 4, 5],
            # [1.5, 4, 7, 11],
            # [4, 7, 11, 15]
            # ]
            #return self.smoothness_pro(board) + (self.monotonic_board_down(board) + self.biggest_tile_down(board))/10 # 512, en otra 256
            #return self.cell_values(board) * self.available_moves(board) # 1024
            # return self.cell_values(board) * self.moves_available(board) #512 256

        # PROFUNDIDAD 5 (Demora mucho!!)
            # return ((self.available_cells(board)+1)/2) * self.monotonic_board_down(board) * self.biggest_tile_down(board) # 1024 y 512 y 256 en 28 minutos
            # return (self.available_cells(board)+1) * self.monotonic_board_down(board) # llego a 1024 256 en 33 minutos
            #return self.smoothness_pro(board) # 256 128

    def moves_available(self, board: GameBoard):
        if len(board.get_available_moves()) == 0:
            return -10000
        return 1

    def moves_available_v2(self, board: GameBoard):
        moves = len(board.get_available_moves())
        if moves == 0:
            return -10000
        return np.sqrt(np.sqrt(moves))

    def only_up_available(self, board: GameBoard):
        moves = board.get_available_moves()
        if len(moves) == 1 and moves[0] == 0:
            return 2
        return 1

    def biggest_neighbours_difference(self, board):
        return board.grid[3][3] - board.grid[3][2]

    def cell_values(self, board):
        sum = 0
        weights = [ [ 0.004, 0.002, 0.001, 0.0005 ],
                    [ 0.008, 0.015, 0.03,  0.05   ],
                    [ 1,     0.5,   0.2,   0.1    ],
                    [ 2,     3.5,   8,     14     ]
                    ]
        for i in range(4):
            for j in range(4):
                sum += board.grid[i][j] * weights[i][j]
        return sum

    def cell_values_v2(self, board):
        sum = 0
        weights = [
        [0.5, 1, 1.5, 2],
        [1, 1.5, 3, 6],
        [2, 3, 4, 8],
        [6, 10, 18, 22]
        ]
        for i in range(4):
            for j in range(4):
                sum += board.grid[i][j] ** weights[i][j]
        return sum

    def reached_2048(self, board: GameBoard):
        if(board.get_max_tile() == 2048):
            return float('inf')
        return 0

    def reached_1024(self, board: GameBoard):
        if(board.get_max_tile() == 1024):
            return 14000
        return 0

    def times_reached_1024(self, board: GameBoard):
        times = 0
        for i in range(4):
            for j in range(4):
                if(board.grid[i][j] == 1024):
                    times += 1
        return times * 14000

    def board_value(self, board):
        return np.sum(np.square(board.grid))

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

    def my_smoothness(self, board): # v2
        smoothness_weight = 10
        smoothness = 0
        sqrt_grid = np.sqrt(board.grid)
        for i in range(4):
            for j in range(4):
                if (i + 1 <= 3):
                    smoothness += sqrt_grid[i + 1][j] - sqrt_grid[i][j]
                if (j + 1 <= 3):
                    smoothness += sqrt_grid[i][j] - sqrt_grid[i][j + 1]
        return smoothness

    def my_smoothness_v2(self, board):
        smoothness_weight = 3
        smoothness = 0
        sqrt_grid = np.sqrt(board.grid)
        for i in range(4):
            for j in range(4):
                if (i + 1 <= 3):
                    value = abs(sqrt_grid[i][j] - sqrt_grid[i + 1][j])
                    smoothness += value ** smoothness_weight
                if (j + 1 <= 3):
                    value = abs(sqrt_grid[i][j] - sqrt_grid[i][j + 1])
                    smoothness += value ** smoothness_weight
        return smoothness * (-1)

    def vertical_smoothness(self, board):
        smoothness_weight = 3
        smoothness = 0
        sqrt_grid = np.sqrt(board.grid)
        for i in range(4):
            for j in range(4):
                if (i + 1 <= 3):
                    value = abs(sqrt_grid[i][j] - sqrt_grid[i + 1][j])
                    smoothness += value ** smoothness_weight
        return 1/smoothness

    def smoothness_pro(self, board):
        smoothness_weight = 3
        smoothness = 0
        sqrt_grid = np.sqrt(board.grid)
        for i in range(4):
            for j in range(4):
                if (i + 1 <= 3):
                    value = abs(sqrt_grid[i][j] - sqrt_grid[i + 1][j])
                    smoothness += value ** smoothness_weight
                if (j + 1 <= 3):
                    value = abs(sqrt_grid[i][j] - sqrt_grid[i][j + 1])
                    smoothness += value ** smoothness_weight
        return 1/smoothness

    def available_cells(self, board):
        return len(board.get_available_cells())

    def monotonic_board_down(self, board): # retorna 2 si es monotonica creciente hacia abajo. De lo contrario, 1.
        for i in range(4):
            for j in range(4):
                if (i + 1 < 3):
                    if(board.grid[i][j] > board.grid[i + 1][j]):
                        return 1
        return 2

    def biggest_tile_down(self, board: GameBoard):
        max_tile = board.get_max_tile()
        for i in range(4):
            if(board.grid[3][i] == max_tile):
                return 2
        return 1

    def biggest_tile_down_right_corner(self, board: GameBoard):
        if(board.grid[3][3] == board.get_max_tile()):
            return 2
        return 1

    def available_moves(self, board: GameBoard):
        return len(board.get_available_moves())

    def expecti_max(self, board_state: GameBoard, player = True, max_depth = 3): # retorna (valor, accion)
        if board_state.get_available_moves() == [] or board_state.get_max_tile() >= 2048 or max_depth == 0:
            return self.heuristic_utility(board_state), None

        value = 0
        selected_action = None
        if player: # MAX
            max = float('-inf')
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

    def get_moves_successors(self, board: GameBoard): # retorna [ movimiento, board ]
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
