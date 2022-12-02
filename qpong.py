import pygame

from assets.circuit_grid import CircuitGrid
from assets import globals, ui, paddle

pygame.init()
screen = pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    classical_paddle = paddle.Paddle(9*globals.WIDTH_UNIT)
    quantum_paddles = paddle.QuantumPaddles(globals.WINDOW_WIDTH - 9*globals.WIDTH_UNIT)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)
    moving_sprites.add(quantum_paddles.paddles)

    exit = False
    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        # draw game
        circuit_grid.draw(screen)
        ui.draw_statevector_grid(screen)
        moving_sprites.draw(screen)
        pygame.display.flip()

        # control framerate
        clock.tick(60)

if __name__ == '__main__':
    main()
