from src.state import *
from copy import deepcopy
from board import *
from src.logic import *


def get_best_move(board, depth, turn, player1, player2, scoreboard, win_tracker, games_tracker):
    print(minimax(board, depth, True, float('-inf'), float('inf'), turn, player1, player2, scoreboard, win_tracker, games_tracker)[1])
    return minimax(board, depth, True, float('-inf'), float('inf'), turn, player1, player2, scoreboard, win_tracker, games_tracker)[1]


def minimax(board, depth, maximizing_player, alpha, beta, turn, player1, player2, scoreboard, win_tracker, games_tracker):
    if depth == 0 or check_end(board):
        return evaluate(board), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        state = State(board, turn, [])
        legal_moves = [el.move for el in state.get_states()]
        for move in legal_moves:
            new_board = deepcopy(board)
            play_move(new_board, move, turn)
            evaluation = minimax(new_board, depth-1, False, alpha, beta, Turn.player1, player1, player2, scoreboard, win_tracker, games_tracker)[0]
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        state = State(board, turn, [])
        legal_moves = [el.move for el in state.get_states()]
        for move in legal_moves:
            new_board = deepcopy(board)
            play_move(new_board, move, turn)
            evaluation = minimax(new_board, depth-1, True, alpha, beta, Turn.player2, player1, player2, scoreboard, win_tracker, games_tracker)[0]
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate(board):
    # Simple evaluation function: count the number of pieces for each player and return the difference
    b_count = 0
    a_count = 0
    for i in range (64):
        if board[i] == 'b':
            b_count += 1
        elif board[i] == 'B':
            b_count += 2
        elif board[i] == 'a':
            a_count += 1
        elif board[i] == 'A':
            a_count += 2
    return b_count - a_count
