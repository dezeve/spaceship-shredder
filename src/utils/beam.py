import pygame
from . import shredder

beam_group = pygame.sprite.Group()
previous_shot = pygame.time.get_ticks()
beam_reload = 500

class Beam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/beam.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self, screen_height):
        self.rect.y += 8
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, shredder.shredder_group, True,
                                       pygame.sprite.collide_mask):
            self.kill()

