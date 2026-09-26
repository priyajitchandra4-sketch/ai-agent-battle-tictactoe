"""
heuristic.py - Heuristic Evaluation Functions for Non-Terminal Board States
"""

def heuristic_h1(board_obj, player):
    """
    Heuristic H1 (NEXUS): Positional Advantage + Line Potential
    - Combines tile value weighting (Center=4, Corners=2, Edges=1) with line threats.
    - Evaluates rows, columns, and diagonals for line strength.
    """
    opponent = 'O' if player == 'X' else 'X'
    board = board_obj.board
    score = 0

    # 1. Positional Weights
    weights = [
        [2, 1, 2],
        [1, 4, 1],
        [2, 1, 2]
    ]
    for r in range(3):
        for c in range(3):
            if board[r][c] == player:
                score += weights[r][c]
            elif board[r][c] == opponent:
                score -= weights[r][c]

    # 2. Line Threat Evaluation
    lines = _get_all_lines(board)
    for line in lines:
        p_count = line.count(player)
        o_count = line.count(opponent)
        empty_count = line.count(' ')

        if p_count == 3:
            score += 100
        elif p_count == 2 and empty_count == 1:
            score += 10
        elif p_count == 1 and empty_count == 2:
            score += 1

        if o_count == 3:
            score -= 100
        elif o_count == 2 and empty_count == 1:
            score -= 10
        elif o_count == 1 and empty_count == 2:
            score -= 1

    return score


def heuristic_h2(board_obj, player):
    """
    Heuristic H2 (TITAN): Direct Line Dominance & Immediate Threat Focus
    - Ignores positional tile bonuses.
    - Heavily rewards unblocked line potential and immediate threats/blocks.
    """
    opponent = 'O' if player == 'X' else 'X'
    board = board_obj.board
    score = 0

    lines = _get_all_lines(board)
    for line in lines:
        p_count = line.count(player)
        o_count = line.count(opponent)
        empty_count = line.count(' ')

        # Immediate winning line
        if p_count == 3:
            score += 100
        # Immediate threat (2 in line, 1 empty)
        elif p_count == 2 and empty_count == 1:
            score += 25
        # Single mark in unblocked line
        elif p_count == 1 and empty_count == 2:
            score += 5

        # Opponent winning line
        if o_count == 3:
            score -= 100
        # Opponent threat needing blocking
        elif o_count == 2 and empty_count == 1:
            score -= 25
        elif o_count == 1 and empty_count == 2:
            score -= 5

    return score


def _get_all_lines(board):
    """Helper method to extract all 8 winning lines (3 rows, 3 cols, 2 diagonals)."""
    lines = []
    # Rows and Columns
    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])
    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    return lines