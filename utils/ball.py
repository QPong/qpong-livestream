import math
import random

import pygame

from utils.parameters import SCREEN_HEIGHT, WINDOW_WIDTH, WIDTH_UNIT
from utils.colors import WHITE


class Ball(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        self.screen_height = SCREEN_HEIGHT
        self.screen_width = WINDOW_WIDTH
        self.width_unit = WIDTH_UNIT
        self.height = self.width_unit
        self.width = self.width_unit

        self.left_edge = self.width_unit
        self.right_edge = self.screen_width - self.left_edge
        self.top_edge = self.width_unit * 0
        self.bottom_edge = self.screen_height - self.top_edge

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.velocity = [0, 0]
        #self.initial_speed_factor = 0.2
        #self.direction = 0

        self.reset()

    def update(self):
        
        self.rect.centerx += self.velocity[0]
        self.rect.centery += self.velocity[1]

        if self.rect.centery <= self.top_edge:
            self.velocity[1] = -self.velocity[1]
        if self.rect.centery > self.bottom_edge - 1 * self.height:
            self.velocity[1] = -self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-2,2)
    
    def reset(self):
        self.rect.centerx = self.screen_width / 2
        self.rect.centery = self.screen_height / 2
        self.velocity = [random.randint(-2,2), random.randint(-2,2)]
