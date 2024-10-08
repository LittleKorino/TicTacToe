# TicTacToe Game

This is a simple implementation of the classic TicTacToe game using Python and Pygame.

## Features

- Human vs Human gameplay
- Human vs Computer (MiniMax AI) gameplay
- Computer vs Computer (MiniMax AI) gameplay
- Dark and light mode toggle
- Reset game functionality
- Visual indication of winning line

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository
2. Install Pygame: `pip install pygame`

## How to Run

Run the game by executing the `main.py` file:
## Controls

- Mouse: Click on the grid to place X or O
- 'E' key: Toggle between dark and light mode
- Click "Reset" button to start a new game when the game is over

## Game Modes

You can switch between different game modes by uncommenting the respective function calls in the main game loop:

- Human vs Human: `Utilities.HumanVsHuman()`
- Human vs Computer: `Utilities.HumanVsComputerMiniMax()`
- Computer vs Computer: `Utilities.MinimaxVsMinimax()`

## File Structure

- `main.py`: Main game loop and initialization
- `Utilities.py`: Game logic and AI functions
- `drawXO.py`: Drawing functions for game elements
- `Res/`: Directory containing fonts and other resources

## Coordinates Reference

![Reference](Res/Coordinates.png)

