import pygame

from utils.parameters import WINDOW_SIZE
import scene

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

scene_manager = scene.SceneManager()
game_scene = scene.GameScene()
scene_manager.push(game_scene)

def main():
    
    while not scene_manager.exit:

        scene_manager.update()
        scene_manager.draw(screen)

        clock.tick(60)

if __name__ == '__main__':
    main()