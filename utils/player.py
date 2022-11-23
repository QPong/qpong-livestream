import random

import pygame

from utils.parameters import WIDTH_UNIT


class ClassicalComputer:

    def __init__(self, paddle):
        self.paddle = paddle

    def update(self, ball):
        
        if self.paddle.rect.centery - ball.rect.centery > 0:
            self.paddle.rect.centery -= 3
        else:
            self.paddle.rect.centery += 3