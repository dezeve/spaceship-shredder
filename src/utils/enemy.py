import pygame

enemy_group = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.direction_x = 1
        self.direction_y = -1
        self.move_distance = 0
        self.max_move_distance = 30
        self.is_rotate = False
    def update(self):
        self.rect.x += self.direction_x
        self.rect.y += self.direction_y
        self.move_distance += 1
        if abs(self.move_distance) > self.max_move_distance:
            self.is_rotate = not self.is_rotate
            if self.is_rotate:
                self.direction_x *= -1
                self.move_distance = 0
            else:
                self.direction_y *= -1 
                self.move_distance = 0
        self.mask = pygame.mask.from_surface(self.image)

def build_enemy():
    rows = 4
    cols = 6
    for row in range(rows):
        for col in range(cols):
            enemy = Enemy(140 + col * 100, 100 + row * 75)
            enemy_group.add(enemy)

