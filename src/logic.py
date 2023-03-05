from src.board import *
from src.state import *
from src.simpleai import *
from src.minimax_ai import *


def play_move(board, move, turn):
    current = board[move[0]]
    board[move[0]] = "-"
    if abs(move[0] - move[1]) > 9:
        mid = move[0] + int((move[1] - move[0])/2)
        board[mid] = "-"
    if turn == Turn.player2:
        if move[1] < 8:
            current = current.upper()
        board[move[1]] = current
    else:
        if move[1] > 56:
            current = current.upper()
        board[move[1]] = current


def change_turn(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def validate_move(player_input: str, board: list, turn):
    try:
        tokens = player_input.split()
        start, dest = int(tokens[0]), int(tokens[1])
    except Exception:
        return None
    move = [start, dest]
    state = State(board, turn, [])
    legal_moves = [el.move for el in state.get_states()]
    print(f'Available moves: {legal_moves}')
    if move in legal_moves:
        return move
    else:
        return None


