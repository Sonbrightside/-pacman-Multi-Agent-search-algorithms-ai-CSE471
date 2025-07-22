

# 🧠 Pacman Multi-Agent Search — UC Berkeley CS188 Adaptation

Implementations of adversarial and probabilistic multi-agent search strategies for guiding Pacman in a maze with ghosts. This project is adapted from UC Berkeley’s CS188 “Intro to AI” coursework and showcases decision-making under uncertainty and opposition.

---

## 📖 Table of Contents

- [Overview](#overview)  
- [Implemented Questions & Algorithms](#implemented-questions--algorithms)  
- [Project Structure](#project-structure)  
- [Getting Started](#getting-started)  
- [Sample Commands](#sample-commands)  
- [Key Learnings](#key-learnings)  
- [Contact](#contact)  

---

## 🧩 Overview

- **Goal**: Design intelligent agents that choose optimal or near-optimal actions in a multi-agent Pacman environment involving ghosts.
- **Core Concepts**:
  - Adversarial search (Minimax, Alpha-Beta)
  - Probabilistic decision-making (Expectimax)
  - State evaluation design (Reflex Agents)
  - Game tree construction & depth-based planning

---

## ✅ Implemented Questions & Algorithms

| Question | Topic               | Highlights |
|---------:|---------------------|------------|
| Q1       | Reflex Agent        | Heuristic state-action evaluation |
| Q2       | Minimax             | Adversarial search with multiple ghost agents |
| Q3       | Alpha-Beta Pruning | Efficient minimax variant using cutoff |
| Q4       | Expectimax          | Probabilistic reasoning for non-deterministic ghost behavior |

---

.
├── multiAgents.py # Your implementations for all agents
├── pacman.py # Game engine
├── game.py # Underlying game logic
├── util.py # Helper data structures (optional)
├── test_cases/ # Autograder test cases
├── autograder.py # Autograding script
├── layouts/ # Map layouts
└── graphics*.py # Visualization modules


🔧 **File Modified**: `multiAgents.py` only

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Sonbrightside/multiagent-pacman-ai.git
cd multiagent-pacman-ai

# (Optional) Setup a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat # Windows

# Run the base Pacman game
python pacman.py

🕹 Sample Commands

# Run ReflexAgent on testClassic layout
python pacman.py -p ReflexAgent -l testClassic

# Run MinimaxAgent with depth 3
python pacman.py -p MinimaxAgent -a depth=3 -l minimaxClassic

# Run AlphaBetaAgent on smallClassic layout
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

# Run ExpectimaxAgent on minimaxClassic layout
python pacman.py -p ExpectimaxAgent -a depth=3 -l minimaxClassic

# Run autograder for Q2 (Minimax)
python autograder.py -q q2 --no-graphics

📘 Key Learnings

    Multi-Agent Decision Making: Implemented tree-based decision agents that simulate adversarial and stochastic environments.

    Algorithm Generalization: Extended standard minimax and alpha-beta pruning to handle multiple agents.

    Evaluation Function Design: Crafted utility-based heuristics for reflex agents to survive and score in dynamic maps.

    Efficiency & Correctness: Matched node expansion expectations to pass strict autograder checks.

📬 Contact

Have questions or want to collaborate?

📧 Hongju Son — hongju.son@asu.edu
💼 LinkedIn (Insert actual link if available)
