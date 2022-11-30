import pygame

from assets import scene

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

def main():

    # initialize game
    scene_manager = scene.SceneManager()
    scene_manager.push(scene.GameScene())

    while not scene_manager.exit:
        # update game
        scene_manager.update()
        # draw game
        scene_manager.draw(screen)

        clock.tick(60)

if __name__ == '__main__':
    main()
