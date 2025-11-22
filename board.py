import pygame
from cell import Cell
from sudoku_generator import generate_sudoku


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, difficulty)
        self.original_board = [row[:] for row in self.board]
        self.cells = self._create_cells()
        self.selected_cell = None

        self.cell_size = self.width // 9

        #centers the board by adding offset
        self.x_offset = (600 - self.width) // 2
        self.y_offset = (600 - self.height) // 2




    def _create_cells(self):
        cells = []
        for r in range(9):
            row = []
            for c in range(9):
                row.append(Cell(self.board[r][c], r, c, self.screen))
            cells.append(row)
        return cells

    def draw(self):
        for r in range(10):
            thickness = 4 if r % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0),
                 (self.x_offset, self.y_offset + r*self.cell_size),
                 (self.x_offset + self.width, self.y_offset + r*self.cell_size),
                 thickness)
            pygame.draw.line(self.screen, (0, 0, 0),
                 (self.x_offset + r*self.cell_size, self.y_offset),
                 (self.x_offset + r*self.cell_size, self.y_offset + self.height),
                 thickness)

        for row in self.cells:
            for cell in row:
                cell.draw(self.cell_size, self.x_offset, self.y_offset)

    def select(self, row, col):
        if self.selected_cell:
            r, c = self.selected_cell
            self.cells[r][c].selected = False

        self.cells[row][col].selected = True
        self.selected_cell = (row, col)

    def click(self, x, y):

        x_rel = x - self.x_offset #Need these because of the offset added
        y_rel = y - self.y_offset

        if 0 <= x < self.width and 0 <= y < self.height:
            return (y_rel // self.cell_size, x_rel // self.cell_size)
        return None

    def clear(self):
        if self.selected_cell:
            r, c = self.selected_cell

            if self.original_board[r][c] == 0:
                self.cells[r][c].sketched_value = 0
                if self.cells[r][c].value != 0:
                    self.cells[r][c].value = 0

    def sketch(self, value):
        if self.selected_cell:
            r, c = self.selected_cell
            if self.original_board[r][c] == 0:
                self.cells[r][c].set_sketched_value(value)
                self.cells[r][c].sketched_value = 0

    def place_number(self, value):
        if self.selected_cell:
            r, c = self.selected_cell
            self.cells[r][c].set_cell_value(value)
            self.cells[r][c].sketched_value = 0

    def reset_to_original(self):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].sketched_value = 0
                self.cells[r][c].value = self.board[r][c]

    def is_full(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return False
        return True

    def update_board(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c] = self.cells[r][c].value

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return (r, c)
        return None

    def check_board(self):
        self.update_board()

        for r in range(9):
            if sorted(self.board[r]) != list(range(1, 10)):
                return False


        for c in range(9):
            col = [self.board[r][c] for r in range(9)]
            if sorted(col) != list(range(1, 10)):
                return False

        for rs in range(0, 9, 3):
            for cs in range(0, 9, 3):
                block = []
                for r in range(rs, rs + 3):
                    for c in range(cs, cs + 3):
                        block.append(self.board[r][c])
                if sorted(block) != list(range(1, 10)):
                    return False
        return True
