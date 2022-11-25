#!/usr/bin/env python
#
# Copyright 2019 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import pygame
from pygame.constants import RLEACCEL
from utils.parameters import WIDTH_UNIT

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, '../data')

def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
    return sound

def load_font(name, size=2 * WIDTH_UNIT):
    """
    Load font with pygame font

    Parameters:
    name (string): file name
    """
    if not pygame.font.get_init():
        pygame.font.init()

    full_name = os.path.join(data_dir, "font", name)
    try:
        font = pygame.font.Font(full_name, size)
    except pygame.error:
        print("Cannot load font: %s" % full_name)
        error_message = pygame.get_error()
        raise SystemExit(error_message) from pygame.error
    return font

class Font:
    """
    Load fonts
    """

    def __init__(self):
        self.gameover_font = load_font("bit5x3.ttf", 10 * WIDTH_UNIT)
        self.credit_font = load_font("bit5x3.ttf", 2 * WIDTH_UNIT)
        self.replay_font = load_font("bit5x3.ttf", 5 * WIDTH_UNIT)
        self.score_font = load_font("bit5x3.ttf", 12 * WIDTH_UNIT)
        self.vector_font = load_font("bit5x3.ttf", 3 * WIDTH_UNIT)
        self.player_font = load_font("bit5x3.ttf", 3 * WIDTH_UNIT)