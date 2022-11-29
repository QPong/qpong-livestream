import pygame
import numpy as np

from assets.circuit_grid import CircuitGrid, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT
from assets.hud import draw_statevector_grid
from assets.paddle import Paddle, QuantumPaddles
from assets import colors
from assets import parameters

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    circuit_grid = CircuitGrid(5, round(750*0.7))
    left_paddle = Paddle(9 * parameters.WIDTH_UNIT)
    right_paddles = QuantumPaddles(parameters.WINDOW_WIDTH - 9 * parameters.WIDTH_UNIT)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(left_paddle)
    moving_sprites.add(right_paddles.paddles)

    exit = False
    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = True
                elif event.key == pygame.K_a:
                    circuit_grid.move_to_adjacent_node(MOVE_LEFT)
                elif event.key == pygame.K_d:
                    circuit_grid.move_to_adjacent_node(MOVE_RIGHT)
                elif event.key == pygame.K_w:
                    circuit_grid.move_to_adjacent_node(MOVE_UP)
                elif event.key == pygame.K_s:
                    circuit_grid.move_to_adjacent_node(MOVE_DOWN)
                elif event.key == pygame.K_x:
                    circuit_grid.handle_input_x()
                elif event.key == pygame.K_y:
                    circuit_grid.handle_input_y()
                elif event.key == pygame.K_z:
                    circuit_grid.handle_input_z()
                elif event.key == pygame.K_h:
                    circuit_grid.handle_input_h()
                elif event.key == pygame.K_SPACE:
                    circuit_grid.handle_input_delete()
                elif event.key == pygame.K_c:
                    # Add or remove a control
                    circuit_grid.handle_input_ctrl()
                elif event.key == pygame.K_UP:
                    # Move a control qubit up
                    circuit_grid.handle_input_move_ctrl(MOVE_UP)
                elif event.key == pygame.K_DOWN:
                    # Move a control qubit down
                    circuit_grid.handle_input_move_ctrl(MOVE_DOWN)
                elif event.key == pygame.K_LEFT:
                    # Rotate a gate
                    circuit_grid.handle_input_rotate(-np.pi / 8)
                elif event.key == pygame.K_RIGHT:
                    # Rotate a gate
                    circuit_grid.handle_input_rotate(np.pi / 8)

        # draw game
        draw_statevector_grid(screen)
        circuit_grid.draw(screen)
        moving_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    main()
