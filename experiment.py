"""
experiment.py - Experimentation Framework & CSV Result Recording
"""

import csv
import os
from game import TicTacToe
from agents import Agent


class Experiment:
    """Manages depth benchmarks, multi-agent battles, and file logging."""

    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run_depth_experiment(self, heuristic_fn, depths=[1, 2, 3, 4]):
        """
        PART 10: Experiment 1 - Evaluates computational cost across search depths.
        """
        print("\n" + "=" * 60)
        print(" EXPERIMENT 1: EFFECT OF SEARCH DEPTH")
        print("=" * 60)
        print(f"{'Depth':<8}{'Nodes Evaluated':<18}{'Nodes Pruned':<18}{'Time (s)':<12}")
        print("-" * 60)

        for d in depths:
            game = TicTacToe()
            agent = Agent("BenchmarkAgent", d, heuristic_fn)
            agent.symbol = 'X'
            
            # Execute one initial search step on an empty board to measure depth cost
            move, nodes_eval, nodes_pruned, search_time = agent.choose_move(game)
            print(f"{d:<8}{nodes_eval:<18}{nodes_pruned:<18}{search_time:<12.6f}")

    def run_battle(self, agent1, agent2, num_games=10):
        """
        PART 11 & 12: Experiment 2 - AI Battle with alternating starting players.
        Saves individual game telemetry into results/results.csv.
        """
        filepath = os.path.join(self.output_dir, "results.csv")
        
        print("\n" + "=" * 70)
        print(f" EXPERIMENT 2: AI AGENT BATTLE ({agent1.name} vs {agent2.name})")
        print("=" * 70)

        results_data = []

        with open(filepath, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                "game", "first", "winner", "moves", 
                "nexus_nodes", "titan_nodes", 
                "nexus_pruned", "titan_pruned", "execution_time"
            ])

            for game_num in range(1, num_games + 1):
                game = TicTacToe()
                agent1.reset_stats()
                agent2.reset_stats()

                # Alternate starting player
                if game_num % 2 != 0:
                    first_agent, second_agent = agent1, agent2
                else:
                    first_agent, second_agent = agent2, agent1

                first_agent.symbol = 'X'
                second_agent.symbol = 'O'

                current_agent = first_agent
                moves_count = 0
                game_start_time = 0.0

                while not game.is_terminal():
                    move, _, _, t_time = current_agent.choose_move(game)
                    game.make_move(move[0], move[1], current_agent.symbol)
                    moves_count += 1
                    game_start_time += t_time

                    if game.is_terminal():
                        break

                    current_agent = second_agent if current_agent == first_agent else first_agent

                # Outcome Determination
                winner_symbol = game.check_winner()
                if winner_symbol == agent1.symbol:
                    winner_name = agent1.name
                elif winner_symbol == agent2.symbol:
                    winner_name = agent2.name
                else:
                    winner_name = "DRAW"

                nexus_agent = agent1 if agent1.name == "NEXUS" else agent2
                titan_agent = agent2 if agent2.name == "TITAN" else agent1

                # Save row data
                row = [
                    game_num, first_agent.name, winner_name, moves_count,
                    nexus_agent.total_nodes_evaluated, titan_agent.total_nodes_evaluated,
                    nexus_agent.total_nodes_pruned, titan_agent.total_nodes_pruned,
                    round(nexus_agent.total_time_taken + titan_agent.total_time_taken, 6)
                ]
                writer.writerow(row)
                results_data.append(row)

                print(f"Game {game_num:02d} | First: {first_agent.name:<6} | Winner: {winner_name:<6} | Moves: {moves_count} | NEXUS Nodes: {nexus_agent.total_nodes_evaluated:<5} | TITAN Nodes: {titan_agent.total_nodes_evaluated:<5}")

        print("\nResults successfully saved to:", filepath)
        return results_data