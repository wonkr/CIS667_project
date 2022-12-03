# ********
# This file is individualized for NetID kwon01.
# ********
import numpy as np
import random

SIZE = 10
disk_count = {0:0, 1:0}
prev_player_action = {0:None, 1:None}
prev_prev_player_action = {0:None, 1:None}
prev_board = None
prev_prev_board = None

inloop = 0
prev_board = None

# DONE: implement initial_state()
# Return a (player, board) tuple representing the initial game state
# The initial player is player 0.
# board[r,c] is the content at position (r,c) of the board: "W", "B", "x", "X", "o" or "O"

# "o", "O" are a disk of player0
# "O" is a king disk
# "x", "X" are a disk of player1
# "X" is a king disk


def initial_state(size:int) -> tuple:
    global SIZE
    SIZE = size
    INITIAL_PLAYER = 0
    if SIZE == 4: 
        obstacle_counts = 1
    elif SIZE == 6:
        obstacle_counts = 2
    else:
        obstacle_counts = 3

    board = np.array([["W"]*SIZE]*SIZE)
    list_0_1 = np.array([ [ "W", "B"], [ "B", "W"] ])
    board = np.tile(list_0_1, (SIZE//2, SIZE//2)) 
    for i in range(SIZE//2-1):
        for j in range(SIZE):
            if board[i][j] == "B":
                board[i][j] = "o" 
                disk_count[0] += 1


    for i in range(SIZE//2+1,SIZE):
        for j in range(SIZE):
            if board[i][j] == "B":
                board[i][j] = "x" 
                disk_count[1] += 1

    
    black_positions = np.where(board=="B")
    black_position_coordinates = list(zip(black_positions[0], black_positions[1]))

    obstacles = random.sample(black_position_coordinates, obstacle_counts)
    
    for i, j in obstacles:
        board[i][j] = "■"

    return (INITIAL_PLAYER, board) # replace with your implementation

# DONE: implement game_over(state)
# Return True if the game is over, and False otherwise.
# The game is over once there is no valid_action.
# Your code should not modify the board list.
def game_over(state: tuple) -> bool:
    player, board = state
    actions = valid_actions(state)
    if actions == []: 
        return True
    else: 
        if len(actions) == 1 and is_king(board, actions[0]):
            return True
        if prev_board is not None and prev_prev_board is not None and prev_prev_player_action[player] is not None:
            if is_king(prev_board, prev_player_action[player]) and is_king(prev_prev_board, prev_prev_player_action[player]):
                inloop += 1
            else:
                inloop = 0
            if inloop > 10:
                return True
        return False

def is_king(board, action):
    is_king = True
    r, c, dr, dc = action
    if board[r][c] not in  ["O", "X"]:
        is_king = False
    return is_king

    
# DONE: implement valid_actions(state)
# state is a (player, board) tuple
# Return a list of all positions and valid move on the board where the current player can move disks.
# Your code should not modify the board list.
def valid_actions(state: tuple) -> list:
    valid_actions = []
    player, board = state
    if player == 0:
        disk = 'o'
        king_disk = 'O'
        possible_moves = [(+1, -1), (+1, +1)]
        possible_jumps = [(+2, -2), (+2, +2)]
    else:
        disk = 'x'
        king_disk = 'X'
        possible_moves = [(-1, -1), (-1, +1)]
        possible_jumps = [(-2, -2), (-2, +2)]

    king_possible_moves = [(+1, -1), (+1, +1),(-1, -1), (-1, +1)]
    king_possible_jumps = [(+2, -2), (+2, +2),(-2, -2), (-2, +2)]

    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == disk:
                for dr, dc in possible_moves:
                    if is_valid_move(board, r, c, dr, dc):
                        valid_actions.append((r,c,dr,dc))
                for dr, dc in possible_jumps:
                    if is_valid_jump(board, player, r, c, dr, dc):
                        valid_actions.append((r,c,dr,dc))
            if board[r][c] == king_disk:
                for dr, dc in king_possible_moves:
                    if is_valid_move(board, r, c, dr, dc):
                        valid_actions.append((r,c,dr,dc))
                for dr, dc in king_possible_jumps:
                    if is_valid_jump(board, player, r, c, dr, dc):
                        valid_actions.append((r,c,dr,dc))

    return valid_actions # replace with your implementation

def is_valid_move(board, r, c, dr, dc):
    new_r = r + dr
    new_c = c + dc
    if new_r > SIZE-1 or new_r < 0:
        return False
    if new_c > SIZE-1 or new_c < 0:
        return False
    if board[new_r][new_c] != 'B':
        return False
    else:
        return True

def is_valid_jump(board, player, r, c, dr, dc):
    if player == 0:
        opponents = ['x', 'X']
    else:
        opponents = ['o', 'O']
    new_r = r + dr
    new_c = c + dc
    interim_r = r + int(dr/2)
    interim_c = c + int(dc/2)
    if new_r > SIZE-1 or new_r < 0:
        return False
    if new_c > SIZE-1 or new_c < 0:
        return False
    if board[interim_r][interim_c] not in opponents:
        return False
    if board[new_r][new_c] != 'B':
        return False
    
    return True


# TODO: implement play_turn(move, board)

def play_turn(action: tuple, board: list) -> tuple:
    # Make a copy of the board before anything else
    # This is important for minimax, so that different nodes do not share the same mutable data
    # Your code should NOT modify the original input board or else bugs may show up elsewhere
    board = np.copy(board)
    r, c, dr, dc = action
    if board[r][c] == "o":
        cur_player = 0
        possible_jumps = [(+2, -2), (+2, +2)]
    elif board[r][c] == "O":
        cur_player = 0
        possible_jumps = [(+2, -2), (+2, +2), (-2, -2), (-2, +2)]
    elif board[r][c] == "x":
        cur_player = 1
        possible_jumps = [(-2, -2), (-2, +2)]
    elif board[r][c] == "X":
        cur_player = 1
        possible_jumps = [(-2, -2), (-2, +2), (+2, -2), (+2, +2)]

    new_player = cur_player^1

    if cur_player:
        kings_row = 0
    else:
        kings_row = SIZE-1

    board[r+dr][c+dc] = board[r][c]
    if r+dr == kings_row:
        board[r+dr][c+dc] = (board[r+dr][c+dc]).upper()

    board[r][c] = "B" 
    if abs(dr) == 2:
        board[r+(dr//2)][c+(dc//2)] = "B"
        disk_count[new_player] -= 1
    
        r, c = r+dr, c+dc
        for dr, dc in possible_jumps:
            if is_valid_jump(board, cur_player, r, c, dr, dc):
                action = (r,c,dr,dc)
                return play_turn(action, board)

    return (new_player, board) # replace with your implementation


def perform_action(action, state):
    player, board = state
    global prev_board
    global prev_prev_board
    prev_prev_board = prev_board
    prev_board = board
    prev_prev_player_action = prev_player_action
    prev_player_action[player] = action
    new_player, new_board = play_turn(action, board)
    return new_player, new_board

# DONE: implement score_in(state)
# state is a (player, board) tuple
# Return the score in the given state.
# The score is the number of player 0's disks, minus the number of player 1's disks.
def score_in(state: tuple) -> int:
    player, board = state
    player_0 = np.count_nonzero(board=='o') + np.count_nonzero(board=='O')
    player_1 = np.count_nonzero(board=='x') + np.count_nonzero(board=='X')


    score = player_0 - player_1
    return score 

# DONE: implement is_tied(board)
# Return True if the game is tied in the given board state, False otherwise.
# A game is tied if both players have no valid action.
def is_tied(board: list) -> bool:
    if valid_actions((0, board)) == [] and valid_actions((1, board)) == [] :
        return True
    else:
        return False # replace with your implementation

# DONE: implement winner_of(board)
# Return the winning player (either 0 or 1) in the given board state.
# The winner is the player with more disks in their board.
def winner_of(board: list) -> int:
    if disk_count[0] > disk_count[1]:
        return 0
    else:
        return 1 # replace with your implementation


def print_board(board: list) -> str:
    a = np.copy(board)
    a[a == 'B'] = '__'
    a[a == 'W'] = '__'

    for i in range(SIZE):
        print(a[i])