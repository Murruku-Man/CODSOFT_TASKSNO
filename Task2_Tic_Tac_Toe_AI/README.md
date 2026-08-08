# CODSOFT Task 2 - Tic-Tac-Toe AI

## Project Description

This project implements an AI agent that plays Tic-Tac-Toe against a human player.

The AI uses the **Minimax algorithm** to evaluate possible game states and select the best available move. Because Tic-Tac-Toe has a small and finite game tree, the AI can examine possible future moves and play optimally.

## Features

- Human vs AI gameplay
- Human plays as `X`
- AI plays as `O`
- Minimax algorithm for AI decision-making
- Win, loss, and tie detection
- Input validation
- Simple terminal-based interface

## Technologies Used

- Python
- Minimax algorithm
- Game-tree search
- Conditional statements and functions

## How to Run

Make sure Python is installed.

Open a terminal in this folder and run:

```bash
python tic_tac_toe.py
```

## How the AI Works

The AI treats itself as the maximizing player and the human as the minimizing player.

- AI win → score `+1`
- Human win → score `-1`
- Tie → score `0`

The Minimax algorithm recursively explores possible moves and chooses the move with the best score for the AI.

## Example Board

```text
 X | O | X
---+---+---
   | O |  
---+---+---
 X |   |  
```

The human enters a position from `1` to `9`, and the AI calculates its best response.

## Learning Outcome

This project demonstrates basic game theory and search algorithms by implementing an AI agent that evaluates future game states using Minimax.

## Internship Task

**Task 2: Tic-Tac-Toe AI**

The CodSoft Artificial Intelligence internship asks for an AI agent that plays Tic-Tac-Toe against a human player. The task suggests using Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable.
