# AI Agent Battle: Tic-Tac-Toe

A modular, pure-Python benchmark platform evaluating the impact of search depth, heuristic formulations, and computational trade-offs in Minimax with Alpha-Beta Pruning.

---

## Directory Structure
```text
ai-agent-battle/
├── main.py          # Program entry point & summary reporter
├── game.py          # Tic-Tac-Toe board representation & rules engine
├── minimax.py       # Minimax with Alpha-Beta pruning algorithm
├── agents.py        # Agent abstraction (NEXUS and TITAN)
├── heuristic.py     # Evaluation functions H1 and H2
├── experiment.py    # Framework for depth & battle experiments
└── results/
    └── results.csv  # Auto-generated experiment outputs