# Sudoku Project

## Overview
This is a Sudoku game project implemented in Python. It's a template/skeleton project designed for educational purposes, where students implement the core Sudoku game logic.

**Current State:** The project structure is in place, but most of the core logic needs to be implemented. The project runs and will display a message indicating which methods need to be implemented.

## Project Structure
- `sudoku.py` - Main entry point that runs the Sudoku game
- `sudoku_generator.py` - Contains the `SudokuGenerator` class for creating Sudoku puzzles
- `board.py` - (Empty) Intended for Board class implementation
- `cell.py` - (Empty) Intended for Cell class implementation
- `main.sh` - Shell script to run the project

## Recent Changes (2025-11-19)
- Fixed LSP error in `sudoku_generator.py` by providing missing constructor parameters (`board` and `box_length`)
- Created basic `sudoku.py` entry point with board display functionality
- Installed Python 3.11 toolchain
- Added Python `.gitignore`
- Configured "Run Sudoku" workflow for console output

## Implementation Status

### Completed
- Project structure setup
- Python environment configuration
- Basic entry point (`sudoku.py`) with board display
- `SudokuGenerator` constructor fixed
- Helper methods: `fill_remaining()` and `fill_values()` (provided)

### Needs Implementation
The following methods in `sudoku_generator.py` are stubs and need to be implemented:
- `get_board()` - Returns the 2D board list
- `print_board()` - Displays the board (optional, for debugging)
- `valid_in_row(row, num)` - Checks if number is valid in row
- `valid_in_col(col, num)` - Checks if number is valid in column
- `valid_in_box(row_start, col_start, num)` - Checks if number is valid in 3x3 box
- `is_valid(row, col, num)` - Checks if number can be placed at position
- `fill_box(row_start, col_start)` - Fills a 3x3 box with random valid numbers
- `fill_diagonal()` - Fills the three diagonal boxes
- `remove_cells()` - Removes cells to create the puzzle

Additionally, `board.py` and `cell.py` are empty and may need class implementations depending on project requirements.

## Running the Project
The project runs automatically via the "Run Sudoku" workflow, or you can run:
```bash
python sudoku.py
```

## User Preferences
None specified yet.

## Project Architecture
- **Language:** Python 3.11
- **Type:** Console application (TUI)
- **Pattern:** Object-oriented design with separate classes for game logic
- **Entry Point:** `sudoku.py`
- **Core Logic:** `SudokuGenerator` class for puzzle generation
