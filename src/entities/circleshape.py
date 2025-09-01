import pygame
from typing import Optional, Tuple

from src.entities.imagesprite import ImageSprite

class CircleShape(ImageSprite):
    def __init__(self, position: pygame.Vector2, radius: float, image: pygame.Surface):
        super().__init__(position, image)
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def update(self, dt: int):
        pass
    
    def collides_with(self, other: "CircleShape") -> bool:
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)