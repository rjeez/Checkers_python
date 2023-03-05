import enum
from copy import deepcopy
from src.steps import *


class Turn(enum.Enum):
    player1 = 0
    player2 = 1


class State(object):
    def __init__(self, board, turn, move):
        self.board = board
        self.turn = turn
        self.move = move

    def change_turn(self):
        if self.turn == Turn.player1:
            self.turn = Turn.player2
        else:
            self.turn = Turn.player1

    def is_terminal_state(self):
        b_counter = 0
        a_counter = 0
        for i in range(63):
            if self.board[i] == "b" or self.board[i] == "B":
                b_counter += 1
            elif self.board[i] == "a" or self.board[i] == "A":
                a_counter += 1

        if b_counter == 0 or a_counter == 0 or len(self.get_states()) == 0:
            return True
        elif b_counter > 3 and a_counter == 1 or a_counter > 3 and b_counter == 1:
            return True

    def get_states(self):
        if self.turn == Turn.player2:
            player = "b"
        else:
            player = "a"

        states = []
        for i in range(64):
            if self.board[i].lower() == player:
                get_legal_jumps(self.board, i, self.turn, states)

        if len(states) == 0:
            for i in range(64):
                if self.board[i].lower() == player:
                    get_legal_moves(self.board, i, self.turn, states)
        return states


""" 
-----------------------------------------------------------------------------------------------------------------
Getting all legal moves for 'get_states' function from State class
-----------------------------------------------------------------------------------------------------------------
"""


def get_legal_jumps(board: list, i: int, turn: Turn, states: list):

    if turn == Turn.player2:

        if board[i] == "B":
            jumps(board, i, turn, states, king_jumps(), 55, 64, "a")
        elif board[i] == "b":
            jumps(board, i, turn, states, player2_jumps(), 55, 64, "a")

    elif turn == Turn.player1:

        if board[i] == "A":
            jumps(board, i, turn, states, king_jumps(), 0, 8, "b")
        elif board[i] == "a":
            jumps(board, i, turn, states, player1_jumps(), 0, 8, "b")


def get_legal_moves(board: list, i: int, turn: Turn, states: list):

    if turn == Turn.player2:

        if board[i] == "B":
            moves(board, i, turn, states, king_steps(), 55, 64)
        elif board[i] == "b":
            moves(board, i, turn, states, player2_steps(), 55, 64)

    elif turn == Turn.player1:

        if board[i] == "A":
            moves(board, i, turn, states, king_steps(), 0, 8)
        elif board[i] == "a":
            moves(board, i, turn, states, player1_steps(), 0, 8)


def moves(board, i, turn, states, steps, lower_border, upper_border):
    """
    Fill the list 'states' with legal moves
    """

    nonlegal_positions = illegal_positions()
    for step in steps:
        index = step + i
        if index in nonlegal_positions:
            continue
        if 63 >= index >= 0 and board[index] == '-':
            board_copy = deepcopy(board)
            board_copy[index], board_copy[i] = board_copy[i], '-'
            if lower_border < i < upper_border:
                board_copy[index] = board_copy[index].upper()
            s = State(board_copy, turn, [i, index])
            states.append(s)


def jumps(board, i, turn, states, steps, lower_border, upper_border, value):
    """
    Fill the list 'states' with jump moves
    """

    nonlegal_positions = illegal_positions()
    for step in steps:
        index = step + i
        if index in nonlegal_positions:
            continue

        mid_i = int(step/2) + i
        if 63 >= index >= 0 and board[index] == '-' and board[mid_i].lower() == value:
            board_copy = deepcopy(board)
            board_copy[index], board_copy[i] = board_copy[i], '-'
            board_copy[mid_i] = '-'
            if lower_border < i < upper_border:
                board_copy[index] = board_copy[index].upper()
            states.append(State(board_copy, turn, [i, index]))
