import pygame
from random import uniform

from src.entities.explosion import Explosion
from src.entities.circleshape import CircleShape
from src.settings import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    asteroid_image: pygame.Surface = None  # type: ignore

    def __init__(self, position: pygame.Vector2, radius: float):
        
        if Asteroid.asteroid_image is None:
            Asteroid.asteroid_image = pygame.image.load("assets/environment/asteroids/base.png").convert_alpha()
        
        super().__init__(position, radius, Asteroid.asteroid_image)
        self.image = pygame.transform.scale(Asteroid.asteroid_image,
                                            (int(radius * 5), int(radius * 5)))#TODO: hardcoded
        self.rect = self.image.get_rect(center=position)
        
    def update(self, dt: float):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            Explosion(self.position.copy(), self.radius) # type: ignore
            return

        random_angle = uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_asteroid_1 = Asteroid(self.position.copy(), new_radius)   # type: ignore
        child_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        child_asteroid_2 = Asteroid(self.position.copy(), new_radius)   # type: ignore
        child_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2
        Explosion(self.position.copy(), self.radius) # type: ignore