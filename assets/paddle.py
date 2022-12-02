import pygame

from . import globals

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()

        self.width = globals.WIDTH_UNIT
        self.height = globals.PADDLE_HEIGHT
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class QuantumPaddles:
    def __init__(self, x_pos=0) -> None:
        self.paddles = []
        for i in range(2**globals.NUM_QUBITS):
            self.paddles.append(Paddle(x_pos, i*globals.PADDLE_HEIGHT))
