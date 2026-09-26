"""
main.py - Assignment X_02 Execution Driver
"""

from heuristic import heuristic_h1, heuristic_h2
from agents import Agent
from experiment import Experiment


def main():
    print("=" * 70)
    print(" AI/ML LABORATORY | ASSIGNMENT X_02: AI AGENT BATTLE - TIC-TAC-TOE")
    print("=" * 70)

    # Instantiating Experiment Runner
    exp = Experiment(output_dir="results")

    # 1. Run Search Depth Experiment
    exp.run_depth_experiment(heuristic_fn=heuristic_h1, depths=[1, 2, 3, 4])

    # 2. Configure Named Agents
    # NEXUS: Search Depth 3 with Heuristic H1 (Positional + Line Threat)
    nexus = Agent(name="NEXUS", depth=3, heuristic_fn=heuristic_h1)

    # TITAN: Search Depth 3 with Heuristic H2 (Direct Line Dominance)
    titan = Agent(name="TITAN", depth=3, heuristic_fn=heuristic_h2)

    # 3. Run AI Battle (10 Games)
    battle_results = exp.run_battle(nexus, titan, num_games=10)

    # 4. Print Summary Statistics
    print_summary(battle_results)


def print_summary(results):
    nexus_wins = sum(1 for r in results if r[2] == "NEXUS")
    titan_wins = sum(1 for r in results if r[2] == "TITAN")
    draws = sum(1 for r in results if r[2] == "DRAW")

    total_nexus_nodes = sum(r[4] for r in results)
    total_titan_nodes = sum(r[5] for r in results)
    avg_nexus_nodes = total_nexus_nodes / len(results)
    avg_titan_nodes = total_titan_nodes / len(results)
    avg_time = sum(r[8] for r in results) / len(results)

    print("\n" + "=" * 70)
    print(" BATTLE SUMMARY STATISTICS")
    print("=" * 70)
    print(f" NEXUS Wins       : {nexus_wins}")
    print(f" TITAN Wins       : {titan_wins}")
    print(f" Draws            : {draws}")
    print(f" Avg Nodes NEXUS  : {avg_nexus_nodes:.2f}")
    print(f" Avg Nodes TITAN  : {avg_titan_nodes:.2f}")
    print(f" Avg Match Time   : {avg_time:.6f} seconds")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()