import pygame

class Cell:
  def __init__(self, value, row, col, screen):
      self.value = value
      self.row = row
      self.col = col
      self.screen = screen
      self.temp = 0
      self.selected = False


  def set_value(self, value):
      self.value = value
    
  def set_temp(self, value):
      self.temp = value

  def draw(self, cell_size = 60):
      x = self.col * cell_size # x position of cell
      y = self.row * cell_size # y position of cell

      if self.selected: #draws a red rectangle outline around cell when selected
          pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)

      font = pygame.font.Font(None, 40) #font for numbers

      if self.value != 0:
          text = font.render(str(self.value), True, (0, 0, 0)) #creates the number in black
          self.screen.blit(text, (x + cell_size // 2 - text.get_width() // 2,
                                  y + cell_size // 2 - text.get_height() // 2)) # centers the text

      elif self.temp != 0:
          temp_font = pygame.font.Font(None, 25)
          text = temp_font.render(str(self.temp), True, (128, 128, 128)) #draws temp number in light gray
          self.screen.blit(text, (x + 5, y + 5)) # puts the temp number in top left


