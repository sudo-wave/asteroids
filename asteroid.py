import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, ASTEROID_MIN_RADIUS)
        self.velocity = 100

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            width=2,
            radius=self.radius,
            center=self.position,
        )

    def update(self, dt):
        self.position += self.velocity * dt
