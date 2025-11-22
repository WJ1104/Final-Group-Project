import pygame

class Cell:
  def __init__(self, value, row, col, screen):
      self.value = value
      self.row = row
      self.col = col
      self.screen = screen
      self.temp = 0
      self.selected = False

def set_cell_value(self, value): 
    self.value= value 

def set_sketched_value(self, value): 
    self.sketched_value= value 

def draw(self): 
    font = pygame.font.SysFont(None, 40)
    x = self.col * 60
    y = self.row * 60

    rect = pygame.Rect(x, y, 60, 60)
    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

    if self.selected:
        pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)

    if self.value != 0:
        text = font.render(str(self.value), True, (0, 0, 0))
        self.screen.blit(text, (x + 20, y + 10))

    elif self.sketched_value != 0:
        sketch_font = pygame.font.SysFont(None, 20)
        text = sketch_font.render(str(self.sketched_value), True, (100, 100, 100))
        self.screen.blit(text, (x + 5, y + 5))
 



 