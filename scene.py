import pygame

from utils.parameters import (
    WINDOW_WIDTH, WINDOW_SIZE, SCREEN_HEIGHT, WIDTH_UNIT, RIGHT_EDGE,
    BLACK, MEASUREMENT_COOLDOWN_TIME, WIN_SCORE
)
from utils.ball import Ball
from utils.paddle import Paddle, QuantumPaddles
from utils.player import ClassicalComputer, QuantumComputer
from utils.circuit_grid import CircuitGrid
from utils.hud import draw_score, draw_statevector_grid

class Scene:
    def __init__(self) -> None:
        pass
    def input(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass


class GameScene(Scene):
    def __init__(self, screen):
        self.circuit_grid = CircuitGrid(5, SCREEN_HEIGHT)
        self.left_paddle = Paddle(9 * WIDTH_UNIT)
        self.classical_computer = ClassicalComputer(self.left_paddle)
        self.right_paddles = QuantumPaddles(WINDOW_WIDTH - 9 * WIDTH_UNIT)
        self.quantum_computer = QuantumComputer(self.right_paddles, self.circuit_grid)
        self.ball = Ball(screen)
        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.left_paddle)
        self.moving_sprites.add(self.right_paddles.paddles)
        self.moving_sprites.add(self.ball)

        self.measured_result = 0
        self.last_measurement_time = pygame.time.get_ticks() - MEASUREMENT_COOLDOWN_TIME
        self.quantum_computer.update_paddle_before_measurement()

    def onEnter(self):
        pass

    def input(self, sm, input_stream):
        print('game input')

    def update(self, sm, input_stream):
        self.ball.update()
        
        # if the ball hits the left wall, quantum computer scores 
        if self.ball.rect.x < 0:
            self.quantum_computer.score+=1
            self.quantum_computer.update_paddle_before_measurement()
            self.ball.reset(1)
        # if the ball hits the right wall, classical computer scores 
        elif self.ball.rect.x > WINDOW_WIDTH:
            self.classical_computer.score+=1
            self.quantum_computer.update_paddle_before_measurement()
            self.ball.reset(-1)

        # if the ball hits the top or bottom wall, it bounces back
        if self.ball.rect.y < self.ball.top_edge:
            self.ball.velocity[1] = -self.ball.velocity[1]
        elif self.ball.rect.y > self.ball.bottom_edge:
            self.ball.velocity[1] = -self.ball.velocity[1]

        self.classical_computer.update(self.ball)
        self.quantum_computer.handle_input()

        # trigger measurement
        self.current_time = pygame.time.get_ticks()
        if RIGHT_EDGE - 12 * WIDTH_UNIT < self.ball.rect.centerx < RIGHT_EDGE - 10 * WIDTH_UNIT and \
          self.current_time - self.last_measurement_time > MEASUREMENT_COOLDOWN_TIME:
            self.measured_result = self.quantum_computer.update_paddle_after_measurement()
            self.last_measurement_time = pygame.time.get_ticks()
        
        if pygame.sprite.collide_mask(self.ball, self.left_paddle) or \
            pygame.sprite.collide_mask(self.ball, self.right_paddles.paddles[self.measured_result]):
            self.ball.bounce()
        
    def draw(self, sm, screen):
        screen.fill(BLACK)
        draw_score(self.classical_computer.score, self.quantum_computer.score, screen)
        draw_statevector_grid(screen)
        self.circuit_grid.draw(screen)
        self.moving_sprites.draw(screen)

class GameOverScene(Scene):
    def input(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass



class SceneManager:
    def __init__(self):
        self.scenes = []
    def isEmpty(self):
        return len(self.scenes) == 0
    def enterScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()
    def exitScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()
    def input(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self, inputStream)
    def update(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self, inputStream)
    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        # present screen
        pygame.display.flip()
    def push(self, scene):
        self.exitScene()
        self.scenes.append(scene)
        self.enterScene()
    def pop(self):
        self.exitScene()
        self.scenes.pop()
        self.enterScene()
    def set(self, scenes):
        # pop all scenes
        while len(self.scenes) > 0:
            self.pop()
        # add new scenes
        for s in scenes:
            self.push(s)