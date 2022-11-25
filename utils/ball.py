import math
import random

import pygame

from utils.parameters import SCREEN_HEIGHT, WINDOW_WIDTH, WIDTH_UNIT, WHITE


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
        self.initial_speed = 4

        self.reset()

    def update(self):
        
        self.rect.centerx += self.velocity[0]
        self.rect.centery += self.velocity[1]

    def bounce(self):
        # ball is speed up 10% after each bounce
        self.velocity[0] = -self.velocity[0]*1.1
        self.velocity[1] = random.randint(-self.initial_speed, self.initial_speed)
    
    def reset(self):
        self.rect.centerx = self.screen_width / 2
        self.rect.centery = self.screen_height / 2
        self.velocity = [random.randint(self.initial_speed/2, self.initial_speed), 
                            random.randint(-self.initial_speed, self.initial_speed)]
