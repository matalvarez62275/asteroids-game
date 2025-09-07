import pygame
from typing import Optional, Tuple

from src.entities.imagesprite import ImageSprite

class Heart(ImageSprite):
    heart_image: pygame.Surface = None  # type: ignore

    def __init__(self, position: pygame.Vector2):
        self._layer = 10
        if Heart.heart_image is None:
            heart_image = pygame.image.load("assets/heart.png").convert_alpha()
            Heart.heart_image = pygame.transform.scale(heart_image, (40, 40))  # TODO: remove hardocoding

        super().__init__(position, Heart.heart_image)
        
        self.visible = True