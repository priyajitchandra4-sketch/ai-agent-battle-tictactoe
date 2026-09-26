"""
minimax.py - Minimax Search with Alpha-Beta Pruning
"""

import math
import random
import time


class MinimaxSearch:
    """Implements Minimax algorithm with Alpha-Beta Pruning and telemetry."""

    def __init__(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def search(self, game_state, current_depth, max_depth, alpha, beta, is_maximizing, ai_player, heuristic_fn):
        self.nodes_evaluated += 1

        winner = game_state.check_winner()
        opponent = 'O' if ai_player == 'X' else 'X'

        # Terminal conditions or max search depth hit
        if winner == ai_player:
            return 1000 - current_depth  # Prefer faster wins
        if winner == opponent:
            return -1000 + current_depth # Delay unavoidable losses
        if game_state.is_draw():
            return 0
        if current_depth >= max_depth:
            return heuristic_fn(game_state, ai_player)

        valid_moves = game_state.get_valid_moves()

        if is_maximizing:
            max_eval = -math.inf
            for row, col in valid_moves:
                child_state = game_state.clone()
                child_state.make_move(row, col, ai_player)
                eval_score = self.search(child_state, current_depth + 1, max_depth,
                                         alpha, beta, False, ai_player, heuristic_fn)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    self.nodes_pruned += (len(valid_moves) - (valid_moves.index((row, col)) + 1))
                    break
            return max_eval
        else:
            min_eval = math.inf
            for row, col in valid_moves:
                child_state = game_state.clone()
                child_state.make_move(row, col, opponent)
                eval_score = self.search(child_state, current_depth + 1, max_depth,
                                         alpha, beta, True, ai_player, heuristic_fn)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    self.nodes_pruned += (len(valid_moves) - (valid_moves.index((row, col)) + 1))
                    break
            return min_eval

    def get_best_move(self, game_state, player, max_depth, heuristic_fn):
        """
        Finds the optimal move for player given depth and heuristic function.
        Randomly selects among multiple moves that share the highest score.
        Returns: (best_move, nodes_evaluated, nodes_pruned, elapsed_time)
        """
        self.nodes_evaluated = 0
        self.nodes_pruned = 0
        start_time = time.perf_counter()

        best_score = -math.inf
        best_moves = []
        valid_moves = game_state.get_valid_moves()

        for row, col in valid_moves:
            child_state = game_state.clone()
            child_state.make_move(row, col, player)
            move_score = self.search(child_state, 1, max_depth, -math.inf, math.inf, False, player, heuristic_fn)

            if move_score > best_score:
                best_score = move_score
                best_moves = [(row, col)]
            elif move_score == best_score:
                best_moves.append((row, col))

        elapsed_time = time.perf_counter() - start_time
        chosen_move = random.choice(best_moves) if best_moves else None

        return chosen_move, self.nodes_evaluated, self.nodes_pruned, elapsed_time