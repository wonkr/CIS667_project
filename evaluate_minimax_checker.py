from checker_helpers import *
from checker_minimax import *
from play_checker import *
import matplotlib.pyplot as plt

def evaluate_minimax_checker(size):
    results = [play_checker(size, baseline, minimax) for i in range(100)]
    winner, player0_node_count, player1_node_count, player1_score, player2_score = zip(*results)
    return winner, player0_node_count, player1_node_count, player1_score, player2_score

if __name__ == "__main__":
    experiment_result = {4:{0:0, 1:0, -1:0}, 6:{0:0, 1:0, -1:0}, 8:{0:0, 1:0, -1:0}, 10:{0:0, 1:0, -1:0}}
    figures = []
    i = 1
    for size in experiment_result.keys():
        winner, player0_node_count, player1_node_count, player1_score, player2_score = evaluate_minimax_checker(size)
        experiment_result[size][0] = winner.count(0)
        experiment_result[size][1] = winner.count(1)
        experiment_result[size][-1] = winner.count(-1)
        
        f = plt.figure(i)
        plt.subplot(2,3, 1)
        plt.hist(player0_node_count, 'auto')
        plt.xlabel('Baseline Node Count', fontsize = 14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

        plt.subplot(2,3, 2)
        plt.hist(player1_node_count, 'auto')
        plt.xlabel('Minimax Node Count', fontsize = 14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

        plt.subplot(2,3, 4)
        plt.hist(player1_score, 'auto')
        plt.xlabel('Baselin Final scores', fontsize = 14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

        plt.subplot(2,3, 5)
        plt.hist(player2_score, 'auto')
        plt.xlabel('Minimax Final scores', fontsize = 14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

        plt.subplot(2,3, 6)
        ratio = [experiment_result[size][0]/size, experiment_result[size][1]/size, experiment_result[size][-1]/size]
        labels = ['baseline Win', 'minimax Win', 'tie']
        plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False)
        
        figures.append(f)
        i += 1
    plt.show()

    for size, result in experiment_result.items():
        print ("[ Size : %d ]"%size)
        print("- player 0 win : %d times"%result[0])
        print("- player 1 win : %d times"%result[1])
        print("- tie : %d times\n"%result[-1])

