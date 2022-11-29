import pygame
from . import parameters
from . import colors

class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.Surface([parameters.WIDTH_UNIT, parameters.WIDTH_UNIT])
        self.image.fill(colors.WHITE)
        self.rect = self.image.get_rect()
        self.velocity = [1, 1]
        self.initial_speed = 2

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.y < 0 or self.rect.y > parameters.SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]