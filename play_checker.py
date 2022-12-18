#***************************************************************************************/
#    Title: mancala_checker.py
#    Author: Katz, G.
#    Date: n.d.
#    Availability: hw2 from course CIS667
#***************************************************************************************/

from checker_helpers import *
from checker_minimax import minimax, simple_evaluate, baseline
from checker_nn import *

def get_user_action(state):
    actions = list(map(str, valid_actions(state)))
    player, board = state
    prompt = "Player %d, choose an action : \n" % (player)
    for i in range(len(actions)):
        prompt += "%d. %s \n" %(i, actions[i])
    while True:
        action = input(prompt)
        if int(action) in range(0,len(actions)): return valid_actions(state)[int(action)]
        print("Invalid action, try again.")

def human(state):
    action = get_user_action(state)
    state = perform_action(action, state)
    return state

def play_checker(size, player0_strategy, player1_strategy):
    state = initial_state(size)
    player_0_node_count = 0
    player_1_node_count = 0

    while not game_over(state):

        player, board = state
        print_board(board)
        if player == 0:
            # action = get_user_action(state)
            # state = perform_action(action, state)
            print("--- Player0's turn --->")
            if player0_strategy == minimax:
                state, _, count = player0_strategy(state)
                player_0_node_count += count
            elif player0_strategy == human or player0_strategy==baseline:
                state = player0_strategy(state)
                player_0_node_count += 1
            else: 
                state, _, count = minimax(state, evaluate=player0_strategy)
                player_0_node_count += count
            #state, _ = minimax(state, max_depth, simple_evaluate)
        else:
            print("--- Player1's turn --->")
            if player1_strategy == minimax:
                state, _, count = player1_strategy(state)
                player_1_node_count += count
            elif player1_strategy == human or player1_strategy==baseline:
                state = player1_strategy(state)
                player_1_node_count += 1
            else:
                state, _, count = minimax(state, evaluate=player1_strategy)
                player_1_node_count += count
    
    player, board = state
    winner = -1
    print_board(board.tolist())
    if is_tied(board):
        winner = -1
        print("Game over, it is tied.")
    else:
        winner = winner_of(board)
        print("Game over, player %d wins." % winner)

    player1_score, player2_score = final_score(state)
    return winner, player_0_node_count, player_1_node_count, player1_score, player2_score
if __name__ == "__main__":

    size_list = [4, 6, 8, 10, 12]
    size_prompt = "Choose problem size : \n"
    for i in range(len(size_list)):
        size_prompt += "%d. %s \n" %(i+1, size_list[i])

    size_select = int(input(size_prompt)) - 1
    size = size_list[size_select]

    strategy_dict = {"human": human, "baseline AI": baseline, "minimax": minimax, "nn": "nn"}
    config_list = list(strategy_dict.keys())
    player_strategy = {0:None, 1:None}
    for player in player_strategy.keys():
        config_prompt = "Choos player %d strategy : \n"%(player)
        for i in range(len(config_list)):
            config_prompt += "%d. %s \n" %(i+1, config_list[i])

        config_select = int(input(config_prompt)) - 1
        player_strategy[player] = strategy_dict[config_list[config_select]]

    if player_strategy[0] == "nn" or player_strategy[1] == "nn":
        net, curve, baseline_error = train_network_kyungrok(size)
        if player_strategy[0] == "nn":
            player_strategy[0] = net
        if player_strategy[1] == "nn":
            player_strategy[1] = net
        play_checker(size, player_strategy[0], player_strategy[1])

    

