import pygame

from src.entities.circleshape import CircleShape
from src.settings import SHOT_RADIUS

class Shot(CircleShape):
    shot_image: pygame.Surface = None  # type: ignore
    
    def __init__(self, position: pygame.Vector2, rotation: float):
        super().__init__(position, SHOT_RADIUS)
        
        if Shot.shot_image is None:
            shot_image = pygame.image.load("assets/shot.png").convert_alpha()
            Shot.shot_image = pygame.transform.scale(shot_image,
                                                     (SHOT_RADIUS * 4, SHOT_RADIUS * 4))    # TODO: remove hardocoding
 
        self.image = Shot.shot_image
        self.rect = self.image.get_rect(center=position)
        self.rotation = rotation
        
    def update(self, dt: float):
        self.position +=  self.velocity * dt
        self.image = pygame.transform.rotate(Shot.shot_image, 180 - self.rotation)
        self.rect = self.image.get_rect(center=self.position)