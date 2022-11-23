import random

import pygame

from utils.parameters import WINDOW_HEIGHT, WINDOW_SIZE, WIDTH_UNIT
from utils.colors import BLACK
from utils.input import Input
from utils.ball import Ball
from utils.paddle import Paddle
from model import CircuitGridModel, CircuitGridNode
from model import circuit_node_types as node_types
from controls import CircuitGrid
from viz import StatevectorGrid
from containers import VBox

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)

def main():
    pygame.display.set_caption('QPong')
    exit = False
    
    # initialize circuit grid
    circuit_grid_model = CircuitGridModel(3, 16)
    circuit_grid_model.set_node(0, 0, CircuitGridNode(node_types.IDEN))
    circuit_grid = CircuitGrid(5, WINDOW_HEIGHT*0.7, circuit_grid_model, screen)
    circuit_grid.draw()

    # initialize statevector grid
    statevector_grid = StatevectorGrid(circuit_grid_model, 3, 100)
    right_statevector = VBox(WIDTH_UNIT*90, WIDTH_UNIT*0, screen, statevector_grid)
    right_statevector.draw()

    # initialize input
    input = Input(circuit_grid, statevector_grid, right_statevector)

    # pong
    left_paddle = Paddle()
    left_paddle.rect.x = 9 * WIDTH_UNIT
    #right_paddle = Paddle()
    ball = Ball(screen)

    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(left_paddle)
    moving_sprites.add(ball)
    
    clock = pygame.time.Clock()

    while not input.exit:
        screen.fill(BLACK)

        input.handle_input()
        ball.update()

        left_paddle.rect.y = (
            ball.rect.y
            - left_paddle.height/2
            + random.randint(- WIDTH_UNIT*4, WIDTH_UNIT*4)
        )

        moving_sprites.update()

        circuit_grid.draw()
        right_statevector.draw()
        moving_sprites.draw(screen)
        pygame.display.update()

        clock.tick(60)

if __name__ == '__main__':
    main()