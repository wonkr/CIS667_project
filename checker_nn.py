#***************************************************************************************/
# Reference
#    Title: ProjectExample.ipynb
#    Author: Katz, G.
#    Date: n.d.
#    Availability: https://colab.research.google.com/drive/1QF8IJHlZ597esIU-vmW7u9KARhyXIjOY
#***************************************************************************************/

import numpy as np
import matplotlib.pyplot as pt
import torch as tr
from checker_helpers import * 

# depth-limited minimax as covered in lecture
def minimax_for_datagen(state, max_depth=2):
    # base cases
    if game_over(state): return score_in(state), []
    if max_depth == 0: return score_in(state), []

    child_utilities = [
            minimax_for_datagen(perform_action(action, state), max_depth - 1)[0]
            for action in valid_actions(state)]

    player, board = state
    if player == 0: return max(child_utilities), child_utilities
    if player == 1: return min(child_utilities), child_utilities

# play a game with each player using depth-limited minimax
# break ties randomly
# return game states and final result
def random_game(size, max_depth):
    state = initial_state(size)
    states = [state]
    while not game_over(state):
        utility, child_utilities = minimax_for_datagen(state, max_depth)
        ties = (np.array(child_utilities) == utility)
        tie_index = np.flatnonzero(ties)
        actions = valid_actions(state)
        action = actions[np.random.choice(tie_index)]
        state = perform_action(action, state)
        states.append(state)
    result = score_in(state)
    return states, result

# Used to generate a training data set
# Combines results from many random games
def generate(num_examples, size, max_depth):
    all_states = []
    all_results = []
    num_games = 0
    while len(all_states) < num_examples:
        num_games += 1
        print(f"game {num_games}, {len(all_states)} of {num_examples} examples...")
        states, result = random_game(size, max_depth)
        all_states += states
        all_results += [result] * len(states)

    return all_states, all_results

# Used to convert a game state to a tensor encoding suitable for NN input
# Uses one-hot encoding at each grid position
def encode(state):
    symbols = np.array(["W", "B", "O", "o", "X", "x", "■", ]).reshape(-1,1,1)
    onehot = tr.from_numpy((symbols == state[1])).float()
    return onehot


# Defines a network with two fully-connected layers and tanh activation functions
class LinNet(tr.nn.Module):
    def __init__(self, size, hid_features, name="Kyungrok"):
        super(LinNet, self).__init__()
        self.student_name = name
        self.to_hidden1 = tr.nn.Linear(7*size**2, size**2)
        self.to_hidden2 = tr.nn.Linear(size**2, hid_features)
        self.to_output = tr.nn.Linear(hid_features, 1)
       
    def forward(self, x):
        # Kyungrok's configuration
        if self.student_name == "Kyungrok":
            h1 = tr.relu(self.to_hidden1(x.reshape(x.shape[0],-1)))
            h2 = tr.sigmoid(self.to_hidden2(h1))
            y = tr.tanh(self.to_output(h2))
        # Neda's configuration
        else:
            h1 = tr.tanh(self.to_hidden1(x.reshape(x.shape[0],-1)))
            h2 = tr.relu(self.to_hidden2(h1))
            y = tr.sigmoid(self.to_output(h2))
        return y

# Calculates the error on one training example
def example_error(net, example):
    state, utility = example
    x = encode(state).unsqueeze(0)
    print(x)
    y = net(x)
    e = (y - utility)**2
    return e

# Calculates the error on a batch of training examples
def batch_error(net, batch):
    states, utilities = batch
    u = utilities.reshape(-1,1).float()
    y = net(states)
    e = tr.sum((y - u)**2) / utilities.shape[0]
    return e

def train_network_kyungrok(size=8): 
    # Make the network and optimizer
    net = LinNet(size=size, hid_features=16, name="Kyungrok")
    optimizer = tr.optim.SGD(net.parameters(), lr=0.01)

    # Generate a lot of training/testing data
    training_examples = generate(num_examples = 1000, size=size, max_depth=3)
    testing_examples = generate(num_examples = 100, size=size, max_depth=3)

    # Baseline testing error: always predict constant
    _, utilities = testing_examples
    baseline_error =sum((u-0)**2 for u in utilities) / len(utilities)

    # Convert the states and their minimax utilities to tensors
    states, utilities = training_examples
    training_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    states, utilities = testing_examples
    testing_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    # Run the gradient descent iterations
    curves = [], []
    for epoch in range(50000):
    
        # zero out the gradients for the next backward pass
        optimizer.zero_grad()

        e = batch_error(net, training_batch)
        e.backward()
        training_error = e.item()

        with tr.no_grad():
            e = batch_error(net, testing_batch)
            testing_error = e.item()

        # take the next optimization step
        optimizer.step()    
        
        # print/save training progress
        if epoch % 1000 == 0:
            print("%d: %f, %f" % (epoch, training_error, testing_error))
        curves[0].append(training_error)
        curves[1].append(testing_error)

    return net, curves, baseline_error

def train_network_neda(size=8): 
    # Make the network and optimizer
    net = LinNet(size=size, hid_features=20, name="Neda")
    optimizer = tr.optim.SGD(net.parameters(), lr=0.01)

    # Generate a lot of training/testing data
    training_examples = generate(num_examples = 1000, size=size, max_depth=3)
    testing_examples = generate(num_examples = 100, size=size, max_depth=3)

    # Baseline testing error: always predict constant
    _, utilities = testing_examples
    baseline_error =sum((u-0)**2 for u in utilities) / len(utilities)

    # Convert the states and their minimax utilities to tensors
    states, utilities = training_examples
    training_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    states, utilities = testing_examples
    testing_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    # Run the gradient descent iterations
    curves = [], []
    for epoch in range(50000):
    
        # zero out the gradients for the next backward pass
        optimizer.zero_grad()

        e = batch_error(net, training_batch)
        e.backward()
        training_error = e.item()

        with tr.no_grad():
            e = batch_error(net, testing_batch)
            testing_error = e.item()

        # take the next optimization step
        optimizer.step()    
        
        # print/save training progress
        if epoch % 1000 == 0:
            print("%d: %f, %f" % (epoch, training_error, testing_error))
        curves[0].append(training_error)
        curves[1].append(testing_error)

    return net, curves, baseline_error

def draw_learning_curves(curves, baseline_error):
    # visualize learning curves on train/test data
    pt.plot(curves[0], 'b-')
    pt.plot(curves[1], 'r-')
    pt.plot([0, len(curves[1])], [baseline_error, baseline_error], 'g-')
    pt.plot()
    pt.legend(["Train","Test","Baseline"])
    pt.show()


