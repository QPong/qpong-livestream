import pygame

from assets.circuit_grid import CircuitGrid, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT
from assets.ui import draw_statevector_grid, draw_score, draw_dashed_line
from assets.paddle import Paddle, QuantumPaddles
from assets.ball import Ball
from assets.player import ClassicalComputer, QuantumComputer
from assets.resources import Font
from assets import colors
from assets import parameters

class Scene:
    def __init__(self) -> None:
        pass
    def update(self, sm):
        pass
    def draw(self, sm, screen):
        pass

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.circuit_grid = CircuitGrid(5, round(750*0.7))
        self.left_paddle = Paddle(9 * parameters.WIDTH_UNIT)
        self.classical_computer = ClassicalComputer(self.left_paddle)
        self.right_paddles = QuantumPaddles(parameters.WINDOW_WIDTH - 9 * parameters.WIDTH_UNIT)
        self.quantum_computer = QuantumComputer(self.right_paddles, self.circuit_grid) 
        self.ball = Ball()
        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.left_paddle)
        self.moving_sprites.add(self.right_paddles.paddles)
        self.moving_sprites.add(self.ball)

    def update(self, sm):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sm.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sm.exit = True
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

        self.ball.update()

        if self.ball.rect.x < 0:
            self.quantum_computer.score += 1
            self.ball.reset(1)
        elif self.ball.rect.x > parameters.WINDOW_WIDTH:
            self.classical_computer.score += 1
            self.ball.reset(-1)

        self.classical_computer.update(self.ball)
        self.quantum_computer.update(self.ball)

        if pygame.sprite.collide_mask(self.ball, self.left_paddle) or \
            pygame.sprite.collide_mask(self.ball, self.right_paddles.paddles[self.quantum_computer.measured_state]):
            self.ball.bounce()

        # check winner
        if self.quantum_computer.score >= parameters.WIN_SCORE:
            sm.push(WinScene())
        elif self.classical_computer.score >= parameters.WIN_SCORE:
            sm.push(LoseScene())

    def draw(self, sm, screen):
        draw_statevector_grid(screen)
        draw_score(self.classical_computer.score, self.quantum_computer.score, screen)
        draw_dashed_line(screen)
        self.circuit_grid.draw(screen)
        self.moving_sprites.draw(screen)

class WinScene(Scene):
    def __init__(self) -> None:
        super().__init__()
    
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
        
        gameover_text = "Congratulations!"
        text = font.gameover_font.render(gameover_text, 5, colors.WHITE)
        text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH / 2, parameters.WIDTH_UNIT * 10))
        screen.blit(text, text_pos)

        gameover_text = "You demonstrated quantum supremacy"
        text = font.replay_font.render(gameover_text, 5, colors.WHITE)
        text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH / 2, parameters.WIDTH_UNIT * 22))
        screen.blit(text, text_pos)

        gameover_text = "for the first time in human history!"
        text = font.replay_font.render(gameover_text, 5, colors.WHITE)
        text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH / 2, parameters.WIDTH_UNIT * 27))
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

        gameover_text = "Game Over"
        text = font.gameover_font.render(gameover_text, 1, colors.WHITE)
        text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH / 2, parameters.WIDTH_UNIT * 10))
        screen.blit(text, text_pos)

        gameover_text = "Classical computer"
        text = font.replay_font.render(gameover_text, 5, colors.WHITE)
        text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH / 2, parameters.WIDTH_UNIT * 22))
        screen.blit(text, text_pos)

        gameover_text = "still rules the world"
        text = font.replay_font.render(gameover_text, 5, colors.WHITE)
        text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH / 2, parameters.WIDTH_UNIT * 27))
        screen.blit(text, text_pos)
    
class SceneManager:
    def __init__(self) -> None:
        self.scenes = []
        self.exit = False
    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self)
    def draw(self, screen):
        screen.fill(colors.BLACK)
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        pygame.display.flip()
    def push(self, scene):
        self.scenes.append(scene)