import pygame

from utils.colors import WHITE
from utils.parameters import WIDTH_UNIT

class Paddle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image
        self.image.fill(WHITE)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.x = 9 * WIDTH_UNIT