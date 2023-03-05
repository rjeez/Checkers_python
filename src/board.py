import chess


def new_board():
    board = ["a", "-", "a", "-", "a", "-", "a", "-",
             "-", "a", "-", "a", "-", "a", "-", "a",
             "a", "-", "a", "-", "a", "-", "a", "-",
             "-", "-", "-", "-", "-", "-", "-", "-",
             "-", "-", "-", "-", "-", "-", "-", "-",
             "-", "b", "-", "b", "-", "b", "-", "b",
             "b", "-", "b", "-", "b", "-", "b", "-",
             "-", "b", "-", "b", "-", "b", "-", "b"]
    return board


def print_board(board):
    for i in range(0, 57, 8):
        temp = []
        for j in range(8):
            temp += board[i+j]
        print(' '.join(temp))


def start_moves_tracker():
    moves_tracker = []
    return moves_tracker


def start_scoreboard():
    scoreboard = {'local': 0, '1': 0, '2': 0, '3': 0}
    return scoreboard


def start_win_tracker():
    win_tracker = {'local': 0, '1': 0, '2': 0, '3': 0}
    return win_tracker


def start_games_tracker():
    games_tracker = {'local': 0, '1': 0, '2': 0, '3': 0}
    return games_tracker


def print_scoreboard(scoreboard):
    sorted_scoreboard = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
    print(sorted_scoreboard)


def end(board, player1, player2, scoreboard, win_tracker, games_tracker):
    player1_counter = 0
    player2_counter = 0
    for i in range(64):
        if (board[i]).lower() == "a":
            player1_counter += 1
        elif (board[i]).lower() == "b":
            player2_counter += 1
    if player1_counter == 0 or (player1_counter <= 2 and player2_counter > 3):
        win_tracker[player2] += 1
        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
        return 2
    elif player2_counter == 0 or (player2_counter <= 2 and player1_counter > 3):
        scoreboard[player1] += 1
        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
        return 1
    else:
        return False


def check_end(board):
    player1_counter = 0
    player2_counter = 0
    for i in range(64):
        if (board[i]).lower() == "a":
            player1_counter += 1
        elif (board[i]).lower() == "b":
            player2_counter += 1
    if player1_counter == 0 or (player1_counter < 2 and player2_counter > 3):
        return 2
    elif player2_counter == 0 or (player2_counter < 2 and player1_counter > 3):
        return 1
    else:
        return False


def change_spots(board):
    board_spot = []
    for i in range(8):
        temp = []
        for j in range(8):
            match board[i*8 + j]:
                case 'a':
                    temp += 1
                case 'A':
                    temp += 3
                case 'b':
                    temp += 2
                case 'B':
                    temp += 4
        board_spot += temp
    return board_spot




'''
def init_gui_board(board):
    board.set_piece_at(chess.B8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.D8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.F8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.H8, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.A7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.C7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.E7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.G7, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.B6, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.D6, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.F6, chess.Piece.from_symbol('k'), chess.KING)
    board.set_piece_at(chess.H6, chess.Piece.from_symbol('k'), chess.KING)

    board.set_piece_at(chess.A3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.C3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.E3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.G3, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.B2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.D2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.F2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.H2, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.A1, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.C1, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.E1, chess.Piece.from_symbol('K'), chess.KING)
    board.set_piece_at(chess.G1, chess.Piece.from_symbol('K'), chess.KING)
    return board
'''