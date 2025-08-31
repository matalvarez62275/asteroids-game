import pygame
from typing import Optional, Tuple

class ImageSprite(pygame.sprite.Sprite):
    containers: Optional[Tuple[pygame.sprite.Group, ...]] = None

    def __init__(self, position: pygame.Vector2, image: pygame.Surface, scale: Optional[Tuple[int, int]] = None):
        if self.containers is not None:
            super().__init__(*self.containers)
        else:
            super().__init__()
        
        if scale is not None:
            image = pygame.transform.scale(image, scale)
        
        self.image = image
        self.rect = self.image.get_rect(center=position)
        