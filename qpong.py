import pygame

from utils.parameters import WINDOW_HEIGHT, WINDOW_SIZE, WIDTH_UNIT
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
    
    circuit_grid_model = CircuitGridModel(3, 16)
    circuit_grid_model.set_node(0, 0, CircuitGridNode(node_types.IDEN))

    circuit_grid = CircuitGrid(5, WINDOW_HEIGHT*0.7, circuit_grid_model)
    circuit_grid.draw(screen)

    circuit = circuit_grid_model.compute_circuit()
    statevector_grid = StatevectorGrid(circuit, 3, 100)
    right_statevector = VBox(
            WIDTH_UNIT * 90, WIDTH_UNIT * 0, statevector_grid
        )
    right_statevector.draw(screen)

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()

if __name__ == '__main__':
    main()