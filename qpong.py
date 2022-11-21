import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

def main():
    pygame.display.set_caption('QPong')
    exit = False
    
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()

if __name__ == '__main__':
    main()