import pygame

game_background = pygame.image.load("./assets/background.png")
menu_background = pygame.image.load("./assets/menu.png")

def draw_game_background(screen):
    screen.blit(game_background, (0, 0))
def draw_menu_background(screen):
    screen.blit(menu_background, (0, 0))

