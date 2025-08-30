import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position: pygame.Vector2):
        super().__init__(position, SHOT_RADIUS)
        
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "red", self.position, self.radius)
        
    def update(self, dt: float):
        self.position +=  self.velocity * dt