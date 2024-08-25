import pygame

class Text():
    def __init__(self, text, font_size, color, x, y):
        font = pygame.font.Font(None, font_size)
        text = font.render(text, True, color)
        self.text = text
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))

