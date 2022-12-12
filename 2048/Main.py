from datetime import datetime
from GameBoard import GameBoard
from Agent import Agent
from Random_Agent import RandomAgent
from ExpectiMax_Agent import ExpectiMaxAgent

def check_win(board: GameBoard):
    return board.get_max_tile() >= 2048


int_to_string = ['UP', 'DOWN', 'LEFT', 'RIGHT']

if __name__ == '__main__':
    wins= 0
    loses= 0
    reached1024 = 0
    start_iterating = datetime.now()
    for i in range(20):
        agent: Agent
        board: GameBoard
        agent = ExpectiMaxAgent()
        board = GameBoard()
        done = False
        moves = 0
        #board.render()
        start = datetime.now()
        while not done:
            action = agent.play(board)
            # print('Next Action: "{}"'.format(
            #     int_to_string[action]), ',   Move: {}'.format(moves))
            done = board.play(action)
            done = done or check_win(board)
            # board.render()
            moves += 1

        print('\nTotal time: {}'.format(datetime.now() - start))
        print('\nTotal Moves: {}'.format(moves))
        print("games played", wins + loses)
        if check_win(board):
            print("WON THE GAME!!!!!!!!")
            wins += 1
        else:
            print("BOOOOOOOOOO!!!!!!!!!")
            loses += 1
            if (board.get_max_tile() == 1024):
                reached1024 += 1
    print("----------------------------")
    print("wins", wins, "times")
    print("loses", loses, "times")
    print("loses that reached 1024:", reached1024, "out of", loses)
    print("loses thet did not even reach 1024:", loses-reached1024, "out of", loses)
    print('\nTotal time: {}'.format(datetime.now() - start_iterating))
