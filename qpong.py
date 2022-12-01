import pygame

from assets.circuit_grid import CircuitGrid
from assets import globals, ui

pygame.init()
screen = pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    circuit_grid = CircuitGrid(5, round(globals.FIELD_HEIGHT))

    exit = False
    # main game loop
    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        # draw game
        ui.draw_statevector_grid(screen)
        circuit_grid.draw(screen)
        pygame.display.flip()

        # frame
        clock.tick(60)

if __name__ == '__main__':
    main()