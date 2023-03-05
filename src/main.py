from src.board import *
from src.state import *
from src.simpleai import *
from src.minimax_ai import *
from inputimeout import inputimeout, TimeoutOccurred

timeout_time = 10


def game_start():
    scoreboard = start_scoreboard()
    win_tracker = start_win_tracker()
    games_tracker = start_games_tracker()
    moves_tracker = start_moves_tracker()
    while True:
        print("Please select from the following, 1 -> self play, 2 -> simple ai, 3 -> minimax ai, "
              "4 -> reinforced learning ai, s -> print scoreboard, m -> past moves list, q -> quit")
        player_input = input()
        match player_input:
            case "q":
                break
            case "s":
                print_scoreboard(scoreboard)
            case "m":
                print(moves_tracker)
            case "1":
                player1_move = []
                player2_move = []
                player1 = input('Player 1 please enter your name:')
                player2 = input('Player 2 please enter your name:')
                player1 = player1.lower()
                player2 = player2.lower()
                try:
                    games_tracker[player1] += 1
                except Exception:
                    games_tracker[player1] = 1
                    scoreboard[player1] = 0
                    win_tracker[player1] = 0
                try:
                    games_tracker[player2] += 1
                except Exception:
                    games_tracker[player2] = 1
                    scoreboard[player2] = 0
                    win_tracker[player2] = 0
                player = 1
                board = new_board()
                while True:
                    print_board(board)
                    if end(board, player1, player2, scoreboard, win_tracker, games_tracker):
                        temp_tracker = []
                        temp_tracker += player1_move
                        temp_tracker += player2_move
                        moves_tracker += temp_tracker
                        print(temp_tracker)
                        break
                    try:
                        player_move = inputimeout(timeout=timeout_time)
                    except TimeoutOccurred:
                        print('You ran out of time, you lost')
                        if player == 1:
                            win_tracker[player2] += 1
                            scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                            scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                        else:
                            win_tracker[player1] += 1
                            scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                            scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                        break
                    if player == 1:
                        try:
                            move = validate_move(player_move, board, Turn.player1)
                            play_move(board, move, Turn.player1)
                            player1_move += move
                        except Exception:
                            print("Incorrect move")
                            win_tracker[player2] += 1
                            scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                            scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                            break
                    else:
                        try :
                            move = validate_move(player_move, board, Turn.player2)
                            play_move(board, move, Turn.player2)
                            player2_move += move
                        except Exception:
                            print("Incorrect move")
                            win_tracker[player1] += 1
                            scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                            scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                            break
                    player = change_turn(player)
            case "2":
                player1 = "player_1"
                player2 = "1"
                games_tracker[player1] += 1
                games_tracker[player2] += 1
                board = new_board()
                while True:
                    print_board(board)
                    game_over = end(board, player1, player2, scoreboard, win_tracker, games_tracker)
                    if game_over:
                        temp_tracker = []
                        temp_tracker += player1_move
                        temp_tracker += player2_move
                        moves_tracker += temp_tracker
                        break
                    try:
                        player_move = inputimeout(timeout=timeout_time)
                    except TimeoutOccurred:
                        print('You ran out of time, you lost')
                        win_tracker[player2] += 1
                        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                    try:
                        move = validate_move(player_move, board, Turn.player1)
                        play_move(board, move, Turn.player1)
                    except Exception:
                        print("Incorrect move")
                        win_tracker[player2] += 1
                        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                        break
                    ai_move = simple_move(board, Turn.player2)
                    play_move(board, ai_move, Turn.player2)
            case "3":
                player1 = "player_1"
                player2 = "2"
                games_tracker[player1] += 1
                games_tracker[player2] += 1
                board = new_board()
                while True:
                    print_board(board)
                    if end(board, player1, player2, scoreboard, win_tracker, games_tracker):
                        temp_tracker = []
                        temp_tracker += player1_move
                        temp_tracker += player2_move
                        moves_tracker += temp_tracker
                        break
                    try:
                        player_move = inputimeout(timeout=timeout_time)
                    except TimeoutOccurred:
                        print('You ran out of time, you lost')
                        win_tracker[player2] += 1
                        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]

                    try:
                        move = validate_move(player_move, board, Turn.player1)
                        play_move(board, move, Turn.player1)
                    except Exception:
                        print("Incorrect move")
                        win_tracker[player2] += 1
                        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                        break
                    ai_move = get_best_move(board, 2, Turn.player2, player1, player2, scoreboard, win_tracker, games_tracker)
                    play_move(board, ai_move, Turn.player2)
                break
            case "4":
                player1 = "player_1"
                player2 = "3"
                games_tracker[player1] += 1
                games_tracker[player2] += 1
                board = new_board()
                while True:
                    print_board(board)
                    if end(board, player1, player2, scoreboard, win_tracker, games_tracker):
                        temp_tracker = []
                        temp_tracker += player1_move
                        temp_tracker += player2_move
                        moves_tracker += temp_tracker
                        break
                    try:
                        player_move = inputimeout(timeout=timeout_time)
                    except TimeoutOccurred:
                        print('You ran out of time, you lost')
                        win_tracker[player2] += 1
                        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                    try:
                        move = validate_move(player_move, board, Turn.player1)
                        play_move(board, move, Turn.player1)
                    except Exception:
                        print("Incorrect move")
                        win_tracker[player2] += 1
                        scoreboard[player2] = win_tracker[player2] / games_tracker[player2]
                        scoreboard[player1] = win_tracker[player1] / games_tracker[player1]
                        break
                    # ai_move = get_best_move(board, 2, Turn.player2, player1, player2, scoreboard, win_tracker, games_tracker)
                    # play_move(board, ai_move, Turn.player2)
                break
            case "6":
                player1_move = []
                player2_move = []
                player1 = "local"
                player2 = "1"
                games_tracker[player1] += 1
                games_tracker[player2] += 1
                board = new_board()
                while True:
                    print_board(board)
                    print('\n')
                    winner = end(board, player1, player2, scoreboard, win_tracker, games_tracker)
                    if winner:
                        temp_tracker = []
                        temp_tracker.append([player1_move])
                        temp_tracker.append([player2_move])
                        temp_tracker.append([winner])
                        moves_tracker.append([temp_tracker])
                        print(temp_tracker)
                        break
                    ai_move = get_best_move(board, 9, Turn.player1, player1, player2, scoreboard, win_tracker, games_tracker)
                    play_move(board, ai_move, Turn.player1)
                    player1_move += [ai_move]
                    print_board(board)
                    print('\n')
                    ai_move = get_best_move(board, 8, Turn.player2, player1, player2, scoreboard, win_tracker, games_tracker)
                    play_move(board, ai_move, Turn.player2)
                    player2_move += [ai_move]

