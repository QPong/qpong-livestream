import pygame

from utils.parameters import WIDTH_UNIT, SCREEN_HEIGHT, NUM_QUBITS, WHITE

class Paddle(pygame.sprite.Sprite):

    def __init__(self, x_pos=0):
        super().__init__()

        self.width = WIDTH_UNIT
        self.height = round(SCREEN_HEIGHT / 2**NUM_QUBITS)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
    
class QuantumPaddles:

    def __init__(self, x_pos):
        self.paddles = []
        for i in range(2**NUM_QUBITS):
            self.paddles.append(Paddle())
        self.set_x_pos(x_pos)
        self.initialize_y_pos()
    
    def initialize_y_pos(self):
        for i in range(len(self.paddles)):
            self.paddles[i].rect.y = i * self.paddles[i].height

    def set_x_pos(self, x_pos):
        for paddle in self.paddles:
            paddle.rect.x = x_pos
 