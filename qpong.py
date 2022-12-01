import pygame

from assets import paddle
from assets.paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    exit = False
    classical_paddle = Paddle()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)

    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # draw game
        moving_sprites.draw(screen)
        pygame.display.flip()

        # control framerate
        clock.tick(60)

if __name__ == '__main__':
    main()