import pygame

from utils.colors import WHITE
from utils.parameters import WIDTH_UNIT, SCREEN_HEIGHT, NUM_QUBITS

class Paddle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.width = WIDTH_UNIT
        self.height = round(SCREEN_HEIGHT / 2**NUM_QUBITS)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
