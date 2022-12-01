import pygame

from . import globals

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()

        self.image = pygame.Surface([globals.WIDTH_UNIT, globals.PADDLE_HEIGHT])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
