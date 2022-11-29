import pygame

from . import parameters
from . import colors


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0) -> None:
        super().__init__()

        self.width = parameters.WIDTH_UNIT
        self.height = parameters.PADDLE_HEIGHT
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(colors.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class QuantumPaddles:
    def __init__(self, x_pos=0) -> None:
        self.paddles = []
        for i in range(2**parameters.NUM_QUBITS):
            self.paddles.append(Paddle(x_pos, i*parameters.PADDLE_HEIGHT))
