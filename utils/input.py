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

    def __init__(self, circuit_grid):
        self.exit = False
        self.circuit_grid = circuit_grid

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
                    self.circuit_grid.draw()
                    pygame.display.flip()
                elif event.key == pygame.K_d:
                    self.circuit_grid.move_to_adjacent_node(MOVE_RIGHT)
                    self.circuit_grid.draw()
                    pygame.display.flip()
                elif event.key == pygame.K_w:
                    self.circuit_grid.move_to_adjacent_node(MOVE_UP)
                    self.circuit_grid.draw()
                    pygame.display.flip()
                elif event.key == pygame.K_s:
                    self.circuit_grid.move_to_adjacent_node(MOVE_DOWN)
                    self.circuit_grid.draw()
                    pygame.display.flip()
                elif event.key == pygame.K_x:
                    self.circuit_grid.handle_input_x()
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_y:
                    self.circuit_grid.handle_input_y()
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_z:
                    self.circuit_grid.handle_input_z()
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_h:
                    self.circuit_grid.handle_input_h()
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_SPACE:
                    self.circuit_grid.handle_input_delete()
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_c:
                    # Add or remove a control
                    self.circuit_grid.handle_input_ctrl()
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_UP:
                    # Move a control qubit up
                    self.circuit_grid.handle_input_move_ctrl(MOVE_UP)
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    # Move a control qubit down
                    self.circuit_grid.handle_input_move_ctrl(MOVE_DOWN)
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_LEFT:
                    # Rotate a gate
                    self.circuit_grid.handle_input_rotate(-np.pi / 8)
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                elif event.key == pygame.K_RIGHT:
                    # Rotate a gate
                    self.circuit_grid.handle_input_rotate(np.pi / 8)
                    self.circuit_grid.draw()
                    #self.update_paddle(level, screen, scene)
                    pygame.display.flip()
                #elif event.key == pygame.K_TAB:
                    # Update visualizations
                    #self.update_paddle(level, screen, scene)

    @staticmethod
    def update_paddle(level, screen, scene):
        """
        Update state vector paddle
        """
        # Update visualizations

        circuit_grid_model = level.circuit_grid_model
        right_statevector = level.right_statevector
        circuit_grid = level.circuit_grid
        statevector_grid = level.statevector_grid

        circuit = circuit_grid_model.construct_circuit()
        statevector_grid.paddle_before_measurement(circuit, scene.qubit_num, 100)
        right_statevector.arrange()
        circuit_grid.draw(screen)
        pygame.display.flip()

    @staticmethod
    def move_update_circuit_grid_display(screen, circuit_grid, direction):
        """
        Update circuit grid after move
        """
        circuit_grid.move_to_adjacent_node(direction)
        circuit_grid.draw(screen)
        pygame.display.flip()
