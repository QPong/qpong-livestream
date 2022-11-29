import pygame

import qiskit

class Computer:
    def __init__(self) -> None:
        pass
    def update(self):
        pass
class ClassicalComputer(Computer):
    def __init__(self, paddle) -> None:
        self.paddle = paddle
        self.score = 0
        self.speed = 3

    def update(self, ball):
        if self.paddle.rect.centery - ball.rect.centery > 0:
            self.paddle.rect.y -= self.speed
        else:
            self.paddle.rect.y += self.speed

class QuantumComputer(Computer):
    def __init__(self, quantum_paddle, circuit_grid) -> None:
        self.paddles = quantum_paddle.paddles 
        self.score = 0
        self.circuit_grid = circuit_grid
    
    def update(self, measured=False):
        if measured:
            return self.update_paddle_after_measurement()
        else:
            return self.update_paddle_before_measurement()

    def update_paddle_before_measurement(self):
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit, simulator)
        statevector = simulator.run(transpiled_circuit, shots=100).result().get_statevector()

        for basis_state, amplitude in enumerate(statevector):
            self.paddles[basis_state].image.set_alpha(abs(amplitude)**2*255)
        
        return None

    def update_paddle_after_measurement(self):
        simulator = qiskit.BasicAer.get_backend("qasm_simulator")
        circuit = self.circuit_grid.model.compute_circuit()
        circuit.measure_all()
        transpiled_circuit = qiskit.transpile(circuit, simulator)
        counts = simulator.run(transpiled_circuit, shots=1).result().get_counts()
        measured_state = int(list(counts.keys())[0], 2)

        for paddle in self.paddles:
            paddle.image.set_alpha(0)
        self.paddles[measured_state].image.set_alpha(255)

        return measured_state 
