import random

import pygame

from utils.parameters import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_SIZE, WIDTH_UNIT, NUM_QUBITS, SCREEN_HEIGHT,
    LEFT_EDGE, RIGHT_EDGE
)
from utils.colors import BLACK
from utils.ball import Ball
from utils.paddle import Paddle
from utils.player import ClassicalComputer, QuantumComputer
from utils.hud import draw_score
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
    statevector_grid = StatevectorGrid(circuit_grid_model)
    right_statevector = VBox(WIDTH_UNIT*90, WIDTH_UNIT*0, screen, statevector_grid)
    right_statevector.draw()

    # pong
    left_paddle = Paddle()
    left_paddle.rect.x = 9 * WIDTH_UNIT
    classical_computer = ClassicalComputer(left_paddle)
    right_paddle = Paddle()
    right_paddle.rect.x = WINDOW_WIDTH - 9 * WIDTH_UNIT
    quantum_computer = QuantumComputer(right_paddle, circuit_grid, statevector_grid, right_statevector)
    ball = Ball(screen)

    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(left_paddle)
    moving_sprites.add(right_paddle)
    moving_sprites.add(ball)
    
    clock = pygame.time.Clock()

    while not quantum_computer.exit:
        screen.fill(BLACK)

        ball.update()

        if ball.rect.centerx <=0:
            quantum_computer.score+=1
            ball.reset()
        if ball.rect.centerx >= WINDOW_WIDTH:
            classical_computer.score+=1
            ball.reset()
        if ball.rect.centery <= ball.top_edge:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.centery > ball.bottom_edge - 1 * ball.height:
            ball.velocity[1] = -ball.velocity[1]

        classical_computer.update(ball)
        quantum_computer.handle_input()

        # trigger measurement
        if RIGHT_EDGE - 12 * WIDTH_UNIT < ball.rect.centerx < RIGHT_EDGE - 10 * WIDTH_UNIT:
            circuit = circuit_grid_model.compute_circuit()
            pos = statevector_grid.paddle_after_measurement()
            right_statevector.arrange()

            # paddle after measurement
            right_paddle.rect.y = pos * SCREEN_HEIGHT / (2**NUM_QUBITS)
        
        if pygame.sprite.collide_mask(ball, left_paddle) or \
            pygame.sprite.collide_mask(ball, right_paddle):
            ball.bounce()
        
        draw_score(classical_computer.score, quantum_computer.score, screen)
        circuit_grid.draw()
        right_statevector.draw()
        moving_sprites.draw(screen)
        pygame.display.update()

        clock.tick(60)

if __name__ == '__main__':
    main()