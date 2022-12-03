from checker_helpers import *
from checker_minimax import *
from play_checker import *

def evaluate_checker(size):
    result = []
    for i in range(100):
        result.append(play_checker(size, baseline, minimax))
    return result.count(0), result.count(1), result.count(-1)

if __name__ == "__main__":
    experiment_result = {4:{0:0, 1:0, -1:0}, 6:{0:0, 1:0, -1:0}, 8:{0:0, 1:0, -1:0}, 10:{0:0, 1:0, -1:0}, 12:{0:0, 1:0, -1:0}}
    for size in experiment_result.keys():
        player0_win, player1_win, tie= evaluate_checker(size)
        experiment_result[size][0] = player0_win
        experiment_result[size][1] = player1_win
        experiment_result[size][-1] = tie

    print(experiment_result)

