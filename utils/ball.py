import math
import random

import pygame

from utils.parameters import WINDOW_HEIGHT, WINDOW_WIDTH, WIDTH_UNIT
from utils.colors import WHITE


class Ball(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        self.screen_height = round(WINDOW_HEIGHT * 0.7)
        self.screen_width = WINDOW_WIDTH
        self.width_unit = WIDTH_UNIT
        self.height = self.width_unit
        self.width = self.width_unit

        self.left_edge = self.width_unit
        self.right_edge = self.screen_width - self.left_edge
        self.top_edge = self.width_unit * 0
        self.bottom_edge = self.screen_height - self.top_edge

        self.image = pygame.Surface([self.height, self.width])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.xpos = 0
        self.ypos = 0
        self.speed = 0
        self.initial_speed_factor = 0.2
        self.direction = 0

        self.reset()

    def update(self):
        
        radians = math.radians(self.direction)

        self.xpos += self.speed * math.sin(radians)
        self.ypos -= self.speed * math.cos(radians)

        # Update ball position
        self.rect.x = self.xpos
        self.rect.y = self.ypos

        if self.ypos <= self.top_edge:
            self.direction = (180 - self.direction) % 360
        if self.ypos > self.bottom_edge - 1 * self.height:
            self.direction = (180 - self.direction) % 360
    
    def reset(self):
        self.xpos = self.screen_width / 2
        self.ypos = self.screen_height / 2
        self.speed = self.width_unit * self.initial_speed_factor
        self.direction = random.randrange(-120, 120)
