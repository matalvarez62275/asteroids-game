import pygame
from typing import Optional, Tuple

class Heart(pygame.sprite.Sprite):
    containers: Optional[Tuple[pygame.sprite.Group, ...]] = None
    heart_image: pygame.Surface = None  # type: ignore

    def __init__(self, position: pygame.Vector2):
        if self.containers is not None:
            super().__init__(*self.containers)
        else:
            super().__init__()

        if Heart.heart_image is None:
            heart_image = pygame.image.load("assets/heart.png").convert_alpha()
            Heart.heart_image = pygame.transform.scale(heart_image, (40, 40))
        
        self.image = Heart.heart_image
        self.rect = self.image.get_rect(center=position)
        