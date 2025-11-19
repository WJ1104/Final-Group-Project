class Cell: 
  def __init__(self, value, row, col, screen):
      self.value = value
      self.row = row
      self.col = col
      self.screen = screen

  def set_value(self, value):
      self.value = value
    
  def set_temp(self, value):
      self.value = value

  def draw(self):
      pass
