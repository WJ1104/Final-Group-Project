import pygame

class Cell:
    def __init__(self, value, row, col, screen_width, screen_height):
        self.value = value
        self.row = row
        self.col = col
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.sketched_value = 0
        self.selected = False
        
    def set_cell_value(self, value):
        self.value = value
        
    def set_sketched_value(self, value):
        self.sketched_value = value
        
    def draw(self, screen):
        cell_size = self.screen_width // 9
        x = self.col * cell_size
        y = self.row * cell_size
        
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)
        
        if self.value != 0:
            font = pygame.font.Font(None, 60)
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            screen.blit(text, text_rect)
        elif self.sketched_value != 0:
            font = pygame.font.Font(None, 30)
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            screen.blit(text, (x + 5, y + 5))
