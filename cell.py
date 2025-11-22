import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, cell_size, x_offset, y_offset):
        x = self.col * cell_size + x_offset
        y = self.row * cell_size + y_offset

        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)

        if self.value != 0:
            font = pygame.font.SysFont(None, int(cell_size * 0.7))
            text = font.render(str(self.value), True, (0, 0, 0))
            text_x = x + (cell_size - text.get_width()) // 2
            text_y = y + (cell_size - text.get_height()) // 2
            self.screen.blit(text, (text_x, text_y))

        elif self.sketched_value != 0:
            sketch_font = pygame.font.SysFont(None, int(cell_size * 0.35))
            text = sketch_font.render(str(self.sketched_value), True, (100, 100, 100))
            self.screen.blit(text, (x + 5, y + 5))
 



 
