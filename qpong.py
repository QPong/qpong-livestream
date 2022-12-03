import pygame

from assets.circuit_grid import CircuitGrid
from assets import globals, ui, paddle, ball, computer

pygame.init()
screen = pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    classical_paddle = paddle.Paddle(9*globals.WIDTH_UNIT)
    classical_computer = computer.ClassicalComputer(classical_paddle)
    quantum_paddles = paddle.QuantumPaddles(globals.WINDOW_WIDTH - 9*globals.WIDTH_UNIT)
    quantum_computer = computer.QuantumComputer(quantum_paddles, circuit_grid)
    pong_ball = ball.Ball()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)
    moving_sprites.add(quantum_paddles.paddles)
    moving_sprites.add(pong_ball)

    exit = False
    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        pong_ball.update(classical_computer, quantum_computer)
        classical_computer.update(pong_ball)
        quantum_computer.update(pong_ball)

        # draw game
        screen.fill(globals.BLACK)
        if classical_computer.score >= globals.WIN_SCORE:
            ui.draw_lose_scene(screen)
        elif quantum_computer.score >= globals.WIN_SCORE:
            ui.draw_win_scene(screen)
        else:
            circuit_grid.draw(screen)
            ui.draw_statevector_grid(screen)
            ui.draw_score(screen, classical_computer.score, quantum_computer.score)
            ui.draw_dashed_line(screen)
            moving_sprites.draw(screen)

        pygame.display.flip()

        # control framerate
        clock.tick(60)

if __name__ == '__main__':
    main()
