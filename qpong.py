import pygame

from model import CircuitGridModel, CircuitGridNode
from model import circuit_node_types as node_types
from controls import CircuitGrid

pygame.init()

WINDOW_WIDTH=1200
WINDOW_HEIGHT=750
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT
screen = pygame.display.set_mode(WINDOW_SIZE)

def main():
    pygame.display.set_caption('QPong')
    exit = False
    
    circuit_grid_model = CircuitGridModel(3, 16)
    circuit_grid_model.set_node(0, 0, CircuitGridNode(node_types.IDEN))

    circuit_grid = CircuitGrid(5, WINDOW_HEIGHT*0.65, circuit_grid_model)
    circuit_grid.draw(screen)

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()

if __name__ == '__main__':
    main()