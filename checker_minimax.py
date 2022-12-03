import numpy as np
from checker_helpers import *
import random

# A simple evaluation function that simply uses the current score.
def simple_evaluate(state):
    return score_in(state)

# # TODO
# # Implement a better evaluation function that outperforms the simple one.
# # Reference : https://digitalcommons.andrews.edu/cgi/viewcontent.cgi?article=1259&context=honors
# # Take H4, H6, H7 
# def better_evaluate(state):
#     player, board = state
#     evaluate = board[mancala_of(0)] - board[mancala_of(1)]*0.6
    
#     play_one_more = False
#     for move in pits_of(player):
#         if board[move] == (mancala_of(player) - move):
#             play_one_more = True 
    
#     if play_one_more:
#         evaluate += 0.9
    
#     return evaluate
    
# depth-limited minimax as covered in lecture
def minimax(state, max_depth=1, evaluate=simple_evaluate):
    # returns chosen child state, utility

    # base cases
    if game_over(state): return None, score_in(state)
    if max_depth == 0: return None, evaluate(state)

    # recursive case
    children = [perform_action(action, state) for action in valid_actions(state)]
    results = [minimax(child, max_depth-1, evaluate) for child in children]


    _, utilities = zip(*results)
    player, board = state
    if player == 0: action = np.argmax(utilities)
    if player == 1: action = np.argmin(utilities)
    return children[action], utilities[action]

# simply choosing valid actions uniformly at random
def baseline(state):
    return perform_action(random.choice(valid_actions(state)), state)

# runs a competitive game between two AIs:
# better_evaluation (as player 0) vs simple_evaluation (as player 1)
def compete(max_depth, verbose=True):
    state = initial_state()
    while not game_over(state):

        player, board = state
        if verbose: print(board)
        if verbose: print("--- %s's turn --->" % ["Better","Simple"][player])
        state, _ = minimax(state, max_depth, [simple_evaluate, simple_evaluate][player])
    
    score = score_in(state)
    player, board = state
    if verbose:
        print(board)
        print("Final score: %d" % score)
    
    return score


if __name__ == "__main__":
    
    score = compete(max_depth=4, verbose=True)

