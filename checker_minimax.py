#***************************************************************************************/
# Reference
#    Title: mancala_minimax.py
#    Author: Katz, G.
#    Date: n.d.
#    Availability: hw2 from course CIS667
#***************************************************************************************/

import numpy as np
from checker_helpers import *
import random
from checker_nn import *

# A simple evaluation function that simply uses the current score.
def simple_evaluate(state):
    return score_in(state)
    
# depth-limited minimax as covered in lecture
def minimax(state, max_depth=2, evaluate=simple_evaluate, node_count=1):
    # returns chosen child state, utility
    # base cases
    if game_over(state): return None, score_in(state), node_count
    if max_depth == 0:
        if evaluate != simple_evaluate:
            x = encode(state).unsqueeze(0) 
            return None, evaluate(x).detach().numpy(), node_count
        else:
            return None, evaluate(state), node_count

    # recursive case
    children = [perform_action(action, state) for action in valid_actions(state)]
    results = [minimax(child, max_depth-1, evaluate, node_count+1) for child in children]

    _, utilities, node_counts = zip(*results)
    player, board = state
    if player == 0: action = np.argmax(utilities)
    if player == 1: action = np.argmin(utilities)
    node_count = np.sum(node_counts)
    return children[action], utilities[action], node_count

# simply choosing valid actions uniformly at random
def baseline(state):
    return perform_action(random.choice(valid_actions(state)), state)

