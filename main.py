import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # surface object
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # delta time
    dt = 0

    while True:  # game loop
        for event in pygame.event.get():  # gets all user inputs or events happening
            if event.type == pygame.QUIT:
                return  # close game

        # background color
        screen.fill("black")

        player.update(dt)

        player.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # cap fps to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
