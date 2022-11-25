import random
import numpy as np

import pygame

from qiskit import BasicAer, execute, ClassicalRegister

from utils.parameters import WIDTH_UNIT, NUM_QUBITS
from utils.circuit_grid import MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT


class ClassicalComputer:

    def __init__(self, paddle):
        self.paddle = paddle
        self.score = 0

    def update(self, ball):
        
        if self.paddle.rect.centery - ball.rect.centery > 0:
            self.paddle.rect.centery -= 3
        else:
            self.paddle.rect.centery += 3

class QuantumComputer:

    def __init__(self, quantum_paddle, circuit_grid, circuit_grid_model):
        self.paddles = quantum_paddle.paddles
        self.score = 0
        self.circuit_grid = circuit_grid
        self.circuit_grid_model = circuit_grid_model
        self.exit = False

    def handle_input(self):
        # pylint: disable=too-many-branches disable=too-many-statements
        """
        Handle quantum player input
        """

        # Handle Input Events
        for event in pygame.event.get():
            pygame.event.pump()

            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit = True
                elif event.key == pygame.K_a:
                    self.circuit_grid.move_to_adjacent_node(MOVE_LEFT)
                elif event.key == pygame.K_d:
                    self.circuit_grid.move_to_adjacent_node(MOVE_RIGHT)
                elif event.key == pygame.K_w:
                    self.circuit_grid.move_to_adjacent_node(MOVE_UP)
                elif event.key == pygame.K_s:
                    self.circuit_grid.move_to_adjacent_node(MOVE_DOWN)
                elif event.key == pygame.K_x:
                    self.circuit_grid.handle_input_x()
                elif event.key == pygame.K_y:
                    self.circuit_grid.handle_input_y()
                elif event.key == pygame.K_z:
                    self.circuit_grid.handle_input_z()
                elif event.key == pygame.K_h:
                    self.circuit_grid.handle_input_h()
                elif event.key == pygame.K_SPACE:
                    self.circuit_grid.handle_input_delete()
                elif event.key == pygame.K_c:
                    # Add or remove a control
                    self.circuit_grid.handle_input_ctrl()
                elif event.key == pygame.K_UP:
                    # Move a control qubit up
                    self.circuit_grid.handle_input_move_ctrl(MOVE_UP)
                elif event.key == pygame.K_DOWN:
                    # Move a control qubit down
                    self.circuit_grid.handle_input_move_ctrl(MOVE_DOWN)
                elif event.key == pygame.K_LEFT:
                    # Rotate a gate
                    self.circuit_grid.handle_input_rotate(-np.pi / 8)
                elif event.key == pygame.K_RIGHT:
                    # Rotate a gate
                    self.circuit_grid.handle_input_rotate(np.pi / 8)

            self.circuit_grid.draw()
            self.update_paddle_before_measurement()
            pygame.display.flip()

    def update_paddle_before_measurement(self):

        backend_sv_sim = BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid_model.compute_circuit()
        job_sim = execute(circuit, backend_sv_sim, shots=100)
        result_sim = job_sim.result()
        quantum_state = result_sim.get_statevector(circuit, decimals=3)

        for basis_state, amplitude in enumerate(quantum_state):
            self.paddles[basis_state].image.set_alpha(abs(amplitude) ** 2 * 255)

    def update_paddle_after_measurement(self):

        backend_sv_sim = BasicAer.get_backend("qasm_simulator")
        circuit = self.circuit_grid_model.compute_circuit()
        creg = ClassicalRegister(NUM_QUBITS)
        circuit.add_register(creg)  # add classical registers for measurement readout
        circuit.measure(circuit.qregs[0], circuit.cregs[0])
        job_sim = execute(circuit, backend_sv_sim, shots=1)
        result_sim = job_sim.result()
        counts = result_sim.get_counts()

        measured_result = int(list(counts.keys())[0], 2)

        for paddle in self.paddles:
            paddle.image.set_alpha(0)
        self.paddles[measured_result].image.set_alpha(255)

        return measured_result