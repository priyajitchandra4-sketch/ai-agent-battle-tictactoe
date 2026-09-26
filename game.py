"""
game.py - Tic-Tac-Toe Game Engine and Board Representation
"""

import copy


class TicTacToe:
    """Represents the 3x3 Tic-Tac-Toe board and game rules."""

    def __init__(self):
        # Empty cells represented by ' '
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        """Displays the current board state in a readable grid format."""
        print("\n  0   1   2")
        for idx, row in enumerate(self.board):
            print(f"{idx} " + " | ".join(row))
            if idx < 2:
                print("  " + "---" * 3)
        print()

    def get_valid_moves(self):
        """Returns a list of tuples (row, col) representing empty cells."""
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == ' ':
                    moves.append((r, c))
        return moves

    def make_move(self, row, col, player):
        """
        Places the player's symbol ('X' or 'O') at (row, col).
        Returns True if the move is valid and executed, False otherwise.
        """
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def check_winner(self):
        """
        Checks for a winner.
        Returns 'X', 'O', or None if no winner exists yet.
        """
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_draw(self):
        """Returns True if board is full and there is no winner, else False."""
        return len(self.get_valid_moves()) == 0 and self.check_winner() is None

    def is_terminal(self):
        """Returns True if game has ended (win or draw)."""
        return self.check_winner() is not None or self.is_draw()

    def clone(self):
        """Returns a deep copy of the game state for simulation."""
        new_game = TicTacToe()
        new_game.board = copy.deepcopy(self.board)
        return new_game