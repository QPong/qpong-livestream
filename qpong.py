import pygame

from utils.parameters import WINDOW_SIZE
import scene
import inputstream

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

scene_manager = scene.SceneManager()
game_scene = scene.GameScene(scene)
scene_manager.push(game_scene)

input_stream = inputstream.InputStream()

def main():
    
    running = True
    while running:

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        input_stream.processInput()

        if scene_manager.isEmpty():
            running = False
        scene_manager.input(input_stream)
        scene_manager.update(input_stream)
        scene_manager.draw(screen)

        clock.tick(60)

if __name__ == '__main__':
    main()