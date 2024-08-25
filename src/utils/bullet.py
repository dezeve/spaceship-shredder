import pygame
from . import enemy

bullet_group = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        self.rect.y -= 12
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, enemy.enemy_group, True,
                                       pygame.sprite.collide_mask):
            self.kill()

