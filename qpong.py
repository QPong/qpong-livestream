import pygame

from assets.circuit_grid import CircuitGrid
from assets import ui

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    circuit_grid = CircuitGrid(5, round(750*0.7))

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
        pygame.display.flip()

        # control framerate
        clock.tick(60)

if __name__ == '__main__':
    main()
