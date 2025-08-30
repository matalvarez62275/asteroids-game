import pygame
from typing import Optional, Tuple

class CircleShape(pygame.sprite.Sprite):
    containers: Optional[Tuple[pygame.sprite.Group, ...]] = None

    def __init__(self, position: pygame.Vector2, radius: float):
        if self.containers is not None:
            super().__init__(*self.containers)
        else:
            super().__init__()
            
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, dt: int):
        pass
    
    def collides_with(self, other: "CircleShape") -> bool:
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)