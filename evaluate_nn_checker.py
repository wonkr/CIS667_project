from checker_helpers import *
from checker_minimax import *
from play_checker import *
import matplotlib.pyplot as plt

KYUNGROK = 1
NEDA = 2

def evaluate_nn_checker(config):
    if config == KYUNGROK:
        net, curve, baseline_error = train_network_kyungrok(8)
    if config == NEDA :
        net, curve, baseline_error = train_network_neda(8)
    draw_learning_curves(curve, baseline_error)
    results = [play_checker(8, baseline, net) for i in range(100)]
    winner, player0_node_count, player1_node_count, player1_score, player2_score = zip(*results)
    return winner, player0_node_count, player1_node_count, player1_score, player2_score

if __name__ == "__main__":
    config_list = ["Kyungrok's configuration", "Neda's configuration"]
    config_prompt = "Choose configuration settings for a neural network: \n"
    for i in range(len(config_list)):
        config_prompt += "%d. %s \n" %(i+1, config_list[i])

    config_select = int(input(config_prompt))

    experiment_result = {0:0, 1:0, -1:0}

    winner, player0_node_count, player1_node_count, player1_score, player2_score = evaluate_nn_checker(config_select)
    experiment_result[0] = winner.count(0)
    experiment_result[1] = winner.count(1)
    experiment_result[-1] = winner.count(-1)

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
    ratio = [experiment_result[0], experiment_result[1], experiment_result[-1]]
    labels = ['baseline Win', 'minimax Win', 'tie']
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False)
    
    plt.show()

    print("- player 0 win : %d times"%experiment_result[0])
    print("- player 1 win : %d times"%experiment_result[1])
    print("- tie : %d times\n"%experiment_result[-1])

