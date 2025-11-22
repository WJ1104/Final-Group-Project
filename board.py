import pygame 
from cell import Cell
from sudoku_generator import generate_sudoku


class Board: 
  def __init__(self, width, height, screen, difficulty): 
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.board= generate_sudoku(9, difficulty)
    self.cells = self._create_cells()
    self.selected_cell= None
    
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
      width = 4 if r % 3 == 0 else 1
      pygame.draw.line(self.screen, (0, 0, 0), (0, r * 60), (540, r * 60), width)
      pygame.draw.line(self.screen, (0, 0, 0), (r * 60, 0), (r * 60, 540), width)

    for row in self.cells:
      for cell in row:
          cell.draw()


  def select(self, row, col): 
    if self.selected_cell:
      r, c = self.selected_cell
      self.cells[r][c].selected = False
    self.cells[row][col].selected = True
    self.selected_cell = (row, col)

  def click(self,x,y): 
    if x < 540 and y < 540:
        return (y // 60, x // 60)
    return None

  def clear(self): 
    if self.selected_cell:
      r, c = self.selected_cell
      if self.cells[r][c].value == 0:
          self.cells[r][c].sketched_value = 0
  
  def sketch(self, value): 
    if self.selected_cell:
      r, c = self.selected_cell
      self.cells[r][c].set_sketched_value(value)

  def place_number(self, value): 
    if self.selected_cell:
      r, c = self.selected_cell
      self.cells[r][c].set_cell_value(value)
    
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
    for r in range(9):
      if len(set(self.board[r])) != 9:
          return False

    for c in range(9):
      col_vals = [self.board[r][c] for r in range(9)]
      if len(set(col_vals)) != 9:
          return False

    for rs in range(0, 9, 3):
      for cs in range(0, 9, 3):
          block = []
          for r in range(rs, rs + 3):
              for c in range(cs, cs + 3):
                  block.append(self.board[r][c])
          if len(set(block)) != 9:
              return False

    return True



