import pygame
import qiskit

class Computer:
    def __init__(self):
        pass
    def update(self):
        pass

class ClassicalComputer(Computer):
    def __init__(self, paddle):
        self.paddle = paddle
        self.score = 0
        self.speed = 3

    def update(self, ball):
        if self.paddle.rect.centery - ball.rect.centery > 0:
            self.paddle.rect.y -= self.speed
        else:
            self.paddle.rect.y += self.speed
        
        if pygame.sprite.collide_mask(ball, self.paddle):
            ball.bounce()

class QuantumComputer(Computer):
    def __init__(self, quantum_paddles, circuit_grid) -> None:
        self.paddles = quantum_paddles.paddles 
        self.score = 0
        self.circuit_grid = circuit_grid

    def update(self, ball):
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit, simulator)
        statevector = simulator.run(transpiled_circuit, shots=100).result().get_statevector()

        for basis_state, amplitude in enumerate(statevector):
            self.paddles[basis_state].image.set_alpha(abs(amplitude)**2*255)
