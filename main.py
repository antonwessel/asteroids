import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # game window
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # delta time
    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():  # gets all user inputs or events happening
            if event.type == pygame.QUIT:
                return  # close game

        updatable.update(dt)

        # background color
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # cap fps to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
