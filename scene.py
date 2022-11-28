import pygame

from utils.parameters import (
    WINDOW_WIDTH, WINDOW_SIZE, SCREEN_HEIGHT, WIDTH_UNIT, RIGHT_EDGE,
    BLACK, MEASUREMENT_COOLDOWN_TIME, WIN_SCORE, WHITE
)
from utils.ball import Ball
from utils.paddle import Paddle, QuantumPaddles
from utils.player import ClassicalComputer, QuantumComputer
from utils.circuit_grid import CircuitGrid
from utils.hud import draw_score, draw_statevector_grid
from utils.resources import Font

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
    def __init__(self):
        self.circuit_grid = CircuitGrid(5, SCREEN_HEIGHT)
        self.left_paddle = Paddle(9 * WIDTH_UNIT)
        self.classical_computer = ClassicalComputer(self.left_paddle)
        self.right_paddles = QuantumPaddles(WINDOW_WIDTH - 9 * WIDTH_UNIT)
        self.quantum_computer = QuantumComputer(self.right_paddles, self.circuit_grid)
        self.ball = Ball()
        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.left_paddle)
        self.moving_sprites.add(self.right_paddles.paddles)
        self.moving_sprites.add(self.ball)

        self.measured_result = 0
        self.last_measurement_time = pygame.time.get_ticks() - MEASUREMENT_COOLDOWN_TIME
        self.quantum_computer.update_paddle_before_measurement()

    def update(self, sm):
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
        self.quantum_computer.handle_input(sm)

        # trigger measurement
        self.current_time = pygame.time.get_ticks()
        if RIGHT_EDGE - 12 * WIDTH_UNIT < self.ball.rect.centerx < RIGHT_EDGE - 10 * WIDTH_UNIT and \
          self.current_time - self.last_measurement_time > MEASUREMENT_COOLDOWN_TIME:
            self.measured_result = self.quantum_computer.update_paddle_after_measurement()
            self.last_measurement_time = pygame.time.get_ticks()
        
        if pygame.sprite.collide_mask(self.ball, self.left_paddle) or \
            pygame.sprite.collide_mask(self.ball, self.right_paddles.paddles[self.measured_result]):
            self.ball.bounce()

        if self.quantum_computer.score >= WIN_SCORE:
            sm.push(WinScene())
        elif self.classical_computer.score >= WIN_SCORE:
            sm.push(LoseScene())
        
    def draw(self, sm, screen):
        screen.fill(BLACK)
        draw_score(self.classical_computer.score, self.quantum_computer.score, screen)
        draw_statevector_grid(screen)
        self.circuit_grid.draw(screen)
        self.moving_sprites.draw(screen)

class WinScene(Scene):
    def __init__(self) -> None:
        pass
    def update(self, sm):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sm.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sm.exit = True
                elif event.key == pygame.K_SPACE:
                    sm.push(GameScene())
    def draw(self, sm, screen):
        font = Font()
        screen.fill(BLACK)

        gameover_text = "Congratulations!"
        text = font.gameover_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 10))
        screen.blit(text, text_pos)

        gameover_text = "You demonstrated quantum supremacy"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 22))
        screen.blit(text, text_pos)

        gameover_text = "for the first time in human history!"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 27))
        screen.blit(text, text_pos)

class LoseScene(Scene):
    def __init__(self) -> None:
        pass
    def update(self, sm):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sm.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sm.exit = True
                elif event.key == pygame.K_SPACE:
                    sm.push(GameScene())
    def draw(self, sm, screen):
        font = Font()
        screen.fill(BLACK)

        gameover_text = "Game Over"
        text = font.gameover_font.render(gameover_text, 1, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 10))
        screen.blit(text, text_pos)

        gameover_text = "Classical computer"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 22))
        screen.blit(text, text_pos)

        gameover_text = "still rules the world"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 27))
        screen.blit(text, text_pos)

class SceneManager:
    def __init__(self):
        self.scenes = []
        self.exit = False
    def input(self):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self)
    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self)
    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        # present screen
        pygame.display.flip()
    def push(self, scene):
        self.scenes.append(scene)
    def pop(self):
        self.scenes.pop()
    def set(self, scenes):
        # pop all scenes
        while len(self.scenes) > 0:
            self.pop()
        # add new scenes
        for s in scenes:
            self.push(s)