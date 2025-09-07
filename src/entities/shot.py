import pygame

from src.entities.circleshape import CircleShape
from src.settings import SHOT_RADIUS

class Shot(CircleShape):
    shot_image: pygame.Surface = None  # type: ignore
    
    def __init__(self, position: pygame.Vector2, rotation: float):
        if Shot.shot_image is None:
            shot_sheet = pygame.image.load("assets/main_ship/projectiles/auto_cannon_bullet.png").convert_alpha()
            shot_image = shot_sheet.subsurface(pygame.Rect(0, 0, 32, 32)).copy()
            Shot.shot_image = pygame.transform.scale(shot_image, (int(SHOT_RADIUS * 4), int(SHOT_RADIUS * 4)))
 
        super().__init__(position, SHOT_RADIUS, Shot.shot_image)
        self.rotation = rotation
        
    def update(self, dt: float):
        self.position +=  self.velocity * dt
        self.image = pygame.transform.rotate(Shot.shot_image, 180 - self.rotation)
        self.rect = self.image.get_rect(center=self.position)