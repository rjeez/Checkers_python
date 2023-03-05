from src.state import *


def simple_move(board: list, turn):
    state = State(board, turn, [])
    legal_moves = [el.move for el in state.get_states()]
    move = legal_moves[0]
    return move
