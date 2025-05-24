import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))  # surface object

    while True:  # game loop
        screen.fill((0, 0, 0))  # black color

        for event in pygame.event.get():  # gets all user inputs or events happening
            if event.type == pygame.QUIT:
                return  # close game

        pygame.display.flip()  # refresh the screen


if __name__ == "__main__":
    main()
