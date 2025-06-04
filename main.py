# asteroids built with pygame
# tb.kirby
# blukirby@gmail.com

import pygame
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()
