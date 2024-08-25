import pygame
from . import bullet

shredder_group = pygame.sprite.Group()

class Shredder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/shredder.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.previous_shot = pygame.time.get_ticks()
    def update(self, screen_width):
        speed = 10
        reload_cooldown = 190
        current_time = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed
        if key[pygame.K_SPACE
               ] and current_time - self.previous_shot >= reload_cooldown:
            shredder_bullet = bullet.Bullet(self.rect.centerx, self.rect.top)
            bullet.bullet_group.add(shredder_bullet)
            self.previous_shot = current_time
        
        self.mask = pygame.mask.from_surface(self.image)

def add_shredder_if_none(screen_width, screen_height):
    if len(shredder_group) is 0:
        shredder_ship = Shredder(int(screen_width / 2), 
                                     screen_height - 75)
        shredder_group.add(shredder_ship)

