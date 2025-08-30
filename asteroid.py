import pygame
from random import uniform

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt: float):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)   # type: ignore
        child_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)   # type: ignore
        child_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2