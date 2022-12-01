import pygame

from assets import paddle, ball, globals, computer

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    exit = False
    classical_paddle = paddle.Paddle(x_pos=50, y_pos=40)
    classical_computer = computer.ClassicalComputer(classical_paddle)
    pong_ball = ball.Ball()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(classical_paddle)
    moving_sprites.add(pong_ball)

    while not exit:
        # update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        pong_ball.update()
        classical_computer.update(pong_ball)

        # draw game
        screen.fill(globals.BLACK)
        moving_sprites.draw(screen)
        pygame.display.flip()

        # control framerate
        clock.tick(60)

if __name__ == '__main__':
    main()