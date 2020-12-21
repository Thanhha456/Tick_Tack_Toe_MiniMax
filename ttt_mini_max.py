"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
# import codeskulptor

# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

    if board.check_win() != None:
        winner = board.check_win()
        score = SCORES[winner]
        return score, (-1, -1)
    empty_sqr = board.get_empty_squares()
    score_list = []
    for sqr in empty_sqr:
        board_clone = board.clone()
        board_clone.move(sqr[0], sqr[1], player)
        move = mm_move(board_clone, provided.switch_player(player))[0]
        score_list.append((move, sqr))

    if player == provided.PLAYERX:
        score = max(score_list)
    elif player == provided.PLAYERO:
        score = min(score_list)
    return score

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
# print(mm_move(provided.TTTBoard(3, False, [[provided.PLAYERO, provided.EMPTY, provided.EMPTY], [provided.PLAYERX, provided.PLAYERO, provided.EMPTY], [provided.PLAYERX, provided.EMPTY, provided.EMPTY]]), provided.PLAYERO))
