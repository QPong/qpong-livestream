#!/usr/bin/env python
#
# Copyright 2019 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from copy import deepcopy

import pygame

from qiskit import BasicAer, execute, ClassicalRegister

from utils.colors import WHITE, BLACK
from utils.parameters import WIDTH_UNIT, SCREEN_HEIGHT, NUM_QUBITS
from utils.states import comp_basis_states
from utils.font import Font


class StatevectorGrid(pygame.sprite.Sprite):
    """
    Displays a statevector grid
    """
    def __init__(self, circuit_grid_model, num_shots=100):
        pygame.sprite.Sprite.__init__(self)

        self.circuit_grid_model = circuit_grid_model
        self.num_qubits = NUM_QUBITS
        self.num_shots = num_shots

        self.image = None
        self.rect = None
        self.font = Font()
        self.block_size = int(round(SCREEN_HEIGHT / 2**self.num_qubits))
        self.basis_states = comp_basis_states(self.num_qubits)

        self.paddle = pygame.Surface([WIDTH_UNIT, self.block_size])
        self.paddle.fill(WHITE)
        self.paddle.convert()

        self.paddle_before_measurement()

    def display_statevector(self):
        """
        Draw computational basis for a statevector of a specified
        number of qubits
        """
        for qb_idx in range(2**self.num_qubits):
            text = self.font.vector_font.render(
                "|" + self.basis_states[qb_idx] + ">", 1, WHITE
            )
            text_height = text.get_height()
            y_offset = self.block_size * 0.5 - text_height * 0.5
            self.image.blit(text, (2 * WIDTH_UNIT, qb_idx * self.block_size + y_offset))

    def paddle_before_measurement(self):
        """
        Get statevector from circuit, and set the
        paddle(s) alpha values according to basis
        state(s) probabilities
        """
        self.update()
        self.display_statevector()

        backend_sv_sim = BasicAer.get_backend("statevector_simulator")
        self.circuit = self.circuit_grid_model.compute_circuit()
        job_sim = execute(self.circuit, backend_sv_sim, shots=self.num_shots)
        result_sim = job_sim.result()
        quantum_state = result_sim.get_statevector(self.circuit, decimals=3)

        for basis_state, ampl in enumerate(quantum_state):
            self.paddle.set_alpha(int(round(abs(ampl) ** 2 * 255)))
            self.image.blit(self.paddle, (0, basis_state * self.block_size))

    def paddle_after_measurement(self):
        """
        Measure all qubits on circuit
        """
        self.update()
        self.display_statevector()

        ## TODO refactor this part to use the best syntax
        backend_sv_sim = BasicAer.get_backend("qasm_simulator")
        creg = ClassicalRegister(NUM_QUBITS)
        circuit = self.circuit_grid_model.compute_circuit()
        measure_circuit = deepcopy(circuit)  # make a copy of circuit
        measure_circuit.add_register(
            creg
        )  # add classical registers for measurement readout
        measure_circuit.measure(measure_circuit.qregs[0], measure_circuit.cregs[0])
        job_sim = execute(measure_circuit, backend_sv_sim, shots=self.num_shots)
        result_sim = job_sim.result()
        counts = result_sim.get_counts()

        self.paddle.set_alpha(255)
        self.image.blit(
            self.paddle, (0, int(list(counts.keys())[0], 2) * self.block_size)
        )

        return int(list(counts.keys())[0], 2)

    def update(self):
        """
        Update statevector grid
        """
        self.image = pygame.Surface(
            [(self.num_qubits + 1) * 3 * WIDTH_UNIT, SCREEN_HEIGHT]
        )
        self.image.convert()
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
