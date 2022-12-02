import pygame

from . import globals

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([globals.WIDTH_UNIT, globals.WIDTH_UNIT])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        self.velocity = [1,2]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.y < 0 or self.rect.y > globals.FIELD_HEIGHT - globals.WIDTH_UNIT:
            self.velocity[1] = -self.velocity[1]
