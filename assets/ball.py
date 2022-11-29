import random

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
        self.reset(direction=-1)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.y < 0 or self.rect.y > parameters.SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]

    def reset(self, direction):
        self.rect.centerx = parameters.WINDOW_WIDTH / 2
        self.rect.centery = parameters.SCREEN_HEIGHT / 2

        if direction > 0:
            self.velocity = [random.randint(2,4), random.randint(-4,4)] * self.initial_speed
        else:
            self.velocity = [random.randint(-4,-2), random.randint(-4,4)] * self.initial_speed

    def bounce(self):
        # ball is sped up 50% after each bounce
        self.velocity[0] = -self.velocity[0] * 1.5
        self.velocity[1] = self.velocity[1] * 1.5