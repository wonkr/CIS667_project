from checker_helpers import *
from checker_minimax import minimax, simple_evaluate, baseline

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

    while not game_over(state):

        player, board = state
        print_board(board)
        if player == 0:
            # action = get_user_action(state)
            # state = perform_action(action, state)
            print("--- Player0's turn --->")
            if player0_strategy == minimax:
                state, _ = player0_strategy(state)
            else:
                state = player0_strategy(state)
            #state, _ = minimax(state, max_depth, simple_evaluate)
        else:
            print("--- Player1's turn --->")
            if player1_strategy == minimax:
                state, _ = player1_strategy(state)
            else:
                state = player1_strategy(state)
    
    player, board = state
    winner = -1
    print_board(board.tolist())
    if is_tied(board):
        winner = -1
        print("Game over, it is tied.")
    else:
        winner = winner_of(board)
        print("Game over, player %d wins." % winner)

    return winner

if __name__ == "__main__":

    size_list = [4, 6, 8, 10, 12]
    size_prompt = "Choose problem size : \n"
    for i in range(len(size_list)):
        size_prompt += "%d. %s \n" %(i+1, size_list[i])

    size_select = int(input(size_prompt)) - 1
    size = size_list[size_select]

    strategy_dict = {"human": human, "baseline AI": baseline, "minimax": minimax}
    strategy_list = list(strategy_dict.keys())
    player_strategy = {0:None, 1:None}
    for player in player_strategy.keys():
        strategy_prompt = "Choos player %d strategy : \n"%(player)
        for i in range(len(strategy_list)):
            strategy_prompt += "%d. %s \n" %(i+1, strategy_list[i])

        strategy_select = int(input(strategy_prompt)) - 1
        player_strategy[player] = strategy_dict[strategy_list[strategy_select]]

    play_checker(size, player_strategy[0], player_strategy[1])

    

