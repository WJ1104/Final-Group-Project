# Sudoku Project

## Overview
This is a fully functional Sudoku game implemented in Python using pygame. The game features a graphical user interface with three difficulty levels (Easy, Medium, Hard), allowing players to solve Sudoku puzzles interactively.

**Current State:** The project is fully functional and ready to use. The game runs with a VNC display showing the pygame GUI.

## Project Structure
- `sudoku.py` - Main entry point that runs the Sudoku game
- `sudoku_generator.py` - Contains the `SudokuGenerator` class for creating Sudoku puzzles
- `board.py` - (Empty) Intended for Board class implementation
- `cell.py` - (Empty) Intended for Cell class implementation
- `main.sh` - Shell script to run the project

## Recent Changes (2025-11-22)
- Successfully migrated project to Replit environment
- Installed pygame using uv package manager
- Updated workflow to use `uv run python sudoku.py` with VNC output
- Added `.pythonlibs/` to .gitignore for virtual environment
- Verified game runs successfully with pygame GUI

## Game Features

### Completed Implementation
- Full pygame-based graphical user interface
- Three difficulty levels: Easy (30 removed cells), Medium (40 removed cells), Hard (50 removed cells)
- Interactive game board with cell selection
- Number input functionality
- Reset, Restart, and Exit buttons
- Win/loss detection
- Start menu for difficulty selection
- Complete Sudoku puzzle generation and validation logic

### Core Components
- `sudoku.py` - Main game loop, menu system, and game state management
- `sudoku_generator.py` - Sudoku puzzle generation with configurable difficulty
- `board.py` - Board class handling the 9x9 grid and game logic
- `cell.py` - Cell class for individual Sudoku cells

## Running the Project
The project runs automatically via the "Run Sudoku" workflow with VNC display, or you can run:
```bash
uv run python sudoku.py
```

The game will open in a VNC window showing the pygame GUI.

## User Preferences
None specified yet.

## Project Architecture
- **Language:** Python 3.11
- **Type:** GUI application using pygame
- **Display:** VNC for graphical output
- **Package Manager:** uv (with virtual environment in `.pythonlibs/`)
- **Pattern:** Object-oriented design with separate classes for game logic
- **Entry Point:** `sudoku.py`
- **Dependencies:** pygame 2.6.1
- **Core Logic:** `SudokuGenerator` class for puzzle generation, `Board` and `Cell` classes for game state
