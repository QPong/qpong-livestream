import random

import pygame

from utils.parameters import (
    WINDOW_WIDTH, WINDOW_SIZE, SCREEN_HEIGHT, WIDTH_UNIT, RIGHT_EDGE,
    BLACK, MEASUREMENT_COOLDOWN_TIME, WIN_SCORE
)
from utils.ball import Ball
from utils.paddle import Paddle, QuantumPaddles
from utils.player import ClassicalComputer, QuantumComputer
from utils.hud import draw_score, draw_statevector_grid
from utils.circuit_grid import CircuitGrid

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)

def main():
    pygame.display.set_caption('QPong')
    
    # initialize game
    circuit_grid = CircuitGrid(5, SCREEN_HEIGHT)

    left_paddle = Paddle(9 * WIDTH_UNIT)
    classical_computer = ClassicalComputer(left_paddle)
    right_paddles = QuantumPaddles(WINDOW_WIDTH - 9 * WIDTH_UNIT)
    quantum_computer = QuantumComputer(right_paddles, circuit_grid)
    ball = Ball(screen)

    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(left_paddle)
    moving_sprites.add(right_paddles.paddles)
    moving_sprites.add(ball)

    measured_result = 0
    last_measurement_time = pygame.time.get_ticks() - MEASUREMENT_COOLDOWN_TIME
    quantum_computer.update_paddle_before_measurement()
    
    clock = pygame.time.Clock()

    while not quantum_computer.exit:
        # update game
        ball.update()

        # if the ball hits the left wall, quantum computer scores 
        if ball.rect.x < 0:
            quantum_computer.score+=1
            quantum_computer.update_paddle_before_measurement()
            ball.reset(1)
        # if the ball hits the right wall, classical computer scores 
        elif ball.rect.x > WINDOW_WIDTH:
            classical_computer.score+=1
            quantum_computer.update_paddle_before_measurement()
            ball.reset(-1)

        # if the ball hits the top or bottom wall, it bounces back
        if ball.rect.y < ball.top_edge:
            ball.velocity[1] = -ball.velocity[1]
        elif ball.rect.y > ball.bottom_edge:
            ball.velocity[1] = -ball.velocity[1]

        classical_computer.update(ball)
        quantum_computer.handle_input()

        # trigger measurement
        current_time = pygame.time.get_ticks()
        if RIGHT_EDGE - 12 * WIDTH_UNIT < ball.rect.centerx < RIGHT_EDGE - 10 * WIDTH_UNIT and \
          current_time - last_measurement_time > MEASUREMENT_COOLDOWN_TIME:
            measured_result = quantum_computer.update_paddle_after_measurement()
            last_measurement_time = pygame.time.get_ticks()
        
        if pygame.sprite.collide_mask(ball, left_paddle) or \
            pygame.sprite.collide_mask(ball, right_paddles.paddles[measured_result]):
            ball.bounce()
        
        # draw game
        screen.fill(BLACK)
        draw_score(classical_computer.score, quantum_computer.score, screen)
        draw_statevector_grid(screen)
        circuit_grid.draw(screen)
        moving_sprites.draw(screen)
        pygame.display.update()

        clock.tick(60)

if __name__ == '__main__':
    main()