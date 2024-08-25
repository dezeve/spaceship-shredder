import pygame

class Button():
    def __init__(self, x, y, button_text, font_size):
        button = pygame.Surface((175, 40))
        button.fill((179, 0, 89))
        font = pygame.font.Font(None, font_size)
        text = font.render(button_text, True, (255, 255, 255))
        self.image = button
        self.rect = button.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.text = text
    def draw(self, screen):
        is_clicked = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed(
            )[0] == 1 and self.clicked == False:
                is_clicked = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.x + 20, self.rect.y + 6))

        return is_clicked
