import pygame
from typing import Optional, Tuple

from src.entities.imagesprite import ImageSprite

class Heart(ImageSprite):
    heart_image: pygame.Surface = None  # type: ignore

    def __init__(self, position: pygame.Vector2):
        if Heart.heart_image is None:
            Heart.heart_image = pygame.image.load("assets/heart.png").convert_alpha()

        super().__init__(position, Heart.heart_image, scale=(40, 40))
        
        self.visible = True