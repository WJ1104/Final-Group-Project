from sudoku_generator import generate_sudoku
#from board import Board (add later)

def print_board(board):
    """Print the Sudoku board in a nice format"""
    if not board:
        print("No board to display")
        return
    
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = ""
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += str(cell if cell != 0 else ".") + " "
        print(row_str)

def main():
    print("=" * 40)
    print("Welcome to Sudoku!")
    print("=" * 40)
    print("\nThis is a Sudoku project template.")
    print("The core classes (Board, Cell) need to be implemented.")
    print("\nGenerating a sample 9x9 Sudoku puzzle with 30 removed cells...")
    print()
    
    try:
        board = generate_sudoku(9, 30)
        print("Generated Sudoku Board:")
        print_board(board)
        print("\nNote: '.' represents empty cells")
    except Exception as e:
        print(f"Error generating Sudoku: {e}")
        print("\nThe sudoku_generator.py has stub methods that need to be implemented:")
        print("- get_board()")
        print("- valid_in_row(), valid_in_col(), valid_in_box()")
        print("- is_valid()")
        print("- fill_box(), fill_diagonal()")
        print("- remove_cells()")

if __name__ == "__main__":
    main()
