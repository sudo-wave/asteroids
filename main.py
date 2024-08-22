import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
