#
# Copyright 2022 the original author or authors.
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

"""
Quantum player input events and control
"""

import numpy as np

import pygame

from utils.navigation import MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT


class Input:
    """
    Handle input events
    """

    def __init__(self, circuit_grid, statevector_grid, right_statevector):
        self.exit = False
        self.circuit_grid = circuit_grid
        self.statevector_grid = statevector_grid
        self.right_statevector = right_statevector

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
            self.update_paddle()
            pygame.display.flip()
            
    def update_paddle(self):
        """
        Update state vector paddle
        """
        # Update visualizations
        self.statevector_grid.paddle_before_measurement()
        self.right_statevector.arrange()
        self.right_statevector.draw()

    @staticmethod
    def move_update_circuit_grid_display(screen, circuit_grid, direction):
        """
        Update circuit grid after move
        """
        circuit_grid.move_to_adjacent_node(direction)
        circuit_grid.draw(screen)
        pygame.display.flip()
