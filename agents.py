"""
agents.py - AI Agent Class Definition
"""

from minimax import MinimaxSearch


class Agent:
    """Represents a named AI decision-making agent."""

    def __init__(self, name, depth, heuristic_fn):
        self.name = name
        self.depth = depth
        self.heuristic_fn = heuristic_fn
        self.symbol = None
        self.minimax_engine = MinimaxSearch()

        # Cumulative telemetry counters
        self.total_nodes_evaluated = 0
        self.total_nodes_pruned = 0
        self.total_time_taken = 0.0

    def reset_stats(self):
        """Resets per-game or per-experiment telemetry metrics."""
        self.total_nodes_evaluated = 0
        self.total_nodes_pruned = 0
        self.total_time_taken = 0.0

    def choose_move(self, game_state):
        """
        Executes search algorithm and returns optimal move (row, col).
        Tracks execution performance statistics.
        """
        move, nodes_eval, nodes_pruned, search_time = self.minimax_engine.get_best_move(
            game_state, self.symbol, self.depth, self.heuristic_fn
        )

        self.total_nodes_evaluated += nodes_eval
        self.total_nodes_pruned += nodes_pruned
        self.total_time_taken += search_time

        return move, nodes_eval, nodes_pruned, search_time