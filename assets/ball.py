import random

import pygame

from .parameters import SCREEN_HEIGHT, WINDOW_WIDTH, WIDTH_UNIT
from . import colors


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.screen_height = SCREEN_HEIGHT
        self.screen_width = WINDOW_WIDTH

        self.image = pygame.Surface([WIDTH_UNIT, WIDTH_UNIT])
        self.image.fill(colors.WHITE)

        self.rect = self.image.get_rect()

        self.velocity = [0, 0]
        self.initial_speed = 2

        self.reset(1)

    def update(self):
        
        self.rect.centerx += self.velocity[0]
        self.rect.centery += self.velocity[1]

    def bounce(self):
        # ball is speed up 10% after each bounce
        self.velocity[0] = -self.velocity[0] * 1.5
        self.velocity[1] = self.velocity[1] * 1.5
    
    def reset(self, direction):
        self.rect.centerx = self.screen_width / 2
        self.rect.centery = self.screen_height / 2

        if direction > 0:
            self.velocity = [random.randint(2, 4), random.randint(-4, 4)] * self.initial_speed
        else: 
            self.velocity = [random.randint(-4, -2), random.randint(-4, 4)] * self.initial_speed
